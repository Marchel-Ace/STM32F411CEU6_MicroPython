from machine import ADC, Pin
from time import sleep

adc = ADC(Pin("PA4"))          # create ADC object on ADC pin

for x in range(100):
    val = adc.read_u16()/65535
    val = val * 3.3
    print("Voltage : ", val, end='\n')
    sleep(0.5)