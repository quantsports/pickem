import csv, datetime, os

# TODO vastly simplify this to just use classic and qbelo win probs

#---------------------------------------------------------------------
#---------------------------------------------------------------------
class game:
    date = ''               #var1
    season = ''             #var2
    team1 = ''              #var3
    team2 = ''              #var4
    qb1 = ''                #var5 for future use
    qb2 = ''                #var6 for future use
    qbelo_prob1 = 0         #var7
    qbelo_prob2 = 0         #var8
    team1_offbye = False    # for future use
    team2_offbye = False    # for future use
    pick = ''
    loser = ''
    pickprob = ''
    team1_travdis = 0       # for future use
    team2_travdis = 0       # for future use

    def __init__(self, datevar, seasonvar, team1var, team2var, qb1var, qb2var, qbelo_prob1var, qbelo_prob2var):
        self.date = datetime.datetime.strptime(datevar, '%Y-%m-%d').date()
        self.season = seasonvar
        self.team1 = team1var
        self.team2 = team2var
        self.qb1 = qb1var
        self.qb2 = qb2var
        self.qbelo_prob1 = round(float(qbelo_prob1var) * 100)
        self.qbelo_prob2 = round(float(qbelo_prob2var) * 100)

    def makePick(self, selectedWeek):
        # make a pick based on win probability
        if self.qbelo_prob1 > self.qbelo_prob2:
            self.pick = self.team1
            self.loser = self.team2
            self.pickprob = self.qbelo_prob1
        elif self.qbelo_prob1 < self.qbelo_prob2:
            self.pick = self.team2
            self.loser = self.team1
            self.pickprob = self.qbelo_prob2
        else:
            self.pick = self.team1 # if PK choose the home team
            self.loser = self.team2
            self.pickprob = 50

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Import all games from CSV
scriptDir = os.path.dirname(__file__)
csvPath = os.path.abspath(os.path.join(scriptDir, '..', 'data', 'nfl_elo_latest.csv'))
allGames = []
with open(csvPath, 'r') as eloCsv:
    next(eloCsv)
    for row in csv.reader(eloCsv):
        allGames.append(game(row[0],row[1],row[4],row[5],row[14],row[15],row[20],row[21]))

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Select games by matching their date to weeks
# Also look back at previous week to determine if team is coming off a bye
def getGames(allWeeks, selectedWeek, prevWeek):
    games = []
    prevGames = []

    for d in allWeeks[selectedWeek]:
        for g in allGames:
            if g.date == d:
                games.append(g)

    if selectedWeek != 'week1' and selectedWeek != 'championship':
        for d in allWeeks[prevWeek]:
            for g in allGames:
                if g.date == d:
                    prevGames.append(g)
        
    # If team is discovered in previous week's lineup, offbye is set to False
    for g in games:
        g.team1_offbye = True
        g.team2_offbye = True
        for p in prevGames:
            if g.team1 in (p.team1, p.team2):
                g.team1_offbye = False
            if g.team2 in (p.team1, p.team2):
                g.team2_offbye = False

    return games