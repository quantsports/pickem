#!/usr/bin/python3
from modules.weeks import getAllWeeks, getThisSeason, getThisWeek
from modules.games import getGames
from optparse import OptionParser
import sys

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Command line options
parser = OptionParser()
parser.add_option("-w", "--week",
                    dest = "week",
                    help = "Select a specific week.\nOptions: week1, week2, etc, \
                    wildcard, divisonal, conference, championship")
parser.add_option("-s", "--season",
                    dest = "season",
                    help = "Select a specific season.")
parser.add_option("-n", "--numGames",
                    dest = "numGames",
                    type = "int",
                    help = "Select number of games to be ranked.")
parser.add_option("-e", "--elo",
                    dest = "elo",
                    help = "Select 'traditional' or 'qb' elo.")
(options, args) = parser.parse_args()

# Configure season, weeks, and games
season = options.season if options.season else getThisSeason()
allWeeks = getAllWeeks(season)
selectedWeek = str(options.week) if options.week else getThisWeek(allWeeks)
eloType = options.elo if options.elo else "qb"
games = getGames(allWeeks, selectedWeek)
# If there is no data available for the selected week inform the user and then exit
if len(games) < 1:
    print("No data found for " + selectedWeek + " of the " + str(season)+ " season.")
    sys.exit()

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Calculate spread of each game then sort games list by highest win probability
for g in games:
    g.makePick(selectedWeek,eloType)

games.sort(key=lambda x: x.pickprob, reverse=True)
# If numGames option used remove items from games list
if options.numGames:
    if options.numGames < len(games):
        diff = len(games) - options.numGames
        games = games[:-diff]

#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Print output
print(selectedWeek + " " + str(season) + "\n----------")
print ('{:<3} {:<4} {:<5} {:<5} {:<5}'.format('pick', '', '', 'pts', 'prob'))
points = len(games)
for g in games:
    if g.pickprob != 50:
        print ('{:<3} {:<4} {:<6} {:<5} {:<5}'.format(g.pick, 'over', g.loser, points, str(round(g.pickprob)) + "%"))
    else:
        print ('{:<3} {:<4} {:<6} {:<5} {:<5}'.format(g.pick, ' or ', g.loser, points, "PK"))
    points -= 1
print("")