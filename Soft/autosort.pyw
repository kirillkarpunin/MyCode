from tkinter import *
import os

root = Tk()
root.geometry('600x750')
root.title("~")

unsorted_list = []
sorted_list = []
unsorted_dictionary = {}
sorted_dictionary = {}
biggest = 0
biggest_index = 0
line_num = 0
keys = []
key = 0
value = 0
repeat = 1
variable = 0
smth = 0
warning = "Incorrect input"

c = Canvas(root, width = 400, height = 650, bg = "black")
c.place(x = 1, y = 80)

if os.path.exists(r'data.txt'):
	file = open(r'data.txt')
	for line in file:
		c.create_text(10, 10 + 25 * line_num, text =  "• " + line.split("; ")[0], fill = "white", font = "Times 15", anchor = NW, tag = str(line_num + 1))
		line_num += 1
		keys.append(line.split("; ")[1])
		if float(line.split("; ")[1]) % 1 != 0:
			repeat += 1

def get_text():
	global line_num, key, repeat
	try:
		int(text.get(1.0, END).split("; ")[1])
	except ValueError:
		text.delete(1.0, END) 
		text.insert(1.0, warning)
	except IndexError:
		c.create_text(10, 10 + 25 * line_num, text = "• " + text.get(1.0, END), fill = "white", font = "Times 15", anchor = NW, tag = str(line_num + 1))
		line_num += 1
		key = '-1'
		if key in keys:
			key = str(int(key) + repeat / 100)
			repeat += 1
		file = open(r'data.txt', 'a')
		file.write(text.get(1.0, END).split("\n")[0] + "; " + key + "; " + str(line_num) + "\n")
		file.close()
		text.delete(1.0, END) 
		keys.append(key)
	else:
		c.create_text(10, 10 + 25 * line_num, text = "• " + text.get(1.0, END).split("; ")[0], fill = "white", font = "Times 15", anchor = NW, tag = str(line_num + 1))
		line_num += 1
		key = text.get(1.0, END).split("\n")[0].split("; ")[1]
		if key in keys:
			key = str(int(key) + repeat / 100)
			repeat += 1
		file = open(r'data.txt', 'a')
		file.write(text.get(1.0, END).split("; ")[0] + "; " + key + "; " + str(line_num) + "\n")
		file.close()
		text.delete(1.0, END) 
		keys.append(key)

def sort():
	file = open(r'data.txt')
	for line in file:
		unsorted_list.append(line.split("; ")[1])
		unsorted_dictionary[line.split("; ")[1]] = line.split("; ")[0]
	for a in range(len(unsorted_list)):
		find_biggest()
	for b in range(len(sorted_list)):
		sorted_dictionary[unsorted_dictionary[sorted_list[b]]] = str(b + 1)
	file.close()
	move()
	
def find_biggest():
	global biggest, biggest_index, variable
	biggest = int(unsorted_list[0])
	for i in range(len(unsorted_list)):
		variable = float(unsorted_list[i])
		if variable % 1 == 0:
			variable = int(variable)
		if biggest <= variable:
			biggest = variable
			biggest_index = i
	sorted_list.append(str(biggest)) 
	del unsorted_list[biggest_index]

def move():
	file = open(r'data.txt')
	for line in file:
		c.move(line.split("\n")[0].split('; ')[2], 0, (round(int(sorted_dictionary[line.split("; ")[0]])) - round(int(line.split("; ")[2]))) * 25)
	unsorted_list.clear()
	sorted_list.clear()
	unsorted_dictionary.clear()
	sorted_dictionary.clear()
	status.config(text = 'sorted')

name = Label(text = "To-do list", font = ("Times", 35))
name.pack()

status = Label(text = 'unsorted', font = ('Times', 15))
status.place(x = 20, y = 50)

direct = Label(text = "Enter your tasks here\n\"Task; priority\"", font = ("Times", 15))
direct.place(x = 415, y = 300)

text = Text(width = 23, height = 5, bg = "black", fg = 'white', wrap = WORD)
text.place(x = 407, y = 350)

add_button = Button(text = "Add task", command = get_text)
add_button.place(x = 470, y = 450)

sort_button = Button(text = "Sort list", command = sort)
sort_button.place(x = 470, y = 680)

root.update()

root.mainloop() 