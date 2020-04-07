from tkinter import *
import os

gradient_stage = 0
gradient_colors = ['#191919', '#313131', 'gray', 'dark gray', 'light gray', 'white']
object = None
func = None

root = Tk()
root.title("Cool Game Demo Edition")

def message_1():
	global object, func, gradient_stage
	object = regrets
	func = message_1
	win_button.place(x = 600, y = 600)
	if gradient_stage < 6:
		gradient()
	else:
		gradient_stage = 0
		message_2()

def message_2():
	global object, func
	pay_button.place(x = 210, y = 300)
	object = pay_button
	func = message_2
	if gradient_stage < 6:
		gradient()

def payment():
	os.startfile('payment.pyw')
	root.destroy()


c = Canvas(root, width = 500, height = 500, bg = "black")
c.pack()

regrets = Label(text = "You have not won yet\nBuy pro edition", fg = "black", bg = "black", font = ("Times", 25))
regrets.place(x = 110, y = 130)

pay_button = Button(text = "Purchase", fg = "black", bg = "black", font = ("Times", 15), command = payment)
pay_button.place(x = 600, y = 600)

win_button = Button(text = "Press to win", fg = "white", bg = "black", activebackground = "gray", font = ("Times", 15), command = message_1)
win_button.place(x = 195, y = 220)

root.resizable(width = False, height = False)
root.update()

def gradient():
	global gradient_stage
	if object == regrets:
		regrets.config(fg = gradient_colors[gradient_stage])
	else:
		pay_button.config(bg = gradient_colors[gradient_stage])
	gradient_stage += 1
	root.after(70, func)

c.focus_set()

root.mainloop() 