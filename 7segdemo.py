import sys
import time
from sevensegment import sevensegment

display = sevensegment()

counter = -1

while(1):
	display.displayInt(1)
	counter = counter + 1
	if(counter > 9):
		counter = 0

	display.displayInt(counter)
	print("Displaying: " + str(counter) + "...") 
	time.sleep(0.2)

	animation = [0,1,2,3,4,5,0,1,6,4,3,2,6,5]
	for i in animation:
		display.displaySegment(i,2)
		time.sleep(0.05)
