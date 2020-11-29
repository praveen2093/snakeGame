import curses
from random import randint

curses.initscr()
window = curses.newwin(30,70,0,0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

#Snake
Snake = [(4, 10),(4,9),(4,8)]

#Food
food = (10, 20)
window.addch(food[0], food[1], "o")

#game

score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
	window.addstr(0,2, "Score" + str(score) + " ")
	#Speed increase
	window.timeout(150 - (len(Snake)) // 5 + len(Snake) // 10 % 120)

	prev_key = key
	event = window.getch()
	key = event if event !=-1 else prev_key

	if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
		key=prev_key

	y = Snake[0][0]
	x = Snake[0][1]

	if key == curses.KEY_DOWN:
		y = y+1
	if  key == curses.KEY_UP:
		y = y-1
	if key == curses.KEY_LEFT:
		x = x-1
	if key == curses.KEY_RIGHT:
		x = x+1

	Snake.insert(0, (y, x)) 


	#create corners touch game out

	if y == 0 :break
	if y == 29 : break
	if x == 0 :break
	if x == 69 :break

	if Snake[0] in Snake[1 :] :break

	if Snake[0] == food:
		#food eat

		score = score + 1
		food = ()
		while food == ():
			food = (randint(1,28), randint(1,68))
			if food in Snake:
				food = ()

		window.addch(food[0], food[1], "o")

	else:
		last = Snake.pop()
		window.addch(last[0], last[1], ' ')

	window.addch(Snake[0][0], Snake[0][1], "@")


curses.endwin()
print(f"final score = {score}")







	

