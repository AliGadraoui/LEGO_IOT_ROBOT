#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
import time

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
color_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Define speed parameters.
normal_speed = 100  # Speed when following a black line.
reduced_speed = 50  # Reduced speed when on blue line.

while True:
    # Check the color sensor reading.
    robot.drive(100, 0) 
    color = color_sensor.color()

    if color == Color.RED:
        # Stop if the sensor sees red.
        robot.stop()
        break
    elif color == Color.BLUE:
        # Reduce speed if the sensor sees blue.
        robot.drive(reduced_speed, 0)
    elif color == Color.BLACK:
        # Continue at normal speed if the sensor sees black.
        robot.drive(normal_speed, 0)
    else:
        # Stop or take some other action if no relevant color is detected.
        robot.stop()
        break

    time.sleep(0.1)  # Small delay to prevent overloading the CPU.
