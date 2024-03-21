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

while True:
    buttons = ev3.buttons.pressed()
    if buttons == [Button.CENTER]:
        ev3.speaker.beep(frequency=523.25)
    elif buttons == [Button.UP]:
        ev3.speaker.beep(frequency=293.665)
    elif buttons == [Button.DOWN]:
        ev3.speaker.beep(frequency=329.628)
    elif buttons == [Button.LEFT]:
        ev3.speaker.beep(frequency=400)
    elif buttons == [Button.RIGHT]:
        ev3.speaker.beep(frequency=600)

          






    


    
