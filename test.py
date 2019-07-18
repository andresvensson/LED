#!/usr/bin/python
import pigpio
import time
from LedController import LedController

time.sleep(2)

#loop.blue()
lc = LedController(red_pin=0, green_pin=0, blue_pin=0)
lc.lights_off()
lc.cycle()
lc.lights_off()

#time.sleep(2)
