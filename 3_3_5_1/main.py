from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from umqtt.robust import MQTTClient
import time

# Create your objects here.
ev3 = EV3Brick()

# Create a motor object
motor = Motor(Port.B)

# Configuration
MQTT_ClientID = 'conductor'
MQTT_Broker = '172.20.10.4'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Connect to the MQTT broker
client.connect()
time.sleep(0.5)

# Song string (CSV format)
song = "C,2,D,4,E,4"

# Split the song into notes and durations
notes = song.split(",")

# Iterate over the notes and durations
for i in range(0, len(notes), 2):
    note = notes[i]
    duration = notes[i+1]
    # Publish commands to play the note
    topic = f"Lego/Play/{note}"
    message = duration
    client.publish(topic, message)
    time.sleep(0.5)  # Adjust as needed for timing between notes

print("Conducting finished.")