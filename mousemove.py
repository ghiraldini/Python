# ---------------------------------------------- #
# Moves mouse every x amount of time by 1 pixel
# ---------------------------------------------- #

import sys
import win32api
import time
import ctypes

DELAY = 60

print("Press 'q' to quit")
b = True
last = time.time()
new_x = 0
new_y = 0

while(True):
	if win32api.GetAsyncKeyState(ord('Q')):
		sys.exit()
		
	current = time.time()
	tick = current - last
	last = current
	
	current = win32api.GetCursorPos()
	cx = current[0]
	cy = current[1]

	print("Mouse coords: ", cx, cy)
	
	if(b):
		new_x = cx+1
		b = False
	else:
		new_x = cx-1
		b = True
	
	new_y = cy

	win32api.SetCursorPos((int(new_x),int(new_y)))
	print("New Mouse coords: ", new_x, new_y)	
	time.sleep(DELAY)	
