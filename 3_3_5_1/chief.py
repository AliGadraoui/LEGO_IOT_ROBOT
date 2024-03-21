from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from umqtt.robust import MQTTClient
import time

# Create your objects here.
ev3 = EV3Brick()

# Create a motor object
motor = Motor(Port.B)

# Musician robot configuration
note_assigned = "C"  # The note this robot is responsible for
MQTT_ClientID = f"robot_{note_assigned}"
MQTT_Broker = '172.20.10.4'
MQTT_Topic = f"Lego/Play/{note_assigned}"
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Connect to the MQTT broker and subscribe to the topic
client.connect()
client.subscribe(MQTT_Topic)
time.sleep(0.5)

def on_message(topic, msg):
    duration = int(msg.decode())
    # Play the note (simulated here with a print statement and light blink)
    ev3.speaker.beep(frequency=262, duration=duration*250)  # Example for "C" note
    ev3.light.on(Color.RED)
    time.sleep(duration*0.25)  # Adjust duration as needed
    ev3.light.off()

client.set_callback(on_message)

print(f"Robot {note_assigned} ready to play.")

# Main loop to check for messages
while True:
    client.check_msg()
    time.sleep(0.5)