# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launch Pad 1

### Assignment Description

This assignment was the initial step to it all. I had to make a countdown from 10 seconds to liftoff (0 seconds). This countdown also had to be printed on an serial monitor. 

### Evidence 

[New CircuitPython on Raspberry Pi Pico Project - Wokwi Simulator - Google Chrome 2022-09-09 13-53-28.zip](https://github.com/Devon128/Engineering_4_Notebook/files/9550439/New.CircuitPython.on.Raspberry.Pi.Pico.Project.-.Wokwi.Simulator.-.Google.Chrome.2022-09-09.13-53-28.zip)
### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
https://wokwi.com/projects/342617914094912082
### Reflection

It wasn't really a challenge in my opinion. I did make some mistakes on this though , and i will say that one thing i needed help on was the for loop code, i didn't really understand it. But despite that i got it done!!

&nbsp;

## Launch Pad 2

### Assignment Description

This assignment was basiclly an add on to part 1, i had to get an red Led blinking every second of the countdown and make an green led turn on to signifiy liftoff.

### Evidence 



https://user-images.githubusercontent.com/71898987/198099321-d96e2e73-f573-47bf-9a85-35bbb0e763db.MOV



### Wiring



### Code
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

### Reflection

This was a not so bad assignment. Now i did have an problem with one of the leds , don't remmember which one it was but it was burnt out so i used the LED on the board instead.

&nbsp;

Launch pad 3










## Launch Pad 3

### Assignment Description

This was an add on to both Launch pad 1 and 2. I had to include an physical button that started off the countdown and still have my leds and serial monitor working.

### Evidence 






https://user-images.githubusercontent.com/71898987/198102094-b1dd18c2-1334-49de-b4a0-4b03527a85e9.MOV





### Wiring


### Code

mport time
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


### Reflection

It was a little harder than the other 2 because i never used a button so i had to learn how to wire it up and i also had to find the code for it.
