import machine
import time 

stateButton = 0

#Create Callback Function
def cbButton(pin): 
    if stateButton == 0:
        stateButton = 1
        led.high()
    else:
        stateButton = 0
        led.low()

led = machine.Pin("PC13", machine.Pin.OUT) #PC13 by default is LED_BLUE in Board

button = machine.Pin("PA0", machine.Pin.IN, machine.Pin.PULL_UP) #PA0 by Default is KEY in Board
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=cbButton) #Set Interrupts Button


state = machine.disable_irq()
machine.enable_irq(state) #Enable Interrupt

for x in range(1000):
    print(".")
    time.sleep(1)