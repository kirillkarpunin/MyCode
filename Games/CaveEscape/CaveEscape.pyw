from tkinter import *
import random

WIDTH = 400
HEIGHT = 500

FALL = False
INTRO = True
OUTRO = False

PLAYER_SPEED_HOR = 0
PLAYER_SPEED_VERT = 0
PLAYER_SPEED = 5

SCORE = 0
PRESCORE = 0
secret = 1

positions = []

for a in range(4):
	STONES_X = random.randint(0,360)
	positions.append(STONES_X)

LOG_1_SPEED = 5
LOG_2_SPEED = 7 
LOG_3_SPEED = 9

LOG_1_POSITION = -150
LOG_2_POSITION = -150
LOG_3_POSITION = -150

LOG_1_SPAWN = 150
LOG_2_SPAWN = 150
LOG_3_SPAWN = 150

PLAYER_CENTER_Y = None
PLAYER_CENTER_X = None

if positions[0] > positions[1]:
	LOG_1_SPEED *= -1
	LOG_1_POSITION = 550
	LOG_1_SPAWN *= -1
if positions[1] > positions[2]:
	LOG_2_SPEED *= -1
	LOG_2_POSITION = 550
	LOG_2_SPAWN *= -1
if positions[2] > positions[3]:
	LOG_3_SPEED *= -1
	LOG_3_POSITION = 550
	LOG_3_SPAWN *= -1

root = Tk()
root.title("Cave Escape")

c = Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
c.pack()

START_LAND = c.create_rectangle(0, HEIGHT - 110, WIDTH + 10, HEIGHT+10, fill = "#702828")
FINISH_LAND = c.create_rectangle(0, 0, WIDTH + 10, 110, fill = "#702828")

LOG_1 = c.create_rectangle(LOG_1_POSITION, 310, LOG_1_POSITION + LOG_1_SPAWN, 350, fill = "#7c3f00")
LOG_2 = c.create_rectangle(LOG_2_POSITION, 230, LOG_2_POSITION + LOG_2_SPAWN, 270, fill = "#7c3f00")
LOG_3 = c.create_rectangle(LOG_3_POSITION, 150, LOG_3_POSITION + LOG_3_SPAWN, 190, fill = "#7c3f00")

STONE_1 = c.create_oval(positions[0], 350, positions[0]+40, 390, fill = "#7c3f00")
STONE_2 = c.create_oval(positions[1], 270, positions[1]+40, 310, fill = "#7c3f00")
STONE_3 = c.create_oval(positions[2], 190, positions[2]+40, 230, fill = "#7c3f00")
STONE_4 = c.create_oval(positions[3], 110, positions[3]+40, 150, fill = "#7c3f00")

PLAYER = c.create_oval(WIDTH/2 - 15, HEIGHT - 40, WIDTH/2 + 15, HEIGHT - 10, fill = "white")
TRANSITION = c.create_oval(-1000, HEIGHT+1000, 0, HEIGHT, fill = "white")


score = c.create_text(50, 20, text = "Score: %s" %SCORE, fill = "white")

root.update()

def main():
	if OUTRO:
		outro_func()
	if FALL:
		game_over()
	fall()
	win()
	logs_movement()
	logs_respawn()
	player_movement()
	root.after(30, main)

def player_movement():
	global PLAYER_SPEED
	if not FALL:
		if c.coords(PLAYER)[0] <= 0:
			c.move(PLAYER, PLAYER_SPEED, 0)
		if c.coords(PLAYER)[2] >= WIDTH:
			c.move(PLAYER, -PLAYER_SPEED, 0)
		if c.coords(PLAYER)[3] >= HEIGHT:
			c.move(PLAYER, 0, -PLAYER_SPEED)
		if c.coords(PLAYER)[1] <= 0:
			c.move(PLAYER, 0, PLAYER_SPEED)
		c.move(PLAYER, PLAYER_SPEED_HOR, PLAYER_SPEED_VERT)
		if c.coords(LOG_1)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_1)[3] and c.coords(LOG_1)[0] <= PLAYER_CENTER_X <= c.coords(LOG_1)[2]:
			c.move(PLAYER, LOG_1_SPEED, 0)
		elif c.coords(LOG_2)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_2)[3] and c.coords(LOG_2)[0] <= PLAYER_CENTER_X <= c.coords(LOG_2)[2]:
			c.move(PLAYER, LOG_2_SPEED, 0)
		elif c.coords(LOG_3)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_3)[3] and c.coords(LOG_3)[0] <= PLAYER_CENTER_X <= c.coords(LOG_3)[2]:
			c.move(PLAYER, LOG_3_SPEED, 0)

