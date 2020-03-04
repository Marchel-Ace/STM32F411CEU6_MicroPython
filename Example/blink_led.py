from machine import Pin
from time import sleep

led = Pin("PC13", Pin.OUT) #PC13 by default is LED_BLUE in Board

for x in range(100):
    led.high()
    sleep(1)
    led.low()
    sleep(1)