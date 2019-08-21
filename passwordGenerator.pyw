import random
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

password = []
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dirChecker = os.path.exists(r"D:/PG")
if not dirChecker:
    os.mkdir(r"D:/PG")
    file = open(r"D:/PG/data.txt", "a")
    file.close()
    dirChecker = True


def generating():
    global password
    password = []
    for i in range(8):
        symbol = random.randint(1, 2)
        if symbol == 1:
             a = random.randint(0, 9)
             password.append(nums[a])
        elif symbol == 2:
            letterCase = random.randint(1,2)
            if letterCase == 1:
                a = random.randint(0, 25)
                password.append(letters[a])
            elif letterCase == 2:
                a = random.randint(0, 25)
                password.append(letters[a].lower())
    password = "".join(password)
    passwordString.configure(state = "normal")
    passwordString.delete(0, END)
    passwordString.insert(0, password)

def reset():
    message = messagebox.askyesno("Reset the list", "Are you sure?")
    if message:
        os.remove(r"D:/PG/data.txt")
        os.rmdir(r"D:/PG")
        os.mkdir(r"D:/PG")
        file = open(r"D:/PG/data.txt", "a")
        file.close()
        passwordsList.configure(state = "normal")
        passwordsList.delete(1.0, END)
        passwordsList.configure(state = "disabled")
        resetButton.grid_remove()
        deleteButton.grid_remove()

def delete():
    message = messagebox.askyesno("Delete the list", "Are you sure?")
    if message:
        os.remove(r"D:/PG/data.txt")
        os.rmdir(r"D:/PG")
        passwordsList.configure(state = "normal")
        passwordsList.delete(1.0, END)
        passwordsList.insert(INSERT, "List is deleted.\nRestart this program if you want\nto create a list")
        passwordsList.configure(state = "disabled")
        resetButton.grid_remove()
        deleteButton.grid_remove()

def save():
    if dirChecker == False:
        os.mkdir(r"D:/PG")
    if savePassword.get() != "" and passwordDestination.get() != "":
        file = open(r"D:/PG/data.txt", "a")
        file.write(savePassword.get() + " | " + passwordDestination.get() + "\n")
        file.close()
        file = open(r"D:/PG/data.txt", "r")
        passwordsList.configure(state = "normal")
        passwordsList.delete(1.0, END)
        for line in file:
            passwordsList.insert(INSERT, line)
        passwordsList.yview(END)
        passwordsList.configure(state = "disabled")
        file.close()
        savePassword.delete(0, END)
        passwordDestination.delete(0, END)
        resetButton.grid()
        deleteButton.grid()

def exit():
    window.destroy()

window = Tk()
window.title("PassGen")
window.geometry("420x500")

tab_control = ttk.Notebook(window)

generatorTab = ttk.Frame(tab_control)
tab_control.add(generatorTab, text = "Generator")

tab_control.pack(expand = 1, fill  = 'both')

name = Label(generatorTab, text = "Password Generator", font = ("Times", 35))
name.grid(column = 0, row = 0, padx = 15, pady = 10)

generateButton = Button(generatorTab, text = "Generate", font = "Times", command = generating)
generateButton.grid(column = 0, row = 1)

passwordString = Entry(generatorTab, font = "Times", width = 10, justify = "center")
passwordString.grid(column = 0, row = 2, pady = 30)
passwordString.configure(state = "disabled")

exitButton = Button(generatorTab, text = "Exit", font = "Times", command = exit)
exitButton.grid(column = 0, row = 3)

saverTab = ttk.Frame(tab_control)
tab_control.add(saverTab, text = "Saver")

passwordLabel = Label(saverTab, text = "Enter a password", font = "Times")
passwordLabel.grid(column = 0, row = 0)

passwordText = StringVar()

savePassword = Entry(saverTab, textvariable = passwordText, width = 15)
savePassword.grid(column = 0, pady = 10, row = 1)

submitButton = Button(saverTab, text = "Submit", font = "Times", command = save)
submitButton.grid(column = 1, row = 2)

destinationLabel = Label(saverTab, text = "Enter a destination of this password", font = "Times")
destinationLabel.grid(column = 0, row = 3)

destinationText = StringVar()

passwordDestination = Entry(saverTab, textvariable = destinationText, width = 30)
passwordDestination.grid(column = 0, pady = 10, row = 4)

passwordsList = scrolledtext.ScrolledText(saverTab, width = 40, height = 10)
passwordsList.grid(column = 0, row = 6, pady = 10)
passwordsList.configure(state = "disabled")

resetButton = Button(saverTab, text = "Reset the list", font = "Times", fg = "red", command = reset)
resetButton.grid(row = 7, sticky = "W", pady = 20)
resetButton.grid_remove()

deleteButton = Button(saverTab, text = "Delete the list", font = "Times", fg = "red", command = delete)
deleteButton.grid(row = 8, sticky = "W")
deleteButton.grid_remove()

if os.path.getsize(r"D:/PG/data.txt") != 0:
    file = open(r"D:/PG/data.txt", "r")
    passwordsList.configure(state = "normal")
    for line in file:
        passwordsList.insert(INSERT, line)
    passwordsList.configure(state = "disabled")
    file.close()
    resetButton.grid()
    deleteButton.grid()

iconChecker = os.path.exists(r"C:/PasswordGeneratorIcon/64.ico")
if iconChecker: 
	window.iconbitmap(r"C:/PasswordGeneratorIcon/64.ico")
window.mainloop()
