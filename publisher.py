# paho-mqtt doesn't work for linux
from time import sleep
import paho.mqtt.client as mqtt
import sys

client = mqtt.Client()

ip = "191.125.6.109"  # Felipe
localhost = "localhost"

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

# client.publish("bedroom/temperature", "bedroom_temperature celsius=15", 0)
# client.publish("uracing/car", "speed km/h=250", 0)

for i in range(0, 300, 5):
    client.publish("uracing/car", f"speed km/h={i}", 0)
    sleep(0.5)

client.disconnect
