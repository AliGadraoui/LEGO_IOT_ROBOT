from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from umqtt.robust import MQTTClient
import time

# Create your objects here.
ev3 = EV3Brick()

# Create a motor object
motor = Motor(Port.B)

#MQTT setup
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '172.20.10.4'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

#cqllbqck
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        motor.run(100) # Change motor speed based on received message
        time.sleep(1)
        motor.stop()


# Write your program here.


# Write your program here.
client.connect() 
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
ev3.speaker.beep()

while True:
    client.check_msg()