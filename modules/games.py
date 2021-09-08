import csv, datetime, os

# TODO vastly simplify this to just use classic and qbelo win probs

#---------------------------------------------------------------------
#---------------------------------------------------------------------
class game:
    date = ''               #var1
    season = ''             #var2
    neutral = 0             #var3
    playoff = ''            #var4
    team1 = ''              #var5
    team2 = ''              #var6
    elo1_pre = 0            #var7 for future use
    elo2_pre = 0            #var8 for future use
    qbelo1_pre = 0          #var9
    qbelo2_pre = 0          #var10
    qb1 = ''                #var11
    qb2 = ''                #var12
    qb1_adj = 0             #var13
    qb2_adj = 0             #var14
    qbelo_prob1 = 0         #var15
    qbelo_prob2 = 0         #var16
    team1_offbye = False    # for future use
    team2_offbye = False    # for future use
    pick = ''
    loser = ''
    pickprob = ''
    team1_travdis = 0   # for future use
    team2_travdis = 0   # for future use

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16):
        self.date = datetime.datetime.strptime(var1, '%Y-%m-%d').date()
        self.season = var2
        self.neutral = int(var3)
        self.playoff = var4
        self.team1 = var5
        self.team2 = var6
        self.elo1_pre = float(var7)
        self.elo2_pre = float(var8)
        try:    # Account for scenario where qbelo_pre value is empty (such as in week1)
            self.qbelo1_pre = float(var9)
        except ValueError:
            self.qbelo1_pre = self.elo1_pre
        try:
            self.qbelo2_pre = float(var10)
        except ValueError:
            self.qbelo2_pre = self.elo2_pre
        self.qb1_adj = float(var13)
        self.qb2_adj = float(var14)
        self.qbelo_prob1 = round(float(var15) * 100)
        self.qbelo_prob2 = round(float(var16) * 100)
        self.qb1 = var11
        self.qb2 = var12

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

        # Determine the spread as a float
        self.spread = abs(self.qbelo2_pre - self.qbelo1_pre) / 25

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Import all games from CSV
scriptDir = os.path.dirname(__file__)
csvPath = os.path.abspath(os.path.join(scriptDir, '..', 'data', 'nfl_elo_latest.csv'))
allGames = []
with open(csvPath, 'r') as eloCsv:
    next(eloCsv)
    for row in csv.reader(eloCsv):
        allGames.append(game(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[12],row[13],row[14],row[15],row[18],row[19],row[20],row[21]))

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