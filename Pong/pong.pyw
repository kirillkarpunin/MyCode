from tkinter import *
import random

iterate = 1

WIDTH = 700
HEIGHT = 300

PAD_W = 10
PAD_H = 100

PAD_SPEED = 10

LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

BALL_RADIUS = 20

while True:
	BALL_X_SPEED_DIRECTION_COUNTER = random.randint(-1, 1)
	if BALL_X_SPEED_DIRECTION_COUNTER != 0:
		break
# BALL_X_SPEED = 7 * BALL_X_SPEED_DIRECTION_COUNTER
# BALL_Y_SPEED = 0

BALL_SPEED_UP = 1.05
BALL_MAX_SPEED = 25

BALL_START_SPEED = 7

right_line_distance = WIDTH - PAD_W

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

root = Tk()
root.title('Pong')

C = Canvas(root, width = WIDTH, height = HEIGHT, background = "black")
C.pack()

# C.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT + 10, fill = "white")
# C.create_line(PAD_W, 0, PAD_W, HEIGHT + 10, fill = "white")

C.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT + 10, fill = "white")

LEFT_PAD = C.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width = PAD_W, fill = "grey")

RIGHT_PAD = C.create_line(WIDTH - PAD_W/2, 0, WIDTH - PAD_W/2, PAD_H, width = PAD_W, fill = "grey")

p_1_text = C.create_text(WIDTH/6, PAD_H/4, text = PLAYER_1_SCORE, font = "Arial 20", fill = "white")
p_2_text = C.create_text(WIDTH - WIDTH/6, PAD_H/4, text = PLAYER_2_SCORE, font = "Arial 20", fill = "white")

BALL = C.create_oval(WIDTH/2 - BALL_RADIUS/2,
					 HEIGHT/2 - BALL_RADIUS/2,
					 WIDTH/2 + BALL_RADIUS/2,
					 HEIGHT/2 + BALL_RADIUS/2,
					 fill = "white")

def bounce(action):
	global BALL_X_SPEED, BALL_Y_SPEED, BALL_MAX_SPEED
	if action == "strike":
		BALL_Y_SPEED = random.randrange(-10, 10)
		if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
			BALL_X_SPEED *= -BALL_SPEED_UP
		else:
			BALL_X_SPEED = -BALL_X_SPEED
	else:
		BALL_Y_SPEED = -BALL_Y_SPEED

def game_restart_st1():
	global PLAYER_1_SCORE, PLAYER_2_SCORE
	C.coords(BALL, (WIDTH/2 - BALL_RADIUS/2,
					HEIGHT/2 - BALL_RADIUS/2,
					WIDTH/2 + BALL_RADIUS/2,
					HEIGHT/2 + BALL_RADIUS/2,))
	PLAYER_1_SCORE = 0
	PLAYER_2_SCORE = 0
	C.itemconfig(p_1_text, text = PLAYER_1_SCORE)
	C.itemconfig(p_2_text, text = PLAYER_2_SCORE)
	root.after(5000, game_restart_st2)

def game_restart_st2():
	C.delete("win_message")
	ball_restart_place()

def ball_restart_speed():
	global BALL_X_SPEED
	if BALL_X_SPEED > 0:
		BALL_X_SPEED = BALL_START_SPEED
	elif BALL_X_SPEED < 0:
		BALL_X_SPEED = BALL_START_SPEED * -1

def ball_restart_place():
	global BALL_X_SPEED, BALL_Y_SPEED
	C.coords(BALL, (WIDTH/2 - BALL_RADIUS/2,
					HEIGHT/2 - BALL_RADIUS/2,
					WIDTH/2 + BALL_RADIUS/2,
					HEIGHT/2 + BALL_RADIUS/2,))
	BALL_X_SPEED /= 10000
	BALL_Y_SPEED /= 10000
	root.after(1000, ball_restart_speed)

