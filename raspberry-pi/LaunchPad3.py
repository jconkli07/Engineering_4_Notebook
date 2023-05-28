import time
import board
import digitalio

#Creates controller for the red and green LEDs
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP11) #Setup to read the button and get the pressed value
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while not button.value: #Waits until button.value=True, which is when the button is pressed
    time.sleep(0.1)

for x in range(10,0,-1):        #Loops 10 times, with x going from 10 and ending at 1
    print(x)
    red.value=True
    time.sleep(0.5)
    red.value=False
    time.sleep(0.5)     #Turns the red LED on and off every 0.5 seconds, and prints x each second

print("Liftoff!")
green.value=True    #Once it is time for liftoff prints liftoff and turns on the green LED