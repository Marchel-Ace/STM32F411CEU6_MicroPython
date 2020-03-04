import onewire, ds18x20
import machine
import time
#ds Pin Define
ds_pin = machine.Pin("PC14")

#Create oneWire Object
ds = ds18x20.DS18X20(onewire.OneWire(ds_pin))

#Scan for device on the bus
roms = ds.scan()
print("found Device:", roms)

for x in range(100):
    print('temperature:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds.read_temp(rom), end='\n')