def win():
	global SCORE, PRESCORE
	if 0 < PLAYER_CENTER_Y < 55:
		PRESCORE +=1
		SCORE = PRESCORE / 7
		print(PRESCORE, SCORE)
		SCORE = int(SCORE)
		c.itemconfig(score, text = "Score: %s" %SCORE )	
		intro_func()


def fall():
	global FALL, PLAYER_CENTER_Y, PLAYER_CENTER_X
	PLAYER_CENTER_Y = (c.coords(PLAYER)[1] + c.coords(PLAYER)[3]) / 2
	PLAYER_CENTER_X = (c.coords(PLAYER)[0] + c.coords(PLAYER)[2]) / 2
	if c.coords(FINISH_LAND)[3] < PLAYER_CENTER_Y < c.coords(START_LAND)[1]:
		if c.coords(STONE_1)[1] <= PLAYER_CENTER_Y <= c.coords(STONE_1)[3] and c.coords(STONE_1)[0] <= PLAYER_CENTER_X <= c.coords(STONE_1)[2] or c.coords(STONE_2)[1] <= PLAYER_CENTER_Y <= c.coords(STONE_2)[3] and c.coords(STONE_2)[0] <= PLAYER_CENTER_X <= c.coords(STONE_2)[2] or c.coords(STONE_3)[1] <= PLAYER_CENTER_Y <= c.coords(STONE_3)[3] and c.coords(STONE_3)[0] <= PLAYER_CENTER_X <= c.coords(STONE_3)[2] or c.coords(STONE_4)[1] <= PLAYER_CENTER_Y <= c.coords(STONE_4)[3] and c.coords(STONE_4)[0] <= PLAYER_CENTER_X <= c.coords(STONE_4)[2]:
			pass
		elif c.coords(LOG_1)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_1)[3] and c.coords(LOG_1)[0] <= PLAYER_CENTER_X <= c.coords(LOG_1)[2] or c.coords(LOG_2)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_2)[3] and c.coords(LOG_2)[0] <= PLAYER_CENTER_X <= c.coords(LOG_2)[2] or c.coords(LOG_3)[1] <= PLAYER_CENTER_Y <= c.coords(LOG_3)[3] and c.coords(LOG_3)[0] <= PLAYER_CENTER_X <= c.coords(LOG_3)[2]:
			pass
		else:
			FALL = True

def game_over():
	global PLAYER_SPEED, SCORE, PRESCORE
	PRESCORE = 0
	SCORE = 0
	c.itemconfig(score, text = "Score: %s" %SCORE )	
	PLAYER_SPEED = 0
	c.coords(PLAYER, c.coords(PLAYER)[0] + 1, c.coords(PLAYER)[1] + 1, c.coords(PLAYER)[2] - 1, c.coords(PLAYER)[3] - 1)
	if c.coords(PLAYER)[2] - PLAYER_CENTER_X == 0:
		intro_func()

def intro_func():
	global INTRO, OUTRO
	if INTRO:
		c.move(TRANSITION, 100, -100)
		if (c.coords(TRANSITION)[0] + c.coords(TRANSITION)[2]) / 2 == WIDTH / 2:
			INTRO = False
			OUTRO = True
			respawn()

def outro_func():
	global INTRO, OUTRO, FALL
	c.move(TRANSITION, 100, -100)
	if c.coords(TRANSITION)[0] == WIDTH:
		OUTRO = False
		INTRO = True
		FALL = False
		c.coords(TRANSITION, -1000, HEIGHT+1000, 0, HEIGHT)

