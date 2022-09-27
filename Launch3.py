import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18)
ledgreen.direction = digitalio.Direction.OUTPUT 
button=digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT 
button.pull = digitalio.Pull.DOWN


for x in range(10,0,-1):
    print(x)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)

print("lifftoff")
ledgreen.value = True
time.sleep(1)
ledgreen.value = False
time.sleep(1)
button.pull = digitalio.PULL.UP
