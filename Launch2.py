import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT 
for x in range(10,0,-1):
    print(x)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
print("lifftoff")
ledgreen = digitalio.DigitalInOut(board.GP19)
ledgreen.direction = digitalio.Direction.OUTPUT 
