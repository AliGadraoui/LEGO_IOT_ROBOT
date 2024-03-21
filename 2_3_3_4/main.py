#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
color_sensor = ColorSensor(Port.S3)

# Write your program here.
while True:
    color_detected = color_sensor.color()

    if color_detected == Color.BLACK:
        # Drive forward at normal speed
        robot.drive(100, 0)  # Speed in mm/s, turn rate in deg/s
    elif color_detected == Color.BLUE:
        # Slow down when the line is blue
        robot.drive(50, 0)   # Reduced speed
    elif color_detected == Color.RED:
        # Stop on red
        robot.stop()
        break  # Exit the loop if you want the program to end on red
 
    # Add a small delay for sensor reading stability
    ev3.wait(10)
