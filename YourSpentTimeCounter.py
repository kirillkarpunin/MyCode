import os
while True:
    print("You can create, edit, read or delete your list")
    menu = input("Also, you can exit\nWhat do you want to do?\n")
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
        except PermissionError:
            print("You must close a data file or data folder\n\n")
            continue
        except FileNotFoundError:
            print("File not founded\n\n")
            continue
        print("Your list was successfully deleted\n\n")
    elif menu == "exit":
        break
    elif menu == "edit":
        date = input("\n\nWhat date is it today?\n")
        print("What time (in hours) do you spent for...")
        series = input("...for series or any else videos?\n")
        books = input("...for books?\n")
        games = input("...for games?\n")
        cleaning = input("...for home cleaning?\n")
        walk = input("...for a walk?\n")
        sleep = input("...for a sleep?\n")
        print("Your list was successfully edited\n\n")
        file = open(r"D:/YSTCounter/YSTCounter_data.txt", "a")
        file.write("Date: %s\n\n" %date)
        file.write("Series: %s hours\n" %series)
        file.write("Books: %s hours\n" %books)
        file.write("Games: %s hours\n" %games)
        file.write("Home cleaning: %s hours\n" %cleaning)
        file.write("Walk: %s hours\n" %walk)
        file.write("Sleep: %s hours\n" %sleep)
        file.write("-----------------------\n\n")
        file.close()
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
        for line in file:
            print(line)
        file.close()
        continue
    else:
        print("Incorrect answer\n\n")
    
