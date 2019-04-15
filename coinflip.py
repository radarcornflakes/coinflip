#!/usr/bin/python
# This is me learning how to program in Python.
# This will select 0 or 1 at random and display the result on the
# SenseHat 8x8 pixel matrix.

from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

#define the coinflip function
def coinflip():
	flip  = random.randint(0, 1)
	if (flip == 0):
		sense.set_pixels(heads)
		print("Heads!")
	else:
		sense.set_pixels(tails)
		print("Tails!")

W = [255,255,255] #white
U = [0,0,255] #blue
R = [255,0,0] #red

heads = [
U, U, U, U, U, U, U, U,
U, U, W, U, U, W, U, U,
U, U, W, U, U, W, U, U,
U, U, W, U, U, W, U, U,
U, U, U, U, U, U, U, U,
U, W, U, U, U, U, W, U,
U, U, W, W, W, W, U, U,
U, U, U, U, U, U, U, U
]

tails = [
R, R, R, R, R, R, R, R,
R, R, W, R, R, W, R, R,
R, R, W, R, R, W, R, R,
R, R, W, R, R, W, R, R,
R, R, R, R, R, R, R, R,
R, R, W, W, W, W, R, R,
R, W, R, R, R, R, W, R,
R, R, R, R, R, R, R, R
]

coinflip()
sleep(3)
sense.clear()
