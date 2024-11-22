
user_path = input("enter path to data file: ")

run = True

while(run) : 
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - option 1 
                2 - option 2 
                3 - option 3 ''')
    elif selection == "1" : 
        print("opiton 1")
    elif selection == "2" : 
        print("option 2")
    elif selection == "3" : 
        print(user_path)
    elif selection == '4' : 
        print("quitting")
        run = False
    else : 
        print("invalid selection")