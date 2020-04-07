from tkinter import *
import webbrowser

gradient_stage = 0
gradient_colors = ['#191919', '#313131', 'gray', 'dark gray', 'light gray', 'white']
object = None
func = None

root = Tk()
root.title("Cool Game Pro Edition")

def message_1():
	global object, func, gradient_stage
	object = congrats
	func = message_1
	win_button.place(x = 600, y = 600)
	if gradient_stage < 6:
		gradient()
	else:
		gradient_stage = 0
		message_2()

def message_2():
	global object, func, gradient_stage
	object = updates
	func = message_2
	if gradient_stage < 6:
		gradient()
	else:
		gradient_stage = 0
		message_3()

def message_3():
	global object, func
	just_button.place(x = 376, y = 475)
	object = just_button
	func = message_3
	if gradient_stage < 6:
		gradient()

def just_func():
	webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=0m43s')

c = Canvas(root, width = 500, height = 500, bg = "black")
c.pack()

congrats = Label(text = "Congratulations\nYou won", fg = "black", bg = "black", font = ("Times", 25))
congrats.place(x = 145, y = 130)

updates = Label(text = "Updates will be soon", fg = "black", bg = "black", font = ("Times", 15))
updates.place(x = 165, y = 300)

win_button = Button(text = "Press to win", fg = "white", bg = "black", activebackground = "gray", font = ("Times", 15), command = message_1)
win_button.place(x = 195, y = 220)

just_button = Button(text = "Get your money back", fg = "black", bg = "black", activebackground = "gray", font = ("Times", 10), command = just_func)

root.resizable(width = False, height = False)
root.update()

def gradient():
	global gradient_stage
	if object == just_button:
		just_button.config(bg = gradient_colors[gradient_stage])
	else:
		object.config(fg = gradient_colors[gradient_stage])
	gradient_stage += 1
	root.after(70, func)

c.focus_set()

root.mainloop() 