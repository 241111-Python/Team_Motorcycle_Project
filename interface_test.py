import sys # Importing the sys module to use sys.exit()
import time
import csv
import json


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
    

run = True

while(run) : 
    user_path  ="./all_CSVs/mainpoke/pokemon.csv"
    data = read_file(user_path)
    
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - List all Pokemons
                2 - List Individual Pokemon
                3 - option 3 
                4 - quit ''') # Added the quit option to display.
    elif selection == "1" : 
        # list all pokemons
        if data:
            print(data) #Added functionality to print the data  
    elif selection == "2" :
        if data:
            name = input("Enter Pokemon's name: ")
            individual_entry(data, name)
    elif selection == "3" : 
        print(user_path)
    elif selection == '4' or selection == 'q' : 
        print("quitting")
        run = False
    elif selection == "5" : 
        print("opiton 1: Read file ") # Changed option 1 to read file to test reading CSVs
       
    else : 
        print("invalid selection")

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).