import time

#Loops 10 times, with x starting at 10 and decreasing by 1 each loop, ending the loop when x gets ot 0
for x in range(10,0,-1):
    print(x)        #Prints the currect value of x, which will result in a countdown from 10 to 1
    time.sleep(1)

print("Liftoff!")