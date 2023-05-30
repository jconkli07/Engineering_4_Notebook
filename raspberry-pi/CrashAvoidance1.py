import time
import board
import adafruit_mpu6050
import busio

sda_pin=board.GP10
scl_pin=board.GP11
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(mpu.acceleration)
    time.sleep(0.5)