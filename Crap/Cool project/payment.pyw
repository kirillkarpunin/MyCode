from tkinter import *
import os

root = Tk()
root.title("~")
root.geometry('500x500')
print()
var = IntVar()

def check():
	try:
		int(number.get(1.0, END))
		int(month.get(1.0, END))
		int(year.get(1.0, END))
		int(CVC.get(1.0, END))
	except ValueError:
		fin_label.place(x = 337, y = 385)
	else:
		try:
			int(owner.get(1.0, END))
		except ValueError:
			fin_label.config(text = "Thanks", fg = "black")
			fin_label.place(x = 357, y = 385)
			root.after(1000, fin)

def fin():
		os.startfile('Cool Game Pro Edition.pyw')
		root.destroy()

name = Label(text = "Cool Game", font = ("Times", 25))
name.pack()

subtitle = Label(text = "\'Absolutely Cool Game\'", font = ("Times", 15))
subtitle.pack()

question = Label(text = "How much money would you like to donate me?", font = ("Times", 15))
question.place(x = 10, y = 150)

one = Radiobutton(text = "1$", variable = var, value = 1)
one.place(x = 40, y = 185)

ten = Radiobutton(text = "10$", variable = var, value = 2)
ten.place(x = 120, y = 185)

hungred = Radiobutton(text = "100$", variable = var, value = 3)
hungred.place(x = 210, y = 185)

thousand = Radiobutton(text = "1000$", variable = var, value = 4)
thousand.place(x = 300, y = 185)

title = Label(font = ("Times", 10))
title.place(x = 10, y = 220)

number_head = Label(text = "Card Number", font = ("Times", 10))
number = Text(bg = "gray", fg = "black", width = 23, height = 1)
date_head = Label(text = "Expiration Date", font = ("Times", 10))
month = Text(bg = "gray", fg = "black", width = 2, height = 1)
year = Text(bg = "gray", fg = "black", width = 2, height = 1)
slash = Label(text = "/", font = 25)
owner_head = Label(text = "Owner", font = ("Times", 10))
owner = Text(bg = "gray", fg = "black", width = 23, height = 1)
CVC_head = Label(text = "CVC", font = ("Times", 10))
CVC = Text(bg = "gray", fg = "black", width = 3, height = 1)
pay_button = Button(text = "Purchase", font = ("Times", 15), command = check)
fin_label = Label(text = "Invalid input", font = ("Times", 15), fg = "red")

root.resizable(width = False, height = False)
root.update()

def card_inf():
	number_head.place(x = 10, y = 280)
	number.place(x = 10, y = 300)
	date_head.place(x = 10, y = 330)
	month.place(x = 10, y = 350)
	slash.place(x = 40, y = 345)
	year.place(x = 60, y = 350)
	owner_head.place(x = 10, y = 380)
	owner.place(x = 10, y = 400)
	CVC_head.place(x = 245, y = 328)
	CVC.place(x = 245, y = 345)
	pay_button.place(x = 345, y = 330)

def main():
	if var.get() == 4:
		one.config(state = "disabled")
		ten.config(state = "disabled")
		hungred.config(state = "disabled")
		title.config(text = "Nice", fg = "black")
		card_inf()
	else:
		if var.get() in (1, 2, 3):
			title.config(text = "Error", fg = "red")
		root.after(60, main)

main()

root.mainloop() 