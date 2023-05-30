import time
import board
import adafruit_mpu6050

sda_pin=board.GP12
scl_pin=board.GP13
i2c = board.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(mpu.acceleration)