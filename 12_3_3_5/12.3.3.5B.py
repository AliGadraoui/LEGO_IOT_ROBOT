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

robot=DriveBase(left_motor,right_motor,wheel_diameter=54,axle_track=105)
CSensor=ColorSensor(Port.S3)
time_end = time.time() + 5
count = 0
blue_line = red_line = black_line = 0

while time.time() < time_end:
    color = CSensor.color()
    robot.drive(50, 0)
    if color == Color.BLACK:
        black_line += 1
        ev3.speaker.beep(frequency=523.25)
    elif color == Color.RED:
        red_line += 1
        ev3.speaker.beep(frequency=293.665)
    elif color == Color.BLUE:
        blue_line += 1
        ev3.speaker.beep(frequency=329.628)
    time.sleep(0.175)
robot.stop()
ev3.screen.print(red_line)
ev3.screen.print(blue_line)
ev3.screen.print(black_line)
    

    


    
