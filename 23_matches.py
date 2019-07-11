import random 

print("------------\n 23 matches\n------------\n")
print("Enter \"?\" to get a help\n")
while True:
    menuInput = str(input().lower())
    if menuInput == "?":
        print("---------------------------------------")
        print(" 1) Enter \"play\" to start a game")
        print(" 2) Enter \"rules\" to see how to play")
        print(" 3) Enter \"exit\" to shut down a game")
        print("---------------------------------------\n\n")
    elif menuInput == "exit":
        print("Goodbye")
        break
    elif menuInput == "rules":
        print("-------------------------------------------------------")
        print(" - There are 23 matches")
        print(" - In your turn you can take one, two or three matches")
        print(" - If you take last match you will lose")
        print("-------------------------------------------------------\n\n")
    elif menuInput == "play":
        print("Choose an opponent:")
        print("    1)Computer")
        print("    2)Another player")
        matches = 23
        playerAnalyzer = 1
        takenMatches = 0
        while True:
            playMenu = str(input())
            if playMenu == "1":
                print("\n\nChoose a difficulty")
                print("    1)Easy")
                print("    2)Hard")
                while True:
                    difficultyMenu = str(input())
                    if difficultyMenu == "1":
                        playerName = str(input("\n\nEnter your name\n"))
                        while matches != 0:
                            print("\n\n------------------\n Matches left: %s\n------------------" %matches)
                            if playerAnalyzer % 2 == 1:
                                print("\nIt is %s's turn" %playerName)
                                takenMatches = input("How many matches do you want to take?\n")
                                try:
                                    int(takenMatches)
                                    check = True
                                except ValueError:
                                    check = False
                                if check:
                                    takenMatches = int(takenMatches)
                                else:
                                    print("It isn't a number")
                                    continue
                                if takenMatches < 4 and takenMatches > 0 and takenMatches <= matches:
                                    matches = matches - takenMatches
                                    if matches != 0:
                                        playerAnalyzer += 1
                                else:
                                    print("You can't take that many matches")
                                    continue
                            else:
                                print("\nIt is computer's turn")
                                while True:
                                    takenMatches = random.randint(1, 3)
                                    if takenMatches > matches:
                                        continue
                                    else:
                                        break
                                if takenMatches == 1:
                                    print("Computer takes 1 match")
                                else:
                                    print("Computer takes %s matches" %takenMatches)
                                matches = matches - takenMatches
                                if matches != 0:
                                    playerAnalyzer += 1
                        if playerAnalyzer % 2 == 0:
                            print("\n%s has won an easy computer" %playerName)
                        else:
                            print("\nComputer has won")
                        print("-------------------------------------")
                        print("\n\n\n\n------------\n 23 matches\n------------\n")
                        print("Enter \"?\" to get a help\n")
                        break        
                    elif difficultyMenu == "2":
                        playerName = str(input("\n\nEnter your name\n"))
                        while matches != 0:
                            print("\n\n------------------\n Matches left: %s\n------------------" %matches)
                            if playerAnalyzer % 2 == 0:
                                print("\nIt is %s's turn" %playerName)
                                takenMatches = input("How many matches do you want to take?\n")
                                try:
                                    int(takenMatches)
                                    check = True
                                except ValueError:
                                    check = False
                                if check:
                                    takenMatches = int(takenMatches)
                                else:
                                    print("It isn't a number")
                                    continue
                                if takenMatches < 4 and takenMatches > 0 and takenMatches <= matches:
                                    matches = matches - takenMatches
                                    if matches != 0:
                                        playerAnalyzer += 1
                                else:
                                    print("You can't take that many matches")
                                    continue
                            else:
                                print("\nIt is computer's turn")
                                if matches == 23:
                                    takenMatches = 2
                                else:
                                    takenMatches = 4 - takenMatches
                                if takenMatches == 1:
                                    print("Computer takes 1 match")
                                else:
                                    print("Computer takes %s matches" %takenMatches)
                                matches = matches - takenMatches
                                playerAnalyzer += 1
                        if playerAnalyzer % 2 == 1:
                            print("\n%s has won a hard computer" %playerName)
                        else:
                            print("\nComputer has won")
                        print("-------------------------------------")
                        print("\n\n\n\n------------\n 23 matches\n------------\n")
                        print("Enter \"?\" to get a help\n")
                        break
                    else:
                        print("Incorrect answer")
                        continue
                break
            elif playMenu == "2":
                firstPlayer = str(input("\n\nEnter a name of first player\n"))
                secondPlayer = str(input("\n\nEnter a name of second player\n"))
                while matches != 0:
                    print("\n\n------------------\n Matches left: %s\n------------------" %matches)
                    if playerAnalyzer % 2 == 1:
                        print("\nIt is %s's turn" %firstPlayer)
                    else:
                        print("\nIt is %s's turn" %secondPlayer)   
                    takenMatches = input("How many matches do you want to take?\n")
                    try:
                        int(takenMatches)
                        check = True
                    except ValueError:
                        check = False
                    if check:
                        takenMatches = int(takenMatches)
                    else:
                        print("It isn't a number")
                        continue
                    if takenMatches < 4 and takenMatches > 0 and takenMatches <= matches:
                        matches = matches - takenMatches
                        if matches != 0:
                            playerAnalyzer += 1
                    else:
                        print("You can't take that many matches")
                        continue
                if playerAnalyzer % 2 == 0:
                    print("\n%s has won" %firstPlayer)
                else:
                    print("\n%s has won" %secondPlayer)
                print("-------------------------------------")
                print("\n\n\n\n------------\n 23 matches\n------------\n")
                print("Enter \"?\" to get a help\n")
                break
            else:
                print("Incorrect answer\n\n")
                continue
    else:
        print("Incorrect answer\n\n")
        continue
