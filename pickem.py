#!/usr/bin/python3
import os, csv, datetime, calendar

class game:
    date = ""
    season = ""
    neutral = 0
    playoff = ""
    team1 = ""
    team2 = ""
    elo1_pre = 0
    elo2_pre = 0
    qbelo1_pre = 0
    qbelo2_pre = 0
    qb1 = ""
    qb2 = ""

    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12):
        self.date = datetime.datetime.strptime(var1, '%Y-%m-%d').date()
        self.season = var2
        self.neutral = var3
        self.playoff = var4
        self.team1 = var5
        self.team2 = var6
        self.elo1_pre = var7
        self.elo2_pre = var8
        self.qbelo1_pre = var9
        self.qbelo2_pre = var10
        self.qb1 = var11
        self.qb2 = var12

# Generate file path for csv with elo data
cwd = os.getcwd()
csvPath = cwd + '/nfl_elo_latest.csv'

allGames = []

# Create a list of objects from the csv
with open(csvPath, 'r') as eloCsv:
    next(eloCsv) # Skip past the csv header
    for row in csv.reader(eloCsv):
        allGames.append(game(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[12],row[13],row[14],row[15]))

# region :get dates of each NFL week
# NFL weeks start on Tuesday and end on Monday
# Assumes the -1 index of the csv is the season you wish to calculate for
year = allGames[-1].season

# Find the date of Labor Day as it corresponds to the start of the NFL season
cal = calendar.Calendar(0).monthdatescalendar(int(year), 9)
if cal[0][0].month == 9:
    laborDay = cal[0][0]
else:
    laborDay = cal[1][0]

nflCal = calendar.Calendar(1) # Calendar with Tuesday as first day of week to account for Monday games
weeksCalWithDups = []

# Create list of weeks from September through February
i = 1
m = 9
while i <= 4:
    for w in nflCal.monthdatescalendar(int(year), m):
        weeksCalWithDups.append(w)
    i += 1
    m += 1

m = 1
while i <= 6:
    for w in nflCal.monthdatescalendar(int(year)+1, m):
        weeksCalWithDups.append(w)
    i += 1
    m += 1

# Remove duplicates weeks from when a week spans across months
weeksCal = []
for w in weeksCalWithDups:
    if w not in weeksCal:
        weeksCal.append(w)

index = 1 # We are looking for the NFL week after Labor Day, so index starts at one
for week in weeksCal:
    if laborDay in week:
        break
    else:
        index += 1

allWeeks = {
    'week1':weeksCal[index],
    'week2':weeksCal[index+1],
    'week3':weeksCal[index+2],
    'week4':weeksCal[index+3],
    'week5':weeksCal[index+4],
    'week6':weeksCal[index+5],
    'week7':weeksCal[index+6],
    'week8':weeksCal[index+7],
    'week9':weeksCal[index+8],
    'week10':weeksCal[index+9],
    'week11':weeksCal[index+10],
    'week12':weeksCal[index+11],
    'week13':weeksCal[index+12],
    'week14':weeksCal[index+13],
    'week15':weeksCal[index+14],
    'week16':weeksCal[index+15],
    'week17':weeksCal[index+16],
    'week18':weeksCal[index+17],
    'wildcard':weeksCal[index+18],
    'divisional':weeksCal[index+19],
    'conference':weeksCal[index+20],
    'championship':weeksCal[index+22]
}
# endregion

#TODO Figure out week selection and how you want this to work
selectedWeek = 'week3'

games = []
for d in allWeeks[selectedWeek]:
    for g in allGames:
        if g.date == d:
            games.append(g)

# TODO calculate ELO things like spread