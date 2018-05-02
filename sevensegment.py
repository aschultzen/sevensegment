import RPi.GPIO as GPIO
import time

SDI   = 11
RCLK  = 12
SRCLK = 13

# Integers
CLEAR = 0x00
ZERO = 0x3F
ONE = 0x06
TWO = 0x5B
THREE = 0x4F
FOUR = 0x66
FIVE = 0x6D #D9
SIX = 0x7D
SEVEN = 0x07
EIGHT = 0x7F
NINE = 0x6F
integers = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

# Letters
AL = 0xEF
BL = 0xFA
CL = 0x73
DL = ZERO
EL = 0xF3

# Segments
SEG_A = 0x1
SEG_B = 0x2
SEG_C = 0x4
SEG_D = 0x8
SEG_E = 0x10
SEG_F = 0x20
SEG_G = 0x40
segment = [SEG_A, SEG_B, SEG_C, SEG_D, SEG_E, SEG_F, SEG_G]

class sevensegment:
	# Tailindex is just for fun to
	# draw a "tail" during animations
	tailIndex = 0x0

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(SDI, GPIO.OUT)
		GPIO.setup(RCLK, GPIO.OUT)
		GPIO.setup(SRCLK, GPIO.OUT)
		GPIO.output(SDI, GPIO.LOW)
		GPIO.output(RCLK, GPIO.LOW)
		GPIO.output(SRCLK, GPIO.LOW)

	def __del__(self):
		GPIO.cleanup()

	def hc595_in(self, dat):
		for bit in range(0, 8):
			GPIO.output(SDI, 0x80 & (dat << bit))
			GPIO.output(SRCLK, GPIO.HIGH)
			time.sleep(0.001)
			GPIO.output(SRCLK, GPIO.LOW)

	def hc595_out(self):
		GPIO.output(RCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(RCLK, GPIO.LOW)

	def displayInt(self, integer):
		if(integer == -1):
			self.hc595_in(CLEAR)
			self.hc595_out()
		self.hc595_in(integers[integer])
		self.hc595_out()

        def displaySegment(self, index, tail):
               	if(index == -1):
                	self.hc595_in(CLEAR)
                	self.hc595_out()
		if(tail):
			segments = segment[index] + segment[self.tailIndex]
			self.tailIndex = index
	                self.hc595_in(segments)
		else:
			self.hc595_in(segment[index])
               	self.hc595_out()
