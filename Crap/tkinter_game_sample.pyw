from tkinter import *

root = Tk()
root.title("~")

# put variables here

c = Canvas(root, width = 500, height = 500, bg = "black")
c.pack()

# put sprites here

root.update()

def main():
	pass
	# put function calls here
	root.after(60, main)

# put functions here

c.focus_set()

main()

root.mainloop() 