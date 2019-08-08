import os
while True:
    print("You can create, edit, read or delete your list")
    menu = input("Also, you can exit\nWhat do you want to do?\n")
    menu = menu.lower()
    if menu == "create":
        dirChecker = os.path.exists(r"D:/YSTCounter")
        if dirChecker:
            print("You have a list already\n\n")
        else:
            os.mkdir(r"D:/YSTCounter")
            file = open(r"D:/YSTCounter/YSTCounter_data.txt", "a")
            print("Your list was created in D:/YSTCounter\n\n")
    elif menu == "delete":            
        try:
            os.remove(r"D:/YSTCounter/YSTCounter_data.txt")
            os.rmdir(r"D:/YSTCounter")
        except FileNotFoundError:
            try:
                os.rmdir(r"D:/YSTCounter")
            except FileNotFoundError:
                print("File not founded\n\n")
                continue
            else:
                print("Your list was successfully deleted\n\n")
                continue
            print("File not founded\n\n")
            continue
        except PermissionError:
                print("You must close a data file or data folder\nAlso, you can't delete an empty file\n\n")
                continue
        print("Your list was successfully deleted\n\n")
    elif menu == "exit":
        break
    elif menu == "edit":
        dirChecker = os.path.exists(r"D:/YSTCounter")
        if not dirChecker:
            print("File not founded\n\n")
            continue
        date = input("\n\nWhat date is it today?\n")
        file = open(r"D:/YSTCounter/YSTCounter_data.txt", "a")
        file.write("-----------------------\n")
        file.write("Date: %s\n\n" %date)
        while True:
            activity = input("\nEnter your activity\nYou can enter 'stop' here to stop entering\n")
            if activity.lower() == "stop":
                file.close()
                break
            time = input("\nHow much time in hours you spent for this activity\n")
            try:
                float(time)
            except ValueError:
                print("It is not a number\n")
                continue
            file.write("%s: %s hours\n" %(activity, time))
            print("")
        print("Your list was successfully edited\n\n")
        continue
    elif menu == "read":
        try:
            file = open(r"D:/YSTCounter/YSTCounter_data.txt", "r")
        except FileNotFoundError:
            print("File not founded\n\n")
            continue
        if os.path.getsize(r"D:/YSTCounter/YSTCounter_data.txt") == 0:
            print("It is empty now\n\n")
            continue
        print("")
        for line in file:
            print(line)
        file.close()
        print("-----------------------\n\n")
        continue
    else:
        print("Incorrect answer\n\n")
    
