#!/usr/bin/python3
from modules.weeks import getAllWeeks, getPrevWeek, getThisSeason, getThisWeek
from modules.games import formatSpread, getGames
from optparse import OptionParser
import sys

# ELO variables
hfa = 55    # Base home field advantage
ra = 25     # Additional ELO advantage if coming off bye week
pa = 1.2    # Playoff ELO adjustment factor

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
(options, args) = parser.parse_args()

# Configure season, weeks, and games
season = options.season if options.season else getThisSeason()
allWeeks = getAllWeeks(season)
selectedWeek = str(options.week) if options.week else getThisWeek(allWeeks)
prevWeek = getPrevWeek(allWeeks, selectedWeek)
games = getGames(allWeeks, selectedWeek, prevWeek)
# If there is no data available for the selected week inform the user and then exit
if len(games) < 1:
    print("No data found for " + selectedWeek + " of the " + str(season)+ " season.")
    sys.exit()

# Calculate spread of each game then sort games list by spread
for g in games:
    g.calculateSpread(hfa, ra, pa, selectedWeek)
games.sort(key=lambda x: x.spread, reverse=True)
# If numGames option used remove items from games list
if options.numGames:
    if options.numGames < len(games):
        diff = len(games) - options.numGames
        games = games[:-diff]

# Print output
print(selectedWeek + " " + str(season) + "\n----------")
print ('{:<3} {:<4} {:<5} {:<5} {:<5}'.format('pick', '', '', 'pts', 'spread'))
points = len(games)
for g in games:
    print ('{:<3} {:<4} {:<6} {:<5} {:<5}'.format(g.pick, 'over', g.loser, points, formatSpread(g.spread)))
    points -= 1
print("")