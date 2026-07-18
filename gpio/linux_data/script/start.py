import gpiozero.pins.lgpio
import lgpio, os, re

def __patched_init(self, chip=0):
    gpiozero.pins.lgpio.LGPIOFactory.__bases__[0].__init__(self)
    chip_path = os.environ.get("GPIOCHIP", "")
    match = re.search(r"(\d+)$", chip_path)
    if match:
        chip = int(match.group(1))
    
    self._handle = lgpio.gpiochip_open(chip)
    self._chip = chip
    self.pin_class = gpiozero.pins.lgpio.LGPIOPin

gpiozero.pins.lgpio.LGPIOFactory.__init__ = __patched_init

import gpiozero
from time import sleep

if __name__ == "__main__":
    led_pin = gpiozero.DigitalOutputDevice(pin=18)
    led_pin.value = 0
    while True:
        led_pin.value = 1 - led_pin.value
        sleep(1)