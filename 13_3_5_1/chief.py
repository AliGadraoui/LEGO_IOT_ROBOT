from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from umqtt.robust import MQTTClient
import time

# Create your objects here.
ev3 = EV3Brick()

# Create a motor object
motor = Motor(Port.B)

# MQTT setup
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '172.20.10.4'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# MQTT callback
def listen(topic, msg):
    if topic == MQTT_Topic_Status.encode():
        try:
            # Print the message on the EV3 screen
            ev3.screen.print(str(msg.decode()))

            # Change motor speed based on received message
            motor_speed = int(msg.decode())
            motor.run(motor_speed)

            # Add a cool animation
            for i in range(5):
                ev3.light.on(Color.GREEN)
                time.sleep(0.1)
                ev3.light.off()
                time.sleep(0.1)

            # Stop the motor after 1 second
            time.sleep(1)
            motor.stop()

        except Exception as e:
            ev3.screen.print(f"Error: {e}")


# Write your program here.

# Connect to the MQTT broker
try:
    client.connect()
except Exception as e:
    ev3.screen.print(f"Error: {e}")

# Set the MQTT callback
client.set_callback(listen)

# Subscribe to the MQTT topic
try:
    client.subscribe(MQTT_Topic_Status)
except Exception as e:
    ev3.screen.print(f"Error: {e}")

# Play a beep sound
ev3.speaker.beep()

# Main loop
while True:
    try:
        # Check for new MQTT messages
        client.check_msg()
    except Exception as e:
        ev3.screen.print(f"Error: {e}")