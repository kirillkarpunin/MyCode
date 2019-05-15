print("***Amazing Calculator*** \n")
print('\n"?" to help\n')
while True:
    first = str(input())
    if first == "?":
        print('\n1. Enter "start" to start. Then:')
        print('    1) Enter "+" to summation')
        print('    2) Enter "-" to subtraction')
        print('    3) Enter "/" to division')
        print('    4) Enter "*" to multiply')
        print('    5) Enter "//" to integer division')
        print('    6) Enter "%" to get remainder of division')
        print('    7) Enter "pow" to exponentiation')
        print('    8) Enter "sqrt" to get a square root')
        print('    9) Enter "stop" to stop')
        print('2. Enter "credits" to see credits')
        print('3. Enter "exit" to exit \n')
        continue
    elif first == "credits":
        print("\n" + 21 * " " + "╔══╦╗──╔╦══╦═══╦══╦╗─╔╦═══╗")
        print(21 * " " + "║╔╗║║──║║╔╗╠═╗─╠╗╔╣╚═╝║╔══╝")
        print(21 * " " + "║╚╝║╚╗╔╝║╚╝║╔╝╔╝║║║╔╗─║║╔═╗")
        print(21 * " " + "║╔╗║╔╗╔╗║╔╗╠╝╔╝─║║║║╚╗║║╚╗║")
        print(21 * " " + "║║║║║╚╝║║║║║─╚═╦╝╚╣║─║║╚═╝║")
        print(21 * " " + "╚╝╚╩╝──╚╩╝╚╩═══╩══╩╝─╚╩═══╝")
        print(21 * " " + "╔══╦══╦╗─╔══╦╗╔╦╗─╔══╦════╦══╦═══╗")
        print(21 * " " + "║╔═╣╔╗║║─║╔═╣║║║║─║╔╗╠═╗╔═╣╔╗║╔═╗║")
        print(21 * " " + "║║─║╚╝║║─║║─║║║║║─║╚╝║─║║─║║║║╚═╝║")
        print(21 * " " + "║║─║╔╗║║─║║─║║║║║─║╔╗║─║║─║║║║╔╗╔╝")
        print(21 * " " + "║╚═╣║║║╚═╣╚═╣╚╝║╚═╣║║║─║║─║╚╝║║║║")
        print(21 * " " + "╚══╩╝╚╩══╩══╩══╩══╩╝╚╝─╚╝─╚══╩╝╚╝ \n")
        print(25*" " + "by Capodastro Corp., 2019 \n")
        continue
    elif first == "exit":
        print("\nHave a nice day!")
        break
    elif first == "start":
        while True:
            a = input(" \nEnter first number \n")
            if a == "stop":
                print("\n\n***Amazing Calculator***\n")
                print('\n"?" to help\n')
                break
            try:
                float(a)
                A = True
            except ValueError:
                A = False
            if A == True:
                a = float(a)
            else:
                print(" \nIncorrect answer!\n")
                continue
            c = input("\nChoose math operation \n")
            if c == "stop":
                print("\n\n***Amazing Calculator***\n")
                print('\n"?" to help\n')
                break
            try:
                float(c)
                C = True
            except ValueError:
                C = False
            if C != True and (c == "+" or c == "-" or c == "*" or c == "/" or c == "//" or c == "%" or c == "pow" or c == "sqrt"):
                c = str(c)
            else:
                print("\nIncorrect answer!\n")
                continue
            if c == "sqrt":
                print("\nResult: %s\n" % pow(a, .5))
                continue
            b = input("\nEnter second number \n")
            if b == "stop":
                print("\n\n***Amazing Calculator***\n")
                print('\n"?" to help\n')
                break
            try:
                float(b)
                B = True
            except ValueError:
                B = False
            if B == True:
                b = float(b)
            else:
                print("\nIncorrect answer!\n")
                continue
            if b == 0 and (c == "/" or c == "//" or c == "%"):
                print("\nError! Division by zero!\n")
                continue
            if c == "+":
                print("\nResult: %s\n" % str(a+b))
                continue
            elif c == "-":
                print("\nResult: %s\n" % str(a-b))
                continue
            elif c == "*":
                print("\nResult: %s\n" % str(a*b))
                continue
            elif c == "/":
                print("\nResult: %s\n" % str(a/b))
                continue
            elif c == "//":
                print("\nResult: %s\n" % str(a//b))
                continue
            elif c == "%":
                print("\nResult: %s\n" % str(a%b))
                continue
            elif c == "pow":
                print("\nResult: %s\n" % str(a**b))
                continue
    else:
        print("\nIncorrent answer! \n")
        continue
