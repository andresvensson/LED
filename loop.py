#!/usr/bin/python

import pigpio, time
import colors
# Constants
RED_PIN = 19
GREEN_PIN = 26
BLUE_PIN = 20
BRIGHT = 255
OFF = 0

pi = pigpio.pi()

def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)


def lightsOff():
        setLights(RED_PIN, 0)
        setLights(GREEN_PIN, 0)
        setLights(BLUE_PIN, 0)

def colorCode(r, g, b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN, b)

def updateColor(color, step):
        color += step


def cycle():
        lightsOff()
        time.sleep(2)
        red()
        time.sleep(2)
        green()
        time.sleep(2)
        blue()

def main_loop():         
        step = 1        
        while True:
                cycle()
                time.sleep(2)
        pi.stop()

if __name__ == "__main__":
        main_loop()
