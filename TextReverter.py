while True:
    reversed_string = []
    string = input("Enter a string\n").split()
    lenght = len(string)
    while lenght > 0:
        lenght -= 1
        reversed_string.append(string[lenght])
    reversed_string = " ".join(reversed_string)
    print(reversed_string)
    answer = str(input("\nDo u wanna stop? (y/n)\n"))
    if answer == "n":
        continue
        print(" \n\n")
    elif answer == "y":
        break
    
