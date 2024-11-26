"""
this is a program to create your own pokemon team and analyze it's strength! 
additional sources: 
https://betterdatascience.com/radar-charts-matplotlib-plotly/

"""

import sys # Importing the sys module to use sys.exit()
import time
# import csv
# import json
# import random
import numpy as np
import matplotlib.pyplot as plt
import argparse
import function_library as lib


run = True

while(run) : 
    #set argparser
    parser = argparse.ArgumentParser(description="Get Pokémon data from a file.")
    parser.add_argument('--file', '-f', type=str, help="Path to the Pokémon data file. Defaults to './all_CSVs/mainpoke/pokemon.csv'.")
    args = parser.parse_args()

    if args.file:
        user_path = args.file
    else:
        user_path = "./all_CSVs/mainpoke/pokemon.csv"

    
    data = lib.read_file(user_path)
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List All Pokemon
                2 - List Individual Pokemon
                3 - Choose Six Pokemon Team 
                4 - Choose Random Pokemon Team
                5 - show current team 
                6 - show team analysis
                7 - save team to poketeams.csv
                8 - quit 
                9 - automated team analyzer''') # Added the quit option to display.
                
        
    elif selection == "1" : 
        # list all pokemon 
        lib.list_all_pokemon()
            

    elif selection == "2" :
        # show pokemon stats by search 
        lib.show_pokemon_stats_by_search()

    elif selection == "3" : 
        # choose pokemon team by name 
        # team = lib.choose_pokemon_team_by_name()
        lib.team = lib.pokemon_team()
            

    elif selection == "4" : 
        # generate random pokemon team
        lib.team = lib.generate_random_pokemon_team()
        

    elif selection == "5" :
        # show current team 
        lib.show_current_team()

    elif selection == "6" : 
        # team analysis with chart 
        lib.analyze_team()
            
    elif selection == "7" : 
        # save current or random team to csv file 
       lib.save_team()


    elif selection == '8' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

    elif selection == '9' : 
        # quit program 
        lib.autorun_stat_analyzer_with_random_team()
        

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).