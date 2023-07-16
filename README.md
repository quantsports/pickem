# pick'em
This is a script that returns a ranked list of games from a given week in the NFL season and displays the likely winner of the game. Teams with the highest percentage chance to win are picked higher and assigned a higher point value.

This project uses the [nfl-elo data set from FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/nfl-elo) which is available under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Download this data set and place in a folder called 'data' to use it with this script. The script is not currently compatible with historic data so you will want to use the **nfl_elo_latest.csv** and not the csv with all historic data.

```
│   .gitignore
│   pickem.py
│   README.md
│
├───data
│       nfl_elo_latest.csv
│
└───modules
    │   games.py
    │   weeks.py
```