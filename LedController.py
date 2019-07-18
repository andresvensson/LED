#!/usr/bin/python
import pigpio
import time
from typing import Dict, Tuple

STEP: int = 1 # Remove this?


class LedController:
    BRIGHT: int = 255
    color_codes: Dict[str, Tuple[int, int, int]] = {
        "Red": (255, 0, 0),
        "Blue": (0, 255, 0),
        "Green":(0, 0, 255),
        "Chocolate": (210, 105, 30),
        "BlueViolet": (138, 43, 226),
        "DodgerBlue": (30, 144, 255),
        "CyanAqua": (0, 255, 255)    
    }

    def __init__(self, red_pin: int, green_pin: int, blue_pin: int):
        self.pi = pigpio.pi()
        self.red_pin: int = red_pin
        self.green_pin: int = green_pin
        self.blue_pin: int = blue_pin

    def set_lights(self, pin: int, brightness: int):
            realBrightness = int(brightness * (float(self.BRIGHT) / 255.0))
            self.pi.set_PWM_dutycycle(pin, realBrightness)

    def lights_off(self):
        self.set_color_code((0, 0, 0))

    def set_color_code(self, rgb: Tuple[int, int, int]):
            self.set_lights(self.red_pin, rgb[0])
            self.set_lights(self.green_pin, rgb[1])
            self.set_lights(self.blue_pin, rgb[2])
    
    @staticmethod
    def update_color(color, step: int):
        # Remove this?
        color += step

    def cycle(self):
            self.lights_off()
            for code in self.color_codes:
                self.set_color_code(self.color_codes[code])
                time.sleep(2)


if __name__ == "__main__":
    led = LedController(red_pin=19, green_pin=26, blue_pin=20)
    led.cycle()
    led.pi.stop()
