import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

#Sets up LEDS, the button, and the servo
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
pwm_servo = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
launchTower = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

launchTower.angle=0     #Sets the servo angle to 0 to start

while not button.value: #Waits until button.value=True, which is when the button is pressed
    time.sleep(0.1)

for x in range(10,0,-1):        #Loops 10 times, with x going from 10 and ending at 1
    print(x)
    red.value=True
    time.sleep(0.5)
    red.value=False
    time.sleep(0.5)     #Turns the red LED on and off every 0.5 seconds, and prints x each second

launchTower.angle=180   #Turns the servo 180 degrees, from 0 to 180
print("Liftoff!")
green.value=True    #Once it is time for liftoff prints liftoff and turns on the green LED