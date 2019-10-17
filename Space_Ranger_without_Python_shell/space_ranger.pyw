from tkinter import *
import random

score = 0
iterate = 1
defeat = False

HEIGHT = 500
WIDTH = 300

SHIP_SPEED = 7
SHIP_SPEED_HOR = 0
SHIP_SPEED_VERT = 0

OBSTACLE_SPEED = 10
ASTEROID_SPEED = 10
OBSTACLE_SPEED_UP = 1.05
ASTEROID_SPEED_UP = 1.1
OBSTACLE_MAX_SPEED = 20
ASTEROID_MAX_SPEED = 20

WIDTH_CENTER = WIDTH / 2

STAR_X = random.randint(10, 290)
ASTEROID_X = random.randint(-20, 240)
OBSTACLE_X = random.randint(-25, 275)

root = Tk()
root.title("Space Ranger")

c = Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
c.pack()

ASTEROID = c.create_oval(ASTEROID_X, - 80, ASTEROID_X + 80, 0, fill = "#261717")
STAR = c.create_line(STAR_X, -30, STAR_X, 0, fill = "grey")
OBSTACLE = c.create_oval(OBSTACLE_X, - 50, OBSTACLE_X + 50, 0, fill = "#702828")
SHIP = c.create_polygon(WIDTH_CENTER - 15, HEIGHT - 10,
					    WIDTH_CENTER, HEIGHT - 40,
					    WIDTH_CENTER + 15, HEIGHT - 10,
					    fill = "white")
SCORE = c.create_text(WIDTH - WIDTH/5, 10, text = "Score: %s" %score, fill = "white")
root.update()

def main():
	rules()	
	score_update()
	try_defeat()
	obstacle()
	astroid()
	stars()
	ship_movement()
	root.after(30, main)

def rules():
	global STAR_SPEED, ASTEROID_SPEED
	if iterate == 1:
		STAR_SPEED = 0
		ASTEROID_SPEED = 0
		c.create_text(WIDTH/4 -10, HEIGHT - 25, text = "Use arrows to move\n'Esc' to close the game\nAwoid asteroids!", fill = "white", tag = "rules")
		root.after(7000, unrules)

def unrules():
	global STAR_SPEED, ASTEROID_SPEED, iterate
	c.delete("rules")
	iterate += 1
	STAR_SPEED = 50
	ASTEROID_SPEED = 10

def score_update():
	c.itemconfig(SCORE, text = "Score: %s" %score)	

def ship_movement():
	if c.coords(SHIP)[0] <= 0:
		c.move(SHIP, 7, 0)
	if c.coords(SHIP)[4] >= WIDTH:
		c.move(SHIP, -7, 0)
	if c.coords(SHIP)[1] >= HEIGHT:
		c.move(SHIP, 0, -7)
	if c.coords(SHIP)[3] <= 0:
		c.move(SHIP, 0, 7)
	if not defeat:
		c.move(SHIP, SHIP_SPEED_HOR, SHIP_SPEED_VERT)
	else:
		pass

def stars():
	global STAR_X
	if c.coords(STAR)[1] > HEIGHT: 
		STAR_X = random.randint(10, 290)
		c.coords(STAR, STAR_X, 0, STAR_X, 30)
	else:
		if not defeat and iterate != 1:
			STAR_SPEED = 50
		else:
			STAR_SPEED = 0
		c.move(STAR, 0, STAR_SPEED)

def astroid():
	global ASTEROID_X, ASTEROID_SPEED
	if c.coords(ASTEROID)[1] > HEIGHT:
		if ASTEROID_SPEED * ASTEROID_SPEED_UP < ASTEROID_MAX_SPEED:
			ASTEROID_SPEED = ASTEROID_SPEED * ASTEROID_SPEED_UP
		else:
			pass
		ASTEROID_X = random.randint(-20, 240)
		c.coords(ASTEROID, ASTEROID_X, - 80, ASTEROID_X + 80, 0)
	else:
		if not defeat and iterate != 1:
			c.move(ASTEROID, 0, ASTEROID_SPEED)
		else:
			pass

def obstacle():
	global OBSTACLE_X, OBSTACLE_SPEED, score
	if c.coords(OBSTACLE)[1] > HEIGHT:
		score += 1
		if OBSTACLE_SPEED * OBSTACLE_SPEED_UP < OBSTACLE_MAX_SPEED:
			OBSTACLE_SPEED = OBSTACLE_SPEED * OBSTACLE_SPEED_UP
		else:
			pass
		OBSTACLE_X = random.randint(-25, 275)
		c.coords(OBSTACLE, OBSTACLE_X, - 50, OBSTACLE_X + 50, 0)
	else:
		if not defeat and iterate != 1:
			c.move(OBSTACLE, 0, OBSTACLE_SPEED)
		else:
			pass

def try_defeat():
	global defeat
	if (c.coords(OBSTACLE)[1] <= c.coords(SHIP)[3] <= c.coords(OBSTACLE)[3] and c.coords(OBSTACLE)[0] <= c.coords(SHIP)[2] <= c.coords(OBSTACLE)[2]) or (c.coords(ASTEROID)[1] <= c.coords(SHIP)[3] <= c.coords(ASTEROID)[3] and c.coords(ASTEROID)[0] <= c.coords(SHIP)[2] <= c.coords(ASTEROID)[2]):
		c.create_text(WIDTH/2, HEIGHT/7, text = "You crashed\nPress 'Space' to restart", fill = "white", tag = "loser")
		defeat = True

def restart():
	global STAR_X, OBSTACLE_X, ASTEROID_X, defeat, OBSTACLE_SPEED, ASTEROID_SPEED, score
	c.delete("loser")
	score = 0
	STAR_X = random.randint(10, 290)
	ASTEROID_X = random.randint(-20, 240)
	OBSTACLE_X = random.randint(-25, 275)
	c.coords(STAR, STAR_X, 0, STAR_X, 30)
	c.coords(ASTEROID, ASTEROID_X, - 80, ASTEROID_X + 80, 0)
	c.coords(OBSTACLE, OBSTACLE_X, - 50, OBSTACLE_X + 50, 0)
	ASTEROID_SPEED = 10
	OBSTACLE_SPEED = 10
	defeat = False

def move_ship(event):
	global SHIP_SPEED_HOR, SHIP_SPEED_VERT
	if event.keysym == "Left":
		SHIP_SPEED_HOR = -SHIP_SPEED
	elif event.keysym == "Right":
		SHIP_SPEED_HOR = SHIP_SPEED
	elif event.keysym == "Up":
		SHIP_SPEED_VERT = -SHIP_SPEED
	elif event.keysym == "Down":
		SHIP_SPEED_VERT = SHIP_SPEED
	elif event.keysym == "Escape":
		root.destroy()

def stop_ship(event):
	global SHIP_SPEED_HOR, SHIP_SPEED_VERT
	if event.keysym in ("Left", "Right"):
		SHIP_SPEED_HOR = 0
	elif event.keysym in ("Up", "Down"):
		SHIP_SPEED_VERT = 0
	elif event.keysym == "space" and defeat:
		restart()

c.bind ("<KeyRelease>", stop_ship)
c.bind ("<KeyPress>", move_ship)

c.focus_set()

main()

root.mainloop()
