#Importing all nececary libraries.
import re
import sys
import time
import csv
import json
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Creating global variables and 
global team

# Leverages the read_file function 
# to list the names of all pokémon.
# (Used as option 1.)
def list_all_pokemon():
    data = read_file(user_path)
    if data:
        for pokemon in data : 
            print(pokemon['name'])

# Leverages the read_file and individual_entry functions
# to list all attributes of a given pokémon by name.
# (Used as option 2.)
def show_pokemon_stats_by_search():
    data = read_file(user_path)
    if data:
        name = input("Enter Pokemon's name: ")
        individual_entry(data, name)

# Creates a DictReader object (reader) and a dictionary object (pokemon)
# and uses the reader to fill the data list with each line as a pokemon
# from the source data file.
# (Not directly referenced in main.)
# (Used in many functions.)
def read_file(user_path):
    #code to read file 
    while True:        
        data = [] 
        try:
            if user_path.endswith('.csv'):
               with open(user_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pokemon = {
                        "name": row["Name"],
                        "types": [row["Type 1"], row["Type 2"]],
                        "hp": int(row["HP"]),
                        "attack": int(row["Attack"]),
                        "defense": int(row["Defense"]),
                        "sp_attack": int(row["Sp. Atk"]),
                        "sp_defense": int(row["Sp. Def"]),
                        "speed": int(row["Speed"])
                    }
                    data.append(pokemon)
                return data
            elif user_path.endswith('.json'):
               with open(user_path, 'r') as file:
                data = json.load(file)
                print(data) #Added functionality to print the data
                return data
            else:
                print("Incorrect file type. File must be a csv or json file.")
        except Exception:
            print(f"Error reading the file: {Exception}. Please try again.")

# Leverages the read_file and random_team functions 
# to choose six pokemon at random,
# persist them to the team list,
# and print the six pokemon names.
# (Used as option 4.)
def generate_random_pokemon_team():
    global team
    data = read_file(user_path)
    if data:
        team = random_team(data)
        print("\nYour Random Team:")
        for i, pokemon in enumerate(team,1):
            print(f"{i}. {pokemon['name']}")
        return team
    else:
        print("Data Unavailable")

# Leverages the read_file and random_team functions 
# to choose six pokemon at random
# and output the team as a list.
# (Not directly referenced in main.)
# (Used in autorun_stat_analyzer_with_random_team function.)
def generate_random_pokemon_team_for_autorun():
    global team
    data = read_file(user_path)
    if data:
        team = random_team(data)
        return team
    else:
        print("Data Unavailable")

# Displays the current stored team.
# (Used as option 5.)
def show_current_team():
    global team
    try:
        if team:
            for i, pokemon in enumerate(team,1):
                print(f"{i}. {pokemon['name']}")
    except(NameError):
        print("Team has not been chosen ")    

# Analyzes stored team's stats by taking the 
def analyze_team(): 
    global team
    try:
        if team: 
            averages = team_statanalyzer()
        else:
            print("Team has not been chosen.")
    except NameError:
        print("Team has not been chosen.")      

def save_team():   
    try:
        if team: 
            with open('./all_CSVs/poketeams.csv', 'a', newline='') as teamfile : 
                print("Saving to file poketeams.csv ")
                fieldnames = ['name', 'types', 'hp', 'attack', 'defense', 
                                'sp_attack', 'sp_defense', 'speed']
                writer = csv.DictWriter(teamfile, fieldnames = fieldnames)
                writer2 = csv.writer(teamfile)
                writer2.writerow("")
                writer.writeheader
                writer.writerows(team) 

        else:
            print("Team has not been chosen.")
    except NameError:
        print("Team has not been chosen.")

            
def individual_entry(data, name):
    track = 0
    for item in data:
        if item["name"].lower() == name.lower():
            print(f"\nDetails for {item['name']}:")
            track+=1
            for key, value in item.items():
                print(f"{key.capitalize()}: {value}")
    
    if track:
        return
    else:
        print(f"No Pokémon found with name '{name}'.")

def pokemon_team():
    data = read_file(user_path)
    team = []
    val=0
    while(val < 6):
        user_input = input("choose pokemon to be added: ")
        for poke in data:
            if poke["name"].lower() == user_input.lower():
                team.append(poke)
                val+=1
                print("Pokemon successfully added to team")
                break
          

    return team

def random_team(data):
    return random.sample(data,6)

def team_statanalyzer():
    global team
    stats = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "sp_attack": 0,
        "sp_defense": 0,
        "speed": 0,
    }
    
    for pokemon in team:
        for key in stats.keys():
            stats[key] += pokemon.get(key, 0)  

    # Calculate the average stats
    average_stats = {key: value / len(team) for key, value in stats.items()}
    
     # Define ratings
    ratings = {}
    for stat, avg in stats.items():
        if avg <= 50:
            ratings[stat] = "Poor"
        elif 50 < avg <= 80:
            ratings[stat] = "Mid"
        else:
            ratings[stat] = "Good"


    print("Average Stats Analysis:")
    for stat, avg in average_stats.items():
        print(f"{stat.capitalize()}: {avg:.2f}")
    radar_chart(average_stats, ratings )
    return average_stats, ratings




