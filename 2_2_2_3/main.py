#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

for i in range(4):
    left_motor.run(300)
    right_motor.run(300)
    time.sleep(2)
    right_motor.stop()
    left_motor.run(200)
    time.sleep(2)



#left_motor.run_time(700,5000,Stop.COAST,False)
#right_motor.run_time(360,2000,Stop.COAST,False)
#time.sleep(2)
