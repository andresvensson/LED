#!/usr/bin/python

import pigpio, time

step = 1

RED_PIN = 19
GREEN_PIN = 26
BLUE_PIN = 20

bright = 255
off = 0

pi = pigpio.pi()


def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)


def red():
        setLights(RED_PIN, 255)
        setLights(GREEN_PIN, 0)
        setLights(BLUE_PIN, 0)

def green():
        setLights(RED_PIN, 0)
        setLights(GREEN_PIN, 255)
        setLights(BLUE_PIN, 0)

def blue():
        setLights(RED_PIN, 0)
        setLights(GREEN_PIN, 0)
        setLights(BLUE_PIN, 255)

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


#cycle()
time.sleep(2)

#chocolate
#colorCode(210,105,30)
#time.sleep(2)

#Blue violett
#colorCode(138,43,226)
#time.sleep(2)

#dodger blue
#colorCode(30,144,255)
#time.sleep(2)

#Cyan/aqua
#colorCode(0,255,255)
#time.sleep(2)


cycle()
time.sleep(2)


pi.stop()

__name__ == "__main__"
