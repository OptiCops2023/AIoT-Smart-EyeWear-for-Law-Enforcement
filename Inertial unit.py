import FaBo9Axis_MPU9255
import time
import sys

mpu9250 = FaBo9Axis_MPU9255.MPU9255()

try:
    while True:
        accel = mpu9255.readAccel()
        print " ax = " , ( accel['x'] )
        print " ay = " , ( accel['y'] )
        print " az = " , ( accel['z'] )

        gyro = mpu9255.readGyro()
        print " gx = " , ( gyro['x'] )
        print " gy = " , ( gyro['y'] )
        print " gz = " , ( gyro['z'] )

        mag = mpu9255.readMagnet()
        print " mx = " , ( mag['x'] )
        print " my = " , ( mag['y'] )
        print " mz = " , ( mag['z'] )
        print

        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()
