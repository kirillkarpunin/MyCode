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
        date = input("\n\nWhat date is it today? (dd/mm/yyyy)\n")
        dateChecker = date.split("/")
        if len(dateChecker) != 3:
            print("Incorrect date's value\n\n")
            continue
        try:
            int(dateChecker[0])
        except ValueError:
            print("Incorrect day's value\n\n")
            continue
        try:
            int(dateChecker[1])
        except ValueError:
            print("Incorrect mounth's value\n\n")
            continue
        if int(dateChecker[1]) > 12 or int(dateChecker[1]) < 0:
            print("Incorrect mounth's value\n\n")
            continue
        if int(dateChecker[1]) == 1 or int(dateChecker[1]) == 3 or int(dateChecker[1]) == 5 or int(dateChecker[1]) == 7 or int(dateChecker[1]) == 8 or int(dateChecker[1]) == 10 or int(dateChecker[1]) == 12:
            if int(dateChecker[0]) > 31 or int(dateChecker[0]) < 0:
                print("Incorrect day's value\n\n")
                continue
        if int(dateChecker[1]) == 11 or int(dateChecker[1]) == 4 or int(dateChecker[1]) == 6 or int(dateChecker[1]) == 9:
            if int(dateChecker[0]) > 30 or int(dateChecker[0]) < 0:
                print("Incorrect day's value\n\n")
                continue
        if int(dateChecker[1]) == 2:
            if (int(dateChecker[2]) % 4) == 0:
                if int(dateChecker[0]) > 29 or int(dateChecker[0]) < 0:
                    print("Incorrect day's value\n\n")
                    continue
            if (int(dateChecker[2]) % 4) == 1:
                if int(dateChecker[0]) > 28 or int(dateChecker[0]) < 0:
                    print("Incorrect day's value\n\n")
                    continue
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
    
