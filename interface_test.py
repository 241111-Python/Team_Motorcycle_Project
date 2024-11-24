import sys # Importing the sys module to use sys.exit()
import time
import csv
import json
user_path = input("enter path to data file: ")

def read_file():
    #code to read file 
    while True:
        user_path = input("enter path to file (csv/json): ").strip()

        try:
            if user_path.endswith('.csv'):
                with open(user_path, 'r') as file:
                    reader = csv.DictReader(file)
                    data = [row for row in reader]
                    print(data) #Added functionality to print the data
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
    

run = True

while(run) : 
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - option 1 
                2 - option 2 
                3 - option 3 
                4 - quit ''') # Added the quit option to display.
    elif selection == "1" : 
        print("opiton 1: Read file ") # Changed option 1 to read file to test reading CSVs
        read_file()
    elif selection == "2" : 
        print("option 2")
    elif selection == "3" : 
        print(user_path)
    elif selection == '4' : 
        print("quitting")
        run = False
    else : 
        print("invalid selection")

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).