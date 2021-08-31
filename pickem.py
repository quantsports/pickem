#!/usr/bin/python3
from modules.weeks import calcWeeks, getPrevWeek, getThisWeek
from modules.games import getGames

# ELO variables
hfa = 55    # Base home field advantage
ra = 25     # Additional ELO advantage if coming off bye week
pa = 1.2    # Playoff ELO adjustment factor

#TODO Determine how this should work. Command line args? Something else?
# Assumptions
season = 2020
selectedWeek = 'week9'
allWeeks = calcWeeks(season)
prevWeek = getPrevWeek(allWeeks, selectedWeek)
games = getGames(allWeeks, selectedWeek, prevWeek)

#TODO Create function to calculate spread
#TODO Itterate through games and calculate spread with ELO variables

# Output is currently just for testing
print ('{:<4} {:<3} {:<10} {:<5} {:<5}'.format('Game', '', '', 't2-ob', 't1-ob'))
for g in games:
    print ('{:<4} {:<3} {:<10} {:<5} {:<5}'.format(g.team2, 'at', g.team1, g.team2_offbye, g.team1_offbye))