import sys # Importing the sys module to use sys.exit()
import time
import csv
import json
import random
import numpy as np
import matplotlib.pyplot as plt


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

def pokemon_team(data):
    poke_team = []
    val=0
    while(val < 6):
        user_input = input("choose pokemon to be added: ")
        for poke in data:
            if poke["name"].lower() == user_input.lower():
                poke_team.append(poke)
                val+=1
                print("Pokemon successfully added to team")
                break
          

    return poke_team

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
   return ""


run = True

while(run) : 
    user_path  ="./all_CSVs/mainpoke/pokemon.csv"
    data = read_file(user_path)
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List All Pokemon
                2 - List Individual Pokemon
                3 - Choose Six Pokemon Team 
                4 - Choose Random Pokemon Team
                5 -
                6 - 
                7 - 
                8 - quit ''') # Added the quit option to display.
    elif selection == "1" : 
        # list all pokemon
        if data:
            print(data) #Added functionality to print the data  
    elif selection == "2" :
        if data:
            name = input("Enter Pokemon's name: ")
            individual_entry(data, name)
    elif selection == "3" : 
        if data:
                team = pokemon_team(data)
                print("\nYour Chosen Pokemon Team:")
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        else:
            print("Data Unavailable")
    elif selection == "4" : 
        if data:
                team = random_team(data)
                print("\nYour Random Team:")
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        else:
            print("Data Unavailable")
    elif selection == "5" :
        try:
            if team:
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        except(NameError):
            print("Team has not been chosen ")
    elif selection == '8' or selection == 'q' : 
        print("quitting")
        run = False
    elif selection == "6" : 
        try:
            if team: 
                averages = team_statanalyzer(team)
                
            else:
                print("Team has not been chosen.")
        except NameError:
            print("Team has not been chosen.")

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).
