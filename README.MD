# Program description #
- Pokémon Team Builder, Analyzer, and Cron Automation
This Python program is a command-line tool that enables users to create, manage, and analyze custom Pokémon teams, with added functionality for automating tasks using cron jobs. The tool integrates file handling, data visualization, and user interaction to provide a comprehensive experience for Pokémon enthusiasts. This project is ideal for Pokémon enthusiasts, competitive players looking to optimize their teams, or anyone seeking a mix of gaming fun and data-driven automation. 


# Functionality #

- All program functionality below.


## Function #1: List all pokemon

- Lists the names of all pokemon contained in the source file with no user input required.


## Function #2: List individual pokemon by name

- Takes a pokemon name as input and lists the name, type(s), and stats of the pokemon.


## Function #3: Choose six pokemon by name as current team

- Allows the user to create a team of six pokemon by typing the pokemon names and displays the team to the user in a list.


## Function #4: Random team generator

- Generates a random team of six pokemon with no user input required and displays their names to the user in a list.

## Function #5: Show current team

- Shows the current team to the user with no input required.


## Function #6: Show Team analysis

- Displays average stats of current team on the command line and in a pop-up-radar chart for nifty visualization.

## Function #7: Save team to poketeams.csv

- Saves current team to poketeams.csv if it currently exists. Creates it if it does not. No user input required.


## Function #8: Clear chosen team

- Clears the current team from program memory, if a team currently exists.


## Function #9: Filter team or all pokemon by type

- If a team exists, filter it by avalable types. If no team exists, then filter all pokemon by desired type.


## Function #10: Automated team analyzer

- Takes input of how many iterations of random teams desired to be analyzed.
- Then runs analysis of maximum and minimum team stats for a random team for as many iterations as specified.
- Then prints the overall and average highest and lowest stats over all iterations of random teams generated.


## Function #11:

- Sionara.


# Functionality to add (future updates)
## 4 Team strength/weakness analyzer
- Takes input from the user (which team of six pokemon they would like analyzed (could also just be the current team)) and pulls the type(s) for each.
- Analyzes each pokemon's strengths and weaknesses (how many attack types are "super effective" and how many are "not very effective" to each pokemon (Treating "no effects" as not very effective)) and stores that value corresponding to the pokemon.
- Then subtracts the total number of "not very effective" matchups (good) to the total "super effective" matchups (bad) for all pokemon and stores that value.
- Then compares the value stored in the last step to a determined range of values and displays the rating based on where that value lies in that range (Good, average, or poor.).