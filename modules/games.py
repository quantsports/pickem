import csv, datetime, os

class game:
    date = ''           #var1
    season = ''         #var2
    neutral = 0         #var3
    playoff = ''        #var4
    team1 = ''          #var5
    team2 = ''          #var6
    elo1_pre = 0        #var7
    elo2_pre = 0        #var8
    qbelo1_pre = 0      #var9
    qbelo2_pre = 0      #var10
    qb1 = ''            #var11
    qb2 = ''            #var12
    qbelo_prob1 = 0     #var13
    qbelo_prob2 = 0     #var14
    team1_offbye = ''
    team2_offbye = ''
    spread = 0
    pick = ''

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14):
        self.date = datetime.datetime.strptime(var1, '%Y-%m-%d').date()
        self.season = var2
        self.neutral = int(var3)
        self.playoff = var4
        self.team1 = var5
        self.team2 = var6
        self.elo1_pre = float(var7)
        self.elo2_pre = float(var8)
        self.qbelo1_pre = float(var9)
        self.qbelo2_pre = float(var10)
        self.qbelo_prob1 = float(var13)
        self.qbelo_prob2 = float(var14)
        self.qb1 = var11
        self.qb2 = var12

# Import all games from CSV
scriptDir = os.path.dirname(__file__)
csvPath = os.path.abspath(os.path.join(scriptDir, '..', 'data', 'nfl_elo_latest.csv'))
allGames = []
with open(csvPath, 'r') as eloCsv:
    next(eloCsv)
    for row in csv.reader(eloCsv):
        allGames.append(game(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[12],row[13],row[14],row[15],row[20],row[21]))

# Select games by matching their date to weeks
# Also look back at previous week to determine if team is coming off a bye
def getGames(allWeeks, selectedWeek, prevWeek):
    games = []
    prevGames = []

    for d in allWeeks[selectedWeek]:
        for g in allGames:
            if g.date == d:
                games.append(g)

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