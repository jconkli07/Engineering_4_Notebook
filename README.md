# Engineering 4 Notebook

---

## Table of Contents
* [Launch Pad 1](#Launch-Pad-1)
* [Launch Pad 2](#Launch-Pad-2)
* [Launch Pad 3](#Launch-Pad-3)
* [Launch Pad 4](#Launch-Pad-4)
* [Crash Avoidance 1](#Crash-Avoidance-1)
* [Crash Avoidance 2](#Crash-Avoidance-2)
* [Crash Avoidance 3](#Crash-Avoidance-3)
* [Landing Area 1](#Landing-Area-1)
* [Landing Area 2](#Landing-Area-2)
* [Morse Code 1](#Morse-Code-1)
* [Morse Code 2](#Morse-Code-2)
* [FEA Part 1-Beam Design](#FEA-Part-1-Beam-Design)
* [FEA Part 2-Simscale Workflow](#FEA-Part-2-Simscale-Workflow)
* [FEA Part 3-Iterative Design](#FEA-Part-3-Iterative-Design)
* [4.1 Ring and Spinner](#41-Ring-and-Spinner)
* [4.2 Key and Prop](#42-Key-and-Prop)
* [4.3 Assembling the Launcher](#43-Assembling-the-Launcher)
* [Media Test](#Media-Test)

---

## Launch Pad 1

### Assignment Description
The assignment was to use circuitpython to countdown from 10 to 1, and then liftoff, and print this to the serial monitor.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/f6de8241-d3c5-497c-960f-7fe7e89154d2

### Code
<details>
<summary>Code</summary>

```python
import time

#Loops 10 times, with x starting at 10 and decreasing by 1 each loop, ending the loop when x gets ot 0
for x in range(10,0,-1):
    print(x)        #Prints the currect value of x, which will result in a countdown from 10 to 1
    time.sleep(1)

print("Liftoff!")
```
</details>

### Reflection
This assignment was pretty simple, but I did learn more about loops in python. THe first number is the start, the second the end, and the third is the step size. If left unspecified the step size is 1. Using the loop correctly allowed me to use the same variable for the loop and countdown, and simply print that variable on each run of the loop.

---

## Launch Pad 2

### Assignment Description
Keep the same structure from the first part, but make a red LED blink each second of the countdown, and a green LED turn on when countdown is completed.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/12ff5ce0-c142-476a-a4ab-dcb0ff94a204

### Wiring
<img width="300" alt="LP2 Wiring" src="https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/edd0c81f-a445-438e-962f-b07b610222fe">

### Code  
<details>
<summary>Code</summary>

```python
import time
import board
import digitalio

#Creates controller for the red and green LEDs
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT

for x in range(10,0,-1):        #Loops 10 times, with x going from 10 and ending at 1
    print(x)
    red.value=True
    time.sleep(0.5)
    red.value=False
    time.sleep(0.5)     #Turns the red LED on and off every 0.5 seconds, and prints x each second

print("Liftoff!")
green.value=True    #Once it is time for liftoff prints liftoff and turns on the green LED
time.sleep(5)
```
</details>

### Reflection
This assignment took more time than the first part as I had to work with physical components as well, with the 2 LEDS. This was useful in practicing how to wire LEDs quickly. I learned that the resistors go between the leds and ground, and the side of the resistor with the most lines goes towards the led. If led wiring isn't working you should try to flip the led, as it only works in one orientation.

---

## Launch Pad 3

### Assignment Description
This is the same as Launch Pad 2, but a button is used to begin the sequence rather than it automatically beginning when the code is loaded.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/f1d3d652-6561-4b69-aca7-a8c1e4130f10

### Wiring
<img width="300" alt="LP3 Wiring" src="https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/ecc73b36-7921-4a25-b73d-14f74d8bbf6a">

### Code
<details>
<summary>Code</summary>

```python
import time
import board
import digitalio

#Creates controller for the red and green LEDs
red = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP2) #Setup to read the button and get the pressed value
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while button.value: #Waits until button.value=True, which is when the button is pressed
    time.sleep(0.1)

for x in range(10,0,-1):        #Loops 10 times, with x going from 10 and ending at 1
    print(x)
    red.value=True
    time.sleep(0.5)
    red.value=False
    time.sleep(0.5)     #Turns the red LED on and off every 0.5 seconds, and prints x each second

print("Liftoff!")
green.value=True    #Once it is time for liftoff prints liftoff and turns on the green LED
time.sleep(5)
```
</details>

### Reflection
This assignment was easier for me than the previous assignment, as I already had figured out digitalio from the previous LEDs, and the button's wiring is easier than the LEDs. I used a while loop loop with a time.sleep in it to wait for a state change. Buttons should be set to pullp up, not down.

---

## Launch Pad 4

### Assignment Description
Once again this builds off the previous assignment, using the same structure except at launch a servo is rotated 180 degrees to represent the launch tower swinging away.

### Evidence 
https://user-images.githubusercontent.com/63983735/198157804-bf16c9f3-f43b-47c4-bb21-4fcf63d7ba15.mov

### Wiring
<img width="300" alt="LP4 Wiring" src="https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/95efed5b-1c67-4311-9886-bcc253912c48">

### Code
<details>
<summary>Code</summary>

```python
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
```
</details>

### Reflection
This was my first time using a motor this year, but the implementation turned out to be rather easy. It had a relatively similar structure to a button or LED, and it required very little code to operate. I just need to remember that setting the angle to 180 degrees, for example, doesn't necesarily mean it rotates 180 degrees, it has to be set to 0 first.

---

## Crash Avoidance 1

### Assignment Description
This requires me to wire an accelerometer and then print out the x, y, and z acceleration values in real-time to the serial monitor.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/74679238-c108-4d94-8c1b-e2bf5b03563a

### Wiring
<img width="300" alt="CA1 Wiring" src="https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/ea8d6033-d2ba-4b53-a025-b839cc1de6ec">

### Code


### Reflection
This assignment wasn't too difficult for me as I have wired accelerometers before this year and generally already understood how to code them. The acceleration values are stored in a 3 value array, with the first being x, second y, and third z.

---

## Crash Avoidance 2

### Assignment Description

The objective of this assigment is to add on to Crash Avoidance 1 and make an LED turn on when it turns past 90 degrees in any direction. We also need to power this by using a LiPo battery instead of the computer.

### Evidence 
https://user-images.githubusercontent.com/63983735/198158030-ad1dd5ff-8b01-41d7-bebb-5063d7477d45.mov

### Wiring
![Crash 3](images/Crash_3_Wire.jpeg)

### Code
[This is my code](https://github.com/qragsda80/Engineering_4_Notebook/blob/main/raspberry-pi/CA2.py) 

### Reflection
This assignment was pretty simple. We added an if functions that said that if the value is less than or greater than 9 (which is around 90 degree), turn the LED on. This means I could turn the accelerometer in any direction on any axis and the LED would turn on if it gets close to 90 degrees. 

---

## Crash Avoidance 3

### Assignment Description
Wire an OLED screen that prints the angular velocity values. Keep the other parts of the assignment like the LiPo battery and the LED turning on when turned past 90 degrees in any direction.

### Evidence 
![Crash 3](images/Crash_3.gif)

### Wiring
![Crash 3](images/Crash_3_Wire.jpeg)

### Code
[This is my code](https://github.com/qragsda80/Engineering_4_Notebook/blob/main/raspberry-pi/CA3.py)

### Reflection
One challenging part of this assignment was learning how to make a splash function run over and over again and not just text on top of eachother. Have ( splash = displayio.Group()) before the code to print on the OLED screen in your while True: loop. Once You also had to change the code from acceleration to angular velocity, but that wasn't hard.

---

## Landing Area 1

### Assignment Description
The task is to make code that prompts a user for 3 coordinates, and if those coordinates are valid and make a triangle prints out the area of the triangle. If the values are not numerical or don't make a triangle it returns an error and prompts the user again until a valid input is entered.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/93487b0b-6cc4-4d1d-8d2b-382fe17188eb

### Code
<details>
<summary>Code</summary>

```python
import math

def triangleArea(x1, y1, x2, y2, x3, y3):   #Takes 6 passed values, an x and y fro each of the 3 points
  x1f = float(x1)
  x2f = float(x2)
  x3f = float(x3)
  y1f = float(y1)
  y2f = float(y2)  
  y3f = float(y3)   #Converts passed values to floats
  return abs((x1f*y2f+x2f*y3f+x3f*y1f-y1f*x2f-y2f*x3f-y3f*x1f)/2)   #Calculates and returns area from passed values

while True:     #Prompts the user again if it was not sucessful the first time
    try:    #If this is unsuccesful it will go the the except: error message
        [x1, y1] = input("Enter coordinate 1: ").split(",")
        [x2, y2] = input("Enter coordinate 2: ").split(",")
        [x3, y3] = input("Enter coordinate 3: ").split(",") #Prompts for and stores values for each cooridnate
        print(f"The area of a triangle with coordinates ({x1},{y1}), ({x2},{y2}), and ({x3},{y3}) is {triangleArea(x1, y1, x2, y2, x3, y3)}")
        #Uses the returned area to print out the coordinates and area of the triangle
    except:
        print("Try again, please enter numerical coordinates that make a triangle:")
        #Prints error message and retrys if the initial attempt is unsuccesful
```
</details>

### Reflection
This assignment was relatively difficult as it used a few new things in the code. The first one is taking the two inputs seperated by commas, which I can do with the .split(",") command. I also used Quinn's formula for calculating the area. I have used try/except in java before but not in python, but it is very useful in this case. It will attempt to run a block of code, and if that fails it will run the section under except.

---

## Landing Area 2

### Assignment Description
Building on the last assignment, use an OLED screen to print everything. Also, you have to graph the triangle on the OLED screen.

### Evidence 
https://user-images.githubusercontent.com/63983735/198158356-7bf65323-b295-4371-82c7-9e00e29244bc.mov

### Wiring
![Landing 2 Wire](images/Landing_2_Wire.jpeg)

### Code
[This is my code](https://github.com/qragsda80/Engineering_4_Notebook/blob/main/raspberry-pi/LA2.py)

### Reflection
This assignment was a lot simpler because of how I did the first assignment. I wired the OLED screen up and created axis lines for the graph. You had figure out how to make the graph correctly. I added 64 to the x-values and 32 to the y-values to make sure the points were in the right place. The 0,0 is in the corner of the OLED screen instead of the middle, so we had to change that. There was a circle function that I put on the origin and the triangle function which I used and put in the coordinate points.

---

## Morse Code 1

### Assignment Description
The objective of this assignment is to translate a few words into morse code. The code asks you for the word(s). You type it in, and the morse code is returned to you. There is a bigger amount of space in between letters and slashes in between different words.

### Evidence 
https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/b0260fff-20e4-4c21-be5e-10e7212c36e7

### Code
<details>
<summary>Code</summary>
    
```python
import time
import board
import digitalio

dictionary = {'A':'.-', 'B':'-...',     #Create morse code dictionary
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

userMessage = input("Enter message: ")      #Prompt for and store message
if not userMessage=="-q":   #Run program if quit message isn't entered
    userMessage=userMessage.upper() #translates message to upper case to allow it to be translated
    translatedMessage = ""
    for letter in userMessage:      #Cycles through each letter in the inputted message
        if letter==" ":     #If the current letter is a space add a /
            translatedMessage+="/"
        else:
            translatedMessage+=dictionary[letter]+" "   #If the current letter is a regular letter add its morse code translation
    print(translatedMessage)    #Print out final combination of translations
```
</details>

### Reflection
 We used libraries for the first time in this assignment. It wwas nice that all of the morse code language was already done for us and we would just pull it from that. One part that I struggled on was figuring out how to space out the words in with the spaces and slashes, but I firgured out I had to count a space as a character. I said that "if letter == " "", you put a slash and a space at the end of it. If there is no space, you add a space on the end of the morse code letter by saying "final = final + MORSE_CODE[letter] + ' '"

---

## Morse Code 2

### Assignment Description
This adds on to the previous assignment by making an LED blink out the actual morse code in addition to writing it. I have to code the LED to blink for the specified number of time for each symbol.

### Evidence 
https://user-images.githubusercontent.com/63983735/198158753-2468a18c-96bf-4cf5-ab43-da9e89b4351b.mov

### Wiring
<img width="300" alt="MC2 Wiring" src="https://github.com/jconkli07/Engineering_4_Notebook/assets/71349609/ade091f4-c83d-463d-9a3f-033968a4676a">

### Code
<details>
<summary>Code</summary>

```python
import time
import board
import digitalio

dictionary = {'A':'.-', 'B':'-...',     #Create morse code dictionary
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

userMessage = input("Enter message: ")      #Prompt for and store message
if not userMessage=="-q":   #Run program if quit message isn't entered
    userMessage=userMessage.upper() #translates message to upper case to allow it to be translated
    translatedMessage = ""
    for letter in userMessage:      #Cycles through each letter in the inputted message
        if letter==" ":     #If the current letter is a space add a /
            translatedMessage+="/"
        else:
            translatedMessage+=dictionary[letter]+" "   #If the current letter is a regular letter add its morse code translation
    print(translatedMessage)    #Print out final combination of translations
    for symbol in translatedMessage:    #Evaluates each symbol and makes LED blink appropiately
        if symbol==".":
            led.value=True
            time.sleep(0.25)    #Turns on LED for 1/4 second if the current symbol is a .
        elif symbol=="-":
            led.value=True
            time.sleep(0.75)    #Turns on LED for 3/4 second if the current symbol is a -
        elif symbol==" ":
            time.sleep(0.5)    #Turns off LED for 1/2 second if it is a space between letters (1/4 sec added from end to make 3/4 total wait)
        elif symbol=="/":
            time.sleep(1.5)    #Turns off LED for 3/2 seconds if it is a space between words (1/4 sec added from end to make 7/4 total wait)
        led.value=False
        time.sleep(0.25)
        #Waits for 1/4 second, adds space between different dots/dashes for same letter
        #This also applies to spaces between letters and words, but their wait time is decreased by 1/4 second so it is the same in the end
```
</details>

### Reflection
This added a good bit of complexity over the earlier assignment as now I actually had to code in specific behaviors for each specific symbol. However, the coding methods were realtively simple and all stuff I have used before. The hardest part was figuring how to do the break between dots/dashes in the same letter effeciently, and I did this by adding a 1/4 second pause to all symbols, and reducing the wait times for the / and space by 1/4 each so they are not effected.

---

## FEA Part 1-Beam Design

### Assignment Description
This assignment is a challenge to see what team can create a beam that can hold the most weight while staying within the constraints listed. The constraints are the following: the beam must be 180mm long, the beam cannot be more than 13g, and vertical angles must be >=45 degrees. The will fail if the beam breaks or the beam bends more than 35mm down.

### Part Link 
[Link to the Beam](https://cvilleschools.onshape.com/documents/34f9b9f6b9a6d5d97f68f198/w/f04197a87a1dec7558ea7a46/e/e540280db2672cb2008c8b17?renderMode=0&uiState=641326126afe3e7e82b82a00).

### Part Image
![Hyperlink text](images/FEA1.jpg)

### Reflection
For this beam, we made walls to try to reduce the amount of displacement going down when the weight is attached. This worked pretty well, but it still reached the displacement down 35mm before it broke. When it did break, it broke at the base of the beam. This means that in the next design, we need to add material to the walls and to the base of our beam.

---

## FEA Part 2-Simscale Workflow

### Assignment Description
This assignment is a challenge to see what team can create a beam that can hold the most weight while staying within the constraints listed. The constraints are the following: the beam must be 180mm long, the beam cannot be more than 13g, and vertical angles must be >=45 degrees. The will fail if the beam breaks or the beam bends more than 35mm down.

### Part Link 
[Link to the Beam](https://cvilleschools.onshape.com/documents/34f9b9f6b9a6d5d97f68f198/w/f04197a87a1dec7558ea7a46/e/e540280db2672cb2008c8b17?renderMode=0&uiState=641326126afe3e7e82b82a00).

### Part Image
![Hyperlink text](images/FEA2.jpg)

### Reflection
When we used the Simscale, we can see that there is a lot of stress at the base of the beam. We used fillets at the base to try to add material to the point where it breaks. We took away as much material as we could from the end to reduce stress and weight and added it to the base with a draft on the walls.

---

## FEA Part 3-Iterative Design

### Assignment Description
This assignment is a challenge to see what team can create a beam that can hold the most weight while staying within the constraints listed. The constraints are the following: the beam must be 180mm long, the beam cannot be more than 13g, and vertical angles must be >=45 degrees. The will fail if the beam breaks or the beam bends more than 35mm down.

### Part Link 
[Link to the Beam](https://cvilleschools.onshape.com/documents/34f9b9f6b9a6d5d97f68f198/w/f04197a87a1dec7558ea7a46/e/e540280db2672cb2008c8b17?renderMode=0&uiState=641326126afe3e7e82b82a00). 

### Part Image
![Hyperlink text](images/FEA3R.jpg)

### Reflection
For the final beam design, we cut out triangular holes and used more fillets to reduce weight. In the redesign, we mostly focused on reducing weight on the end and adding material. We made the walls taller and thinner. It held 2.27kg before it bent past 35mm. We finished first place in our class for this assignment, so I think that it was pretty successful.

---

## 4.1 Ring and Spinner

### Assignment Description
This assignment was a refresher for onshape skills, using sketches, extrusions, relations, etc. to model a Ring and Spinner. I modeled the Ring, and used [Shrey's](https://github.com/shrey45) spinner to represent him being the Student B, with me being Student A.

### Part Link 
[Onshape Link](https://cvilleschools.onshape.com/documents/ba8472dcf4c5b8a5aa8cdf15/w/95fc89eb58180a50ec8e6108/e/1cb2083397180410db65082c?renderMode=0&uiState=6478ce94e5fcbd3ced9ffe7a)

### Part Image
![Hyperlink text](images/Ring.jpg) 
![Hyperlink text](images/Spinner.jpg) 

### Reflection
This assignment mostly used tools that I have used before, but it was a good refresher as it has been a while since I have used Onshape. This was good practice in creating and using variables, as I had not used them very much. They can be very effective at easily allowing the user to adjust many values at the same time and creates dimensions that are linked to each other. Also, extruding in two different planes and merging them into one object was good practice that took a few tries to get correct. A chamfer is like a fillet, but uses one, flat, diagonal plan to "round" the corner rather than a continuous curved plane.

---

## 4.2 Key and Prop

### Assignment Description
This worked with more advanced Onshape skills and tools to make the Key and Prop. As Student A I made the key, and used [Shrey's](https://github.com/shrey45) model for the prop.

### Part Link 
[Link to the Key and Prop](https://cvilleschools.onshape.com/documents/8616b8a375e597ac84230d17/w/24a18f8c93de24401fba89ea/e/5fe78ceeb2398b3504d84b42?renderMode=0&uiState=640f2f1e61c40226d1bda0a9).  

### Part Image
![Hyperlink text](images/Key.jpg)
![Hyperlink text](images/Prop.jpg)

### Reflection
Like the last one, this assignment used mostly tools that I already have used before, but its good to have practice with those. Offset is used to pattern features like lines and circles, but make them bigger or smaller than the original. H is the shorct for horizontal, and v is vertical. The only problem I had on this is that I accidentally offset the key 0.8 mm and not the #print_gap distance of 0.4mm, but I eventually figured this out after checking the mass. This also works with creating a mate connector within a part rather than an assembly, which I havn't worked with much before, but it was pretty similar to doing it in an assembly so I was able to complete it relatively easily.

---

## 4.3 Assembling the Launcher

### Assignment Description

The purpose of this assignment is to refresh and relearn our skills in Onshape. The task is to create and design a ring and a spinner for a helicopter toy called a "Pull Copter." In this assignment, I was Student A and Shrey Panicker [@shrey45](https://github.com/shrey45) was Student B. I created the Ring, the Top, and the Key, while Shrey created the Spinner and the Prop.

### Part Link 
[Link to the Assembly](https://cvilleschools.onshape.com/documents/8616b8a375e597ac84230d17/w/24a18f8c93de24401fba89ea/e/5d6f1ec0c09f80c20c19635d). 

### Part Image


### Reflection


---

## Media Test
Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[test.py](https://github.com/jconkli07/Engineering4_Notebook/blob/c06f7788a58206abf1b949c0d3ae60a8d23c17ee/raspberry-pi/test.py)

### Test Image
![Lakers](https://github.com/jconkli07/Engineering_4_Notebook/blob/c06f7788a58206abf1b949c0d3ae60a8d23c17ee/images/lakers.png) 

### Test GIF
![Monkey Playing Guitar](https://github.com/jconkli07/Engineering_4_Notebook/blob/c06f7788a58206abf1b949c0d3ae60a8d23c17ee/images/monkeyGuitaring.gif)

---

[Back to Top](#Engineering-4-Notebook)
