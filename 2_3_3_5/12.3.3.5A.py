#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
import time

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
color_sensor = ColorSensor(Port.S3)

# Initialize variables
count = 0
previously_on_white = True  # Track if the previous color was white

# Main loop
time_end = time.time() + 60  # Run for 60 seconds
while time.time() < time_end:
    current_color = color_sensor.color()
    robot.drive(200, 0)  # Adjust speed as needed

    if current_color != Color.WHITE and previously_on_white:
        # Detected a non-white color after being on white
        count += 1
        ev3.screen.clear()
        ev3.screen.print("Lines crossed:", count)
        previously_on_white = False
    elif current_color == Color.WHITE:
        previously_on_white = True

    time.sleep(0.1)  # Small delay for debounce

robot.stop()
ev3.screen.print("Final count:", count)
time.sleep(5)  # Display final count for 5 seconds
