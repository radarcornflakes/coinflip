#!/usr/bin/python

from sense_hat import SenseHat, ACTION_RELEASED
from signal import pause
from time import sleep

sense = SenseHat()

def roll20(event):
	if event.action == ACTION_RELEASED:


