#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from umqtt.robust import MQTTClient
import time

ev3 = EV3Brick()

MQTT_ClientID = 'a'
MQTT_Broker = '172.20.10.5'
MQTT_Topic_Command = 'Lego/Command'
MQTT_Topic_Sensor = 'Lego/Sensor'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

client.connect()
time.sleep(0.5)
ev3.screen.print('Controller Started')

def on_message(topic, msg):
    if topic == MQTT_Topic_Sensor.encode():
        ev3.screen.clear()
        ev3.screen.print("Distance: " + msg.decode() + " mm")

client.set_callback(on_message)
client.subscribe(MQTT_Topic_Sensor)

while True:
    if Button.CENTER in ev3.buttons.pressed():
        client.publish(MQTT_Topic_Command, 'Forward')
    elif Button.LEFT in ev3.buttons.pressed():
        client.publish(MQTT_Topic_Command, 'Left')
    elif Button.RIGHT in ev3.buttons.pressed():
        client.publish(MQTT_Topic_Command, 'Right')
    client.check_msg()
    time.sleep(0.5)
