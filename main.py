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
    
    lib.data = lib.read_file(lib.user_path)
    print("""---------------------------------------------
          press h for list of options """)
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List all pokemon.
                2 - List individual pokemon.
                3 - Choose six pokemon team. 
                4 - Choose random pokemon team.
                5 - Show current team. 
                6 - Show team analysis.
                7 - Save team to poketeams.csv.
                8 - Clear chosen team.
                9 - Filter team or all pokemon by type.
                10 - Run the automated team analyzer.
                11 - Or q to quit. ''')
                
        
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


    elif selection == '8':
        # clear selected team 
        print("chosen team cleared")
        lib.team = []


    elif selection == "9":
    # Filter Pokémon by type
       lib.type_filter(lib.data)

    elif selection == '10' : 
        # Auto Stat Analyzer
        lib.autorun_stat_analyzer_with_random_team()


    elif selection == '11' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False
        

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).