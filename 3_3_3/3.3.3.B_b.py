#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from umqtt.robust import MQTTClient
import time

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultra_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

MQTT_ClientID = 'b'
MQTT_Broker = '172.20.10.5'
MQTT_Topic_Command = 'Lego/Command'
MQTT_Topic_Sensor = 'Lego/Sensor'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

def on_command(topic, msg):
    message = msg.decode()
    if message == 'Forward':
        robot.drive(100, 0)
        time.sleep(1)
        robot.stop()
    elif message == 'Left':
        robot.turn(-90)
    elif message == 'Right':
        robot.turn(90)

client.connect()
client.set_callback(on_command)
client.subscribe(MQTT_Topic_Command)

while True:
    distance = ultra_sensor.distance()
    client.publish(MQTT_Topic_Sensor, str(distance))
    client.check_msg()
    time.sleep(0.5)
