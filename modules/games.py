import csv, datetime, os

#---------------------------------------------------------------------
#---------------------------------------------------------------------
class game:
    date = ''               #var1
    season = ''             #var2
    team1 = ''              #var3
    team2 = ''              #var4
    elo_prob1 = ''          #var5
    elo_prob2 = ''          #var6
    qb1 = ''                #var7 for future use
    qb2 = ''                #var8 for future use
    qbelo_prob1 = 0         #var9
    qbelo_prob2 = 0         #var10
    pick = ''
    loser = ''
    pickprob = ''

    def __init__(self, datevar, seasonvar, team1var, team2var, elo_prob1var, elo_prob2var, qb1var, qb2var, qbelo_prob1var, qbelo_prob2var):
        self.date = datetime.datetime.strptime(datevar, '%Y-%m-%d').date()
        self.season = seasonvar
        self.team1 = team1var
        self.team2 = team2var
        self.elo_prob1 = round(float(elo_prob1var) * 100)
        self.elo_prob2 = round(float(elo_prob2var) * 100)
        self.qb1 = qb1var
        self.qb2 = qb2var
        self.qbelo_prob1 = round(float(qbelo_prob1var) * 100)
        self.qbelo_prob2 = round(float(qbelo_prob2var) * 100)

    def makePick(self, selectedWeek, elo):
        # make a pick based on win probability using qb or classic elo
        if elo == 'qb':
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
        elif elo == 'traditional':
                if self.elo_prob1 > self.elo_prob2:
                    self.pick = self.team1
                    self.loser = self.team2
                    self.pickprob = self.elo_prob1
                elif self.elo_prob1 < self.elo_prob2:
                    self.pick = self.team2
                    self.loser = self.team1
                    self.pickprob = self.elo_prob2
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
        allGames.append(game(row[0],row[1],row[4],row[5],row[8],row[9],row[14],row[15],row[20],row[21]))

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Select games by matching their date to weeks
# Also look back at previous week to determine if team is coming off a bye
def getGames(allWeeks, selectedWeek):
    games = []

    for d in allWeeks[selectedWeek]:
        for g in allGames:
            if g.date == d:
                games.append(g)

    return games