#!/usr/bin/python

import pigpio, time
import colors
# Constants
RED_PIN = 19
GREEN_PIN = 26
BLUE_PIN = 20
bright = 255
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

def start():
        blink()
        colors.blue()

def blink():
        time.sleep(0.3)
        colors.green()
        time.sleep(0.3)
        colors.red()
        time.sleep(0.3)
        lightsOff()
        time.sleep(0.3)
        colors.red()
        time.sleep(0.3)
        lightsOff()
        time.sleep(0.3)
        colors.red()
        time.sleep(0.3)
        colors.red()
        time.sleep(1)


def main_led():
        step = 1
        while True:
                time.sleep(4)
                start()
                pi.stop
                break


if __name__ == "__main__":
        main_led()
