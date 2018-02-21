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

#r = 0
#g = 0
#b = 255


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

def set(rgb):
        colorCode(rgb[0], rgb[1], rgb[2])

def fade(rgb):
        nr = rgb[0]
        ng = rgb[1]
        nb = rgb[2]

        r = 128
        g = 129
        b = 130
        print (r, g, b)
        print (nr, ng, nb)

        while nr != r or ng != g or nb != b:
                if nr > r and ng == g and nb == b:
                        r = r + 1
                        print (r, g, b)
                        setLights(RED_PIN, r)

                elif nr < r and ng == g and nb == b:
                        r = r - 1
                        print (r, g, b)
                        setLights(RED_PIN, r)

                elif nr == r and ng > g and nb == n:
                        g = g + 1
                        print (r, g, b)
                        setLights(GREEN_PIN, g)

                elif nr == r and ng < g and nb == b:
                        g = g - 1
                        print (r, g, b)
                        setLights(GREEN_PIN, g)

                elif nr == r and ng == g and nb > n:
                        b = b + 1
                        print (r, g, b)
                        setLights(BLUE_PIN, b)

                elif nr == r and ng == g and nb < b:
                        b = b - 1
                        print (r, g, b)
                        setLights(BLUE_PIN, b)

def start():
        #blink(7)
        fade(colors.green())
        set(colors.blue())


def blink(count):
        while count > 0:
                set(colors.red())
                time.sleep(0.1)
                lightsOff()
                time.sleep(0.1)
                count = count - 1
        else:
                set(colors.green())
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
