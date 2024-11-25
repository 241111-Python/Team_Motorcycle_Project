"""
this is a program to create your own pokemon team and analyze it's strength! 
additional sources: 
https://betterdatascience.com/radar-charts-matplotlib-plotly/

"""

import sys # Importing the sys module to use sys.exit()
import time
import csv
import json
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse


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

    
    data = read_file(user_path)
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List All Pokemons
                2 - List Individual Pokemon
                3 - Choose Six Pokemon Team 
                4 - Choose Random Pokemon Team
                5 - show current team 
                6 - show team analysis
                7 - save team to poketeams.csv
                8 - quit ''') # Added the quit option to display.
        
    elif selection == "1" : 
        # list all pokemon 
        if data:
            for pokemon in data : 
                print(pokemon['name'])

    elif selection == "2" :
        # show pokemon stats by search 
        if data:
            name = input("Enter Pokemon's name: ")
            individual_entry(data, name)

    elif selection == "3" : 
        # choose pokemon team by name 
        if data:
                team = pokemon_team(data)
                print("\nYour Chosen Pokemon Team:")
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        else:
            print("Data Unavailable")

    elif selection == "4" : 
        # random pokemon team n
        if data:
                team = random_team(data)
                print("\nYour Random Team:")
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        else:
            print("Data Unavailable")

    elif selection == "5" :
        # show current team 
        try:
            if team:
                for i, pokemon in enumerate(team,1):
                    print(f"{i}. {pokemon['name']}")
        except(NameError):
            print("Team has not been chosen ")

    elif selection == "6" : 
        # team analysis with chart 
        try:
            if team: 
                averages = team_statanalyzer(team)
            else:
                print("Team has not been chosen.")
        except NameError:
            print("Team has not been chosen.")
            
    elif selection == "7" : 
        # save current team to csv file 
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


    elif selection == '8' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).