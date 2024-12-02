# Program description #
Pokémon Team Builder, Analyzer, and Cron Automation
This Python program is a command-line tool that enables users to create, manage, and analyze custom Pokémon teams, with added functionality for automating tasks using cron jobs. The tool integrates file handling, data visualization, and user interaction to provide a comprehensive experience for Pokémon enthusiasts. This project is ideal for Pokémon enthusiasts, competitive players looking to optimize their teams, or anyone seeking a mix of gaming fun and data-driven automation.


# Functionality #

All program functionality below.


## Function #1: List all pokemon

Lists the names of all pokemon contained in the source file with no user input required.


## Function #2: List individual pokemon by name

Takes a pokemon name as input and lists the name, type(s), and stats of the pokemon.


## Function #3: Choose six pokemon by name as current team

- Allows the user to create a team of six pokemon by typing the pokemon names and displays the team to the user in a list.


## Function #4: Random team generator

- Generates a random team of six pokemon with no user input required and displays their names to the user in a list.


## 3 Team stats analyzer
- Takes input from the user (which team of six pokemon they would like analyzed) and pulls the stats (HP, attack, defense, SP attack, SP defense, and speed) for each.
- Then averages each stat over the six pokemon and stores those averages.
- Then displays those averages in a radar chart format.
- Also displays ratings (poor, mid, or good) for each stat average, listed below the radar chart in list format.


# Functionality to add (future updates)
## 4 Team strength/weakness analyzer
- Takes input from the user (which team of six pokemon they would like analyzed (could also just be the current team)) and pulls the type(s) for each.
- Analyzes each pokemon's strengths and weaknesses (how many attack types are "super effective" and how many are "not very effective" to each pokemon (Treating "no effects" as not very effective)) and stores that value corresponding to the pokemon.
- Then subtracts the total number of "not very effective" matchups (good) to the total "super effective" matchups (bad) for all pokemon and stores that value.
- Then compares the value stored in the last step to a determined range of values and displays the rating based on where that value lies in that range (Good, average, or poor.).