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

def colorCode(rgb):
        setLights(RED_PIN, rgb[0])
        setLights(GREEN_PIN, rgb[0])
        setLights(BLUE_PIN, rgb[0])

def updateColor(color, step):
        color += step

def color(x):
        #colorCode = color
        #colorCode(colors.(x))

def cycle():
        lightsOff()
        time.sleep(2)
        colorCode(colors.red())
        time.sleep(2)
        colorCode(colors.green())
        time.sleep(2)
        colorCode(colors.blue())

def main_led():
        step = 1
        Run = 0
        while Run < 10:
                cycle()
                time.sleep(2)
                pi.stop()
                Run += 1

if __name__ == "__main__":
        main_led()
