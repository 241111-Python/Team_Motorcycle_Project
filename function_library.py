import re
import sys # Importing the sys module to use sys.exit()
import time
import csv
import json
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="Get Pokémon data from a file.")
parser.add_argument('--file', '-f', type=str, help="Path to the Pokémon data file. Defaults to './all_CSVs/mainpoke/pokemon.csv'.")
args = parser.parse_args()

if args.file:
        user_path = args.file
else:
    user_path = "./all_CSVs/mainpoke/pokemon.csv"

def list_all_pokemon():
    data = read_file(user_path)
    if data:
        for pokemon in data : 
            print(pokemon['name'])

def show_pokemon_stats_by_search():
    data = read_file(user_path)
    if data:
        name = input("Enter Pokemon's name: ")
        individual_entry(data, name)

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
      
def choose_pokemon_team_by_name():
    data = read_file(user_path)
    if data:
        team = pokemon_team(data)
        print("\nYour Chosen Pokemon Team:")
        for i, pokemon in enumerate(team,1):
            print(f"{i}. {pokemon['name']}")
        else:
            print("Data Unavailable")

def generate_random_pokemon_team():
    data = read_file(user_path)
    if data:
        team = random_team(data)
        print("\nYour Random Team:")
        for i, pokemon in enumerate(team,1):
            print(f"{i}. {pokemon['name']}")
        return team

    else:
        print("Data Unavailable")

def show_current_team(team):
    try:
        if team:
            for i, pokemon in enumerate(team,1):
                print(f"{i}. {pokemon['name']}")
    except(NameError):
        print("Team has not been chosen ")    

def analyze_team(team): 
    try:
        if team: 
            averages = team_statanalyzer(team)
        else:
            print("Team has not been chosen.")
    except NameError:
        print("Team has not been chosen.")      

def save_team(team):   
    try:
        if team: 
            print("Saving to file poketeams.csv ")
            with open('./all_CSVs/poketeams.csv', 'a', newline='') as teamfile : 
                fieldnames = ['name', 'types', 'hp', 'attack', 'defense', 
                                'sp_attack', 'sp_defense', 'speed']
                writer = csv.DictWriter(teamfile, fieldnames = fieldnames)
                writer.writeheader
                writer.writerow({})
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

def team_statanalyzer(team):
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

    print("Average Stats Analysis:")
    for stat, avg in average_stats.items():
        print(f"{stat.capitalize()}: {avg:.2f}")
    radar_chart(average_stats)
    return average_stats

def radar_chart(stats):
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
    plt.legend()
    plt.show()

def type_filter(team, data):
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
    regex_to_match = r"0-9"
    while(run):
        iterations = input("How many iterations would you like to run? ")
        if re.match(regex_to_match, iterations):
            print("running stats on " + iterations + " iterations.")

            stats_for_all_runs = {}
            for i in range(iterations):
                random_team = random_team(data)
                analyzer_results = team_statanalyzer(random_team)
                greatest_stat = max(analyzer_results)
                least_stat = min(analyzer_results)
                stats_for_all_runs.append(greatest_stat, least_stat)
                
                # on each run store minimum and maximum stat and names of.
                # On end of iterations output the minimum and maximum stats for each stat.
                
            run = False

            print(stats_for_all_runs)
        else : 
            print("Invalid input. Type a number. ")