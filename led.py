#!/usr/bin/python

import pigpio, time
import colors
# Constants
RED_PIN = 19
GREEN_PIN = 26
BLUE_PIN = 20
bright = 255
OFF = 0
STEP = 1
pi = pigpio.pi()

# This will run @ start
def start():
        blink(7)
        fade(colors.green())
        set(colors.blue())


# Set and read pin
def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

def readLights(pin):
        value = pi.get_PWM_dutycycle(pin)
        realValue = int(value)
        return realValue

# Code
def lightsOff():
        setLights(RED_PIN, 0)
        setLights(GREEN_PIN, 0)
        setLights(BLUE_PIN, 0)

def colorCode(r, g, b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN, b)

def set(rgb):
        colorCode(rgb[0], rgb[1], rgb[2])

def fade(rgb):
        nr = rgb[0]
        ng = rgb[1]
        nb = rgb[2]

        t = 0.01

        r = readLights(RED_PIN)
        g = readLights(GREEN_PIN)
        b = readLights(BLUE_PIN)
        print (r, g, b)
        print (nr, ng, nb)

        while nr != r or ng != g or nb != b:
                if nr > r:
                        r = r + 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(RED_PIN, r)

                if nr < r:
                        r = r - 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(RED_PIN, r)

                if ng > g:
                        g = g + 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(GREEN_PIN, g)

                if ng < g:
                        g = g - 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(GREEN_PIN, g)

                if nb > b:
                        nb = b + 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(BLUE_PIN, b)

                if nb < b:
                        b = b - 1
                        time.sleep(t)
                        print (r, g, b)
                        setLights(BLUE_PIN, b)
        else:
                setLights(RED_PIN, r)
                setLights(GREEN_PIN, g)
                setLights(BLUE_PIN, b)

def blink(count):
        while count > 0:
                set(colors.red())
                time.sleep(0.1)
                lightsOff()
                time.sleep(0.1)
                count = count - 1
        else:
                set(colors.blue())
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
