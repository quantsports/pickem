#!/usr/bin/python3
from modules.weeks import getAllWeeks, getPrevWeek, getThisWeek
from modules.games import getGames

# ELO variables
hfa = 33    # Base home field advantage
ra = 25     # Additional ELO advantage if coming off bye week
pa = 1.2    # Playoff ELO adjustment factor

#TODO Determine how this should work. Command line args? Something else?
# Assumptions
season = 2020
selectedWeek = 'week12'
allWeeks = getAllWeeks(season)
prevWeek = getPrevWeek(allWeeks, selectedWeek)
games = getGames(allWeeks, selectedWeek, prevWeek)

ranked = []
for g in games:
    g.calculateSpread(hfa, ra, pa, selectedWeek)
    ranked.append(g)
ranked.sort(key=lambda x: x.spread, reverse=True)
    
print ('{:<3} {:<4} {:<5} {:<5} {:<5}'.format('pick', '', '', 'pts', 'spread'))
points = len(ranked)
for g in ranked:
    print ('{:<3} {:<4} {:<6} {:<5} {:<5}'.format(g.pick, 'over', g.loser, points, "-" + str(round(g.spread * 2) / 2)))
    points -= 1