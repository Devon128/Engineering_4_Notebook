import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18)
ledgreen.direction = digitalio.Direction.OUTPUT 
button=digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT 
button.pull = digitalio.Pull.DOWN
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

for x in range(10,0,-1):
    print(x)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)

servo1.angle = 180
print("lifftoff")
ledgreen.value = True
time.sleep(1)
ledgreen.value = False
time.sleep(1)