def team_statanalyzer_for_autorun():
    global team
    stats = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "sp_attack": 0,
        "sp_defense": 0,
        "speed": 0,
    }

    for pokemon in team:
        for key in stats.keys():
            stats[key] += pokemon.get(key, 0)  
    # Calculate the average stats
    average_stats = {key: value / len(team) for key, value in stats.items()}
    return average_stats

def radar_chart(stats, ratings):
    labels = list(stats.keys())
    values = list(stats.values())
    
    labels = [*labels, labels[0]]
    values = [*values, values[0]]


    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(values))

    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_loc, values, label='Team Stats')
    plt.title('Team Stats Radar Chart', size=20, y=1.05)
    labels = plt.thetagrids(np.degrees(label_loc), labels=labels)
    rating_text = "\n".join([f"{stat.capitalize()}: {rating}" for stat, rating in ratings.items()])
    plt.figtext(0.5, 0.02, f"Ratings:\n{rating_text}", wrap=True, horizontalalignment="center", fontsize=12)
    plt.legend()
    plt.show()

def type_filter(data):
    global team
    if team:
        types = {t for p in team for t in p["types"] if t}  # Get all unique types
        print("Available Types:", ", ".join(types))
        type_filter = input("Enter the type to filter by: ").capitalize()
        filtered_data = [p for p in team if type_filter in p["types"]]
        if filtered_data:
            print(f"\nPokémon with type '{type_filter}':")
            for i, pokemon in enumerate(filtered_data, 1):
                print(f"{i}. {pokemon['name']} - Types: {', '.join(pokemon['types'])}")
        else:
            print(f"No Pokémon found with type '{type_filter}'.")
            return ""
    else:
        print("Team not chosen default to all entry sorting")
        if data:
            types = {t for p in data for t in p["types"] if t}  # Get all unique types
            print("Available Types:", ", ".join(types))
            type_filter = input("Enter the type to filter by: ").capitalize()
            filtered_data = [p for p in data if type_filter in p["types"]]
            if filtered_data:
                print(f"\nPokémon with type '{type_filter}':")
                for i, pokemon in enumerate(filtered_data, 1):
                    print(f"{i}. {pokemon['name']} - Types: {', '.join(pokemon['types'])}")
            else:
                print(f"No Pokémon found with type '{type_filter}'.")
                return ""

        

def autorun_stat_analyzer_with_random_team():
    data = read_file(user_path)
    run = True
    regex_to_match = r"[0-9]"
    while(run):
        
        iterations_str = input("How many iterations would you like to run? ")
        
        if re.match(regex_to_match, iterations_str):
            print("running stats on " + iterations_str + " iterations.")
            iterations = int(iterations_str)
            max_stats_for_all_runs = {}
            min_stats_for_all_runs = {}
            for i in range(iterations):
                random_team = generate_random_pokemon_team_for_autorun()
                analyzer_results = team_statanalyzer_for_autorun()
                max_key = max(analyzer_results, key=analyzer_results.get)
                greatest_stat = analyzer_results[max_key]
                min_key = min(analyzer_results, key=analyzer_results.get)
                least_stat = analyzer_results[min_key]
                max_stats_for_all_runs[i] = greatest_stat
                min_stats_for_all_runs[i] = least_stat
                
                # on each run store minimum and maximum stat and names of.
                # On end of iterations output the minimum and maximum stats for each stat.
                
            run = False
            highest_overall_stat = max(max_stats_for_all_runs.values())
            lowest_overall_stat = min(min_stats_for_all_runs.values())
            average_highest_stat=(sum(max_stats_for_all_runs.values()) // iterations)
            average_lowest_stat=(sum(min_stats_for_all_runs.values()) // iterations)
            print("The overall highest stat = " + str(highest_overall_stat))
            print("The overall lowest stat = " + str(lowest_overall_stat))
            print("The average highest stat = " + str(average_highest_stat))
            print("The average lowest stat = " + str(average_lowest_stat))
        else : 
            print("Invalid input. Type a number. ")

parser = argparse.ArgumentParser(description="Get Pokémon data from a file.")
parser.add_argument('--file', '-f', type=str, help="Path to the Pokémon data file. Defaults to './all_CSVs/mainpoke/pokemon.csv'.")
parser.add_argument('--save_random_team', '-srt', action='store_true', help='generate random team, save team to file')
args = parser.parse_args()

if args.file:
    user_path = args.file
else:
    user_path = "./all_CSVs/mainpoke/pokemon.csv"

if args.save_random_team:
    print("saving a random team to file...")
    team = generate_random_pokemon_team()
    save_team()
    time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
    sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).