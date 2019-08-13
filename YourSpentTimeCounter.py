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
        print("\n")
        while True:
            date = input("What date is it today? (dd/mm/yyyy)\n")
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
            day = int(dateChecker[0])
            mounth = int(dateChecker[1])
            year = int(dateChecker[2])
            if mounth > 12 or mounth < 0:
                print("Incorrect mounth's value\n\n")
                continue
            if mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8 or mounth == 10 or mounth == 12:
                if day > 31 or day < 0:
                    print("Incorrect day's value\n\n")
                    continue
            if mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11:
                if day > 30 or day < 0:
                    print("Incorrect day's value\n\n")
                    continue
            if mounth == 2:
                if year % 4 == 0:
                    if day > 29 or day < 0:
                        print("Incorrect day's value\n\n")
                        continue
                if year % 4 == 1:
                    if day > 28 or day < 0:
                        print("Incorrect day's value\n\n")
                        continue
            break
        file = open(r"D:/YSTCounter/YSTCounter_data.txt", "a")
        file.write("-----------------------\n")
        file.write("Date: %s\n\n" %date)
        while True:
            activity = input("\n\nEnter your activity\nYou can enter 'stop' here to stop entering\n")
            if activity.lower() == "stop":
                file.close()
                break
            time = input("\n\nHow much time in hours you spent for this activity\n")
            try:
                float(time)
            except ValueError:
                print("It is not a number\n")
                continue
            file.write("%s: %s hours\n" %(activity, time))
        print("\n\nYour list was successfully edited\n\n")
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
    
