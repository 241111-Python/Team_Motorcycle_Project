"""
this is a program to create your own pokemon team and analyze it's strength! 
additional sources: 
https://betterdatascience.com/radar-charts-matplotlib-plotly/
https://www.serebii.net/pokedex-sv/index.png

"""
# Importing all libraries and functions nececary for program function
import sys
import time
import function_library as lib

run = True

while(run) :
    # Printing list of options to select from.
    lib.data = lib.read_file(lib.user_path)
    print("""---------------------------------------------
          press h for list of options """)
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List all pokémon.
                2 - List individual pokémon.
                3 - Choose six pokemon team. 
                4 - Choose random pokémon team.
                5 - Show current team. 
                6 - Show team analysis.
                7 - Save team to pokéteams.csv.
                8 - Clear chosen team.
                9 - Filter team or all pokémon by type.
                10 - Run the automated team analyzer.
                11 - Or q to quit. ''')
                
        
    elif selection == "1" : 
        # Lists all pokémon names by pokedex #.
        lib.list_all_pokemon()
            

    elif selection == "2" :
        # Shows individual pokémon stats by typing the pokémon name.
        lib.show_pokemon_stats_by_search()

    elif selection == "3" : 
        # Allows you to choose pokémon team by name and persist it.
        lib.team = lib.pokemon_team()
            
    elif selection == "4" : 
        # Generates a random pokemon team.
        lib.team = lib.generate_random_pokemon_team()
        
    elif selection == "5" :
        # Shows the current stored team.
        lib.show_current_team()

    elif selection == "6" : 
        # Displays the team analysis with a radar chart.
        lib.analyze_team()
            
    elif selection == "7" : 
        # Saves current team to csv file.
       lib.save_team('all_CSVs/poketeams.csv')

    elif selection == '8':
        # Clears the current stored team.
        print("chosen team cleared")
        lib.team = []

    elif selection == "9":
    # Filters pokémon by type
       lib.type_filter(lib.data)

    elif selection == '10' : 
        # Auto Stat Analyzer
        lib.autorun_stat_analyzer_with_random_team()

    elif selection == '11' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False
        
# Timer to wait two seconds before terminating the program 
# with a successful exit code of 0.
time.sleep(2)
sys.exit(0)