def respawn():
	global STONES_X, LOG_1_SPEED, LOG_2_SPEED, LOG_3_SPEED, LOG_1_SPAWN, LOG_2_SPAWN, LOG_3_SPAWN, LOG_1_POSITION, LOG_2_POSITION, LOG_3_POSITION, PLAYER_SPEED, FALL

	FALL = False

	c.coords(PLAYER, WIDTH/2 - 15, HEIGHT - 40, WIDTH/2 + 15, HEIGHT - 10)

	positions = []

	for a in range(4):
		STONES_X = random.randint(0,360)
		positions.append(STONES_X)

	LOG_1_SPEED = 5
	LOG_2_SPEED = 7 
	LOG_3_SPEED = 9

	LOG_1_POSITION = -150
	LOG_2_POSITION = -150
	LOG_3_POSITION = -150

	LOG_1_SPAWN = 150
	LOG_2_SPAWN = 150
	LOG_3_SPAWN = 150

	if positions[0] > positions[1]:
		LOG_1_SPEED *= -1
		LOG_1_POSITION = 550
		LOG_1_SPAWN *= -1
	if positions[1] > positions[2]:
		LOG_2_SPEED *= -1
		LOG_2_POSITION = 550
		LOG_2_SPAWN *= -1
	if positions[2] > positions[3]:
		LOG_3_SPEED *= -1
		LOG_3_POSITION = 550
		LOG_3_SPAWN *= -1

	c.coords(LOG_1, LOG_1_POSITION, 310, LOG_1_POSITION + LOG_1_SPAWN, 350)
	c.coords(LOG_2, LOG_2_POSITION, 230, LOG_2_POSITION + LOG_2_SPAWN, 270)
	c.coords(LOG_3, LOG_3_POSITION, 150, LOG_3_POSITION + LOG_3_SPAWN, 190)

	c.coords(STONE_1, positions[0], 350, positions[0]+40, 390)
	c.coords(STONE_2, positions[1], 270, positions[1]+40, 310)
	c.coords(STONE_3, positions[2], 190, positions[2]+40, 230)
	c.coords(STONE_4, positions[3], 110, positions[3]+40, 150)

	PLAYER_SPEED = 5
	
def logs_movement():
	c.move(LOG_1, LOG_1_SPEED, 0)
	c.move(LOG_2, LOG_2_SPEED, 0)
	c.move(LOG_3, LOG_3_SPEED, 0)

def logs_respawn():
	if LOG_1_SPEED > 0:
		if c.coords(LOG_1)[0] >= WIDTH:
			c.coords(LOG_1, LOG_1_POSITION, 350, LOG_1_POSITION + LOG_1_SPAWN, 310)
	else:
		if c.coords(LOG_1)[2] <= 0:
			c.coords(LOG_1, LOG_1_POSITION, 350, LOG_1_POSITION + LOG_1_SPAWN, 310)

	if LOG_2_SPEED > 0:
		if c.coords(LOG_2)[0] >= WIDTH:
			c.coords(LOG_2, LOG_2_POSITION, 230, LOG_2_POSITION + LOG_2_SPAWN, 270)
	else:
		if c.coords(LOG_2)[2] <= 0:
			c.coords(LOG_2, LOG_2_POSITION, 230, LOG_2_POSITION + LOG_2_SPAWN, 270)

	if LOG_3_SPEED > 0:
		if c.coords(LOG_3)[0] >= WIDTH:
			c.coords(LOG_3, LOG_3_POSITION, 150, LOG_3_POSITION + LOG_3_SPAWN, 190)
	else:
		if c.coords(LOG_3)[2] <= 0:
			c.coords(LOG_3, LOG_3_POSITION, 150, LOG_3_POSITION + LOG_3_SPAWN, 190)




def player_move(event):
	global PLAYER_SPEED_VERT, PLAYER_SPEED_HOR, secret, SCORE
	if event.keysym == "Left":
		PLAYER_SPEED_HOR = -PLAYER_SPEED
		if secret == 5 or secret == 7:
			secret += 1
		else:
			secret = 1
	if event.keysym == "Right":
		PLAYER_SPEED_HOR = PLAYER_SPEED
		if secret == 6 or secret == 8:
			secret += 1
		else:
			secret = 1
	if event.keysym == "Up":
		PLAYER_SPEED_VERT = -PLAYER_SPEED
		if secret == 1 or secret == 2:
			secret += 1
		else:
			secret = 1
	if event.keysym == "Down":
		PLAYER_SPEED_VERT = PLAYER_SPEED
		if secret == 3 or secret == 4:
			secret += 1
		else:
			secret = 1
	if event.keysym == "b" or event.keysym == "B":
		if secret == 9:
			secret += 1
		else:
			secret = 1
	if event.keysym == "a" or event.keysym == "A":
		if secret == 10:
			SCORE += 1000
			c.itemconfig(score, text = "Score: %s" %SCORE )	
			secret = 1
		else:
			secret = 1
	if event.keysym == "Escape":
		root.destroy()

def player_stop(event):
	global PLAYER_SPEED_HOR, PLAYER_SPEED_VERT
	if event.keysym in ("Left", "Right"):
		PLAYER_SPEED_HOR = 0
	if event.keysym in ("Up", "Down"):
		PLAYER_SPEED_VERT = 0

c.bind ("<KeyRelease>", player_stop)
c.bind ("<KeyPress>", player_move)

c.focus_set()

main()

root.iconbitmap(r"icon.ico")
root.mainloop() 

