# pick'em
This is a script that returns a ranked list of games from a given week in the NFL season and displays the likely winner of the game. Teams with the highest percentage chance to win are picked higher and assigned a higher point value.

This project uses the [nfl-elo data set from FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/nfl-elo) which is available under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Download this data set and place in a folder called 'data' to use it with this script. The script is not currently compatible with historic data so you will want to use the **nfl_elo_latest.csv** and not the **nfl_elo.csv**.

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

The script can be run with several optional parameters. Default behavior and the parameters are described below.
## Default behavior
By default the script will check the current date and pull relevant info for the current NFL week. The NFL week is assumed to be Wed - Tue (although it's pretty rare, sometimes reshceduled games are plated on Tuesdays). The script uses the Quarterback adjusted Elo by default.
## Optional parameters
| Parameter           | Description       |
|---------------------|-------------------|
|`-w`<br/>`--week`     |Select an NFL week. Format as `week1`, `week2`, etc. For playoffs you can use `wildcard`, `divisional`, `conference`, or `championship`. For example, you could use `python3 .\pickem.py -w week3` to run the script for week 3 of the current NFL season.|
|`-s`<br/>`--season`     |Select an NFL season. Format as `2022`, `2023`, etc.|
|`-n`<br/>`--numGames`    |Select the number of games to be ranked. For example, you could use `python3 .\pickem.py -n 5` to return only the top five ranked games. Assigned point values will be changed accordingly.|
|`-e`<br/>`--elo`         |Select Elo rating type to be used. Valid options are `traditional` and `qb` for Quarterback adjusted Elo. See the 538 [How Our NFL Predicitions Work](https://fivethirtyeight.com/methodology/how-our-nfl-predictions-work/) article for an explanation of Elo.|