def move_ball():
	global PLAYER_1_SCORE, PLAYER_2_SCORE, BALL_X_SPEED, BALL_Y_SPEED
	ball_left, ball_top, ball_right, ball_bot = C.coords(BALL)
	ball_center = (ball_top + ball_bot)/2
	if ball_right + BALL_X_SPEED < right_line_distance and ball_left + BALL_X_SPEED > PAD_W:
		C.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
	elif ball_right == right_line_distance or ball_left == PAD_W:
		if ball_right > WIDTH / 2:
			if C.coords(RIGHT_PAD)[1] < ball_center < C.coords(RIGHT_PAD)[3]:
				bounce("strike")
			else:
				PLAYER_1_SCORE += 1
				C.itemconfig(p_1_text, text = PLAYER_1_SCORE)
				if PLAYER_1_SCORE >= 7:
					C.create_text(WIDTH/2, HEIGHT/3, text = "Player 1 has won", font = "Arial 20", fill = "white", tag = "win_message")
					BALL_X_SPEED /= 10000
					BALL_Y_SPEED /= 10000
					game_restart_st1()
				else:
					ball_restart_place()
		else:
			if C.coords(LEFT_PAD)[1] < ball_center < C.coords(LEFT_PAD)[3]:
				bounce("strike")
			else:
				PLAYER_2_SCORE += 1
				C.itemconfig(p_2_text, text = PLAYER_2_SCORE)
				if PLAYER_2_SCORE >= 7:
					C.create_text(WIDTH/2, HEIGHT/3, text = "Player 2 has won", font = "Arial 20", fill = "white", tag = "win_message")
					BALL_X_SPEED /= 10000
					BALL_Y_SPEED /= 10000
					game_restart_st1()
				else:
					ball_restart_place()
	else:
		if ball_right > WIDTH / 2:
			C.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
		else:
			C.move(BALL, -ball_left + PAD_W, BALL_Y_SPEED)
	if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
		bounce("ricochet")

def unchecker():
	global BALL_X_SPEED
	C.delete("rules")
	BALL_X_SPEED = 7 * BALL_X_SPEED_DIRECTION_COUNTER

def checker():
	global iterate, BALL_X_SPEED, BALL_Y_SPEED
	if iterate == 1:
		C.create_text(WIDTH/5, HEIGHT-40, text = "W, S - 1st player\nPage Up, Page Down - 2nd player\nESC - quit\nYou need to score 7 points to win\nYou can't play on Russian keyboard keymap!", font = "Arial 10", fill = "white", tag = "rules")
		BALL_X_SPEED = 0
		BALL_Y_SPEED = 0
		iterate = 2
		root.after(7000, unchecker)


def pads_borders():
	PADS = {LEFT_PAD:LEFT_PAD_SPEED,
			RIGHT_PAD:RIGHT_PAD_SPEED}
	for pad in PADS:
		C.move(pad, 0, PADS[pad])
		if C.coords(pad)[1] < 0:
			C.move(pad, 0, -C.coords(pad)[1])
		elif C.coords(pad)[3] > HEIGHT:
			C.move(pad, 0, HEIGHT - C.coords(pad)[3])

def main():
	checker()
	move_ball()
	pads_borders()
	root.after(30, main)

def move_pad(event):
	global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
	if event.keysym == "w" or event.keysym == "W":
		LEFT_PAD_SPEED = -PAD_SPEED
	elif event.keysym == "s" or event.keysym == "S":
		LEFT_PAD_SPEED = PAD_SPEED
	elif event.keysym == "Up":
		RIGHT_PAD_SPEED = -PAD_SPEED
	elif event.keysym == "Down":
		RIGHT_PAD_SPEED = PAD_SPEED
	if event.keysym == "Escape":
		root.destroy()

def stop_pad(event):
	global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
	if event.keysym in ("w", "s", "W", "S"):
		LEFT_PAD_SPEED = 0
	elif event.keysym in ("Up", "Down"):
		RIGHT_PAD_SPEED = 0

C.bind ("<KeyRelease>", stop_pad)
C.bind ("<KeyPress>", move_pad)

C.focus_set()

main()

root.iconbitmap(r"icon.ico")
root.mainloop()
