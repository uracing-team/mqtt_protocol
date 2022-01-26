import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Speed_sensor")
client.connect(mqttBroker, port=80)

while True:
    random_number = randrange(200)
    client.publish("SPEED", random_number)
    print(f"Just published {random_number} to topic SPEED")
    time.sleep(1)
