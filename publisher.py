# paho-mqtt doesn't work for linux
import paho.mqtt.client as mqtt
import sys

client = mqtt.Client()

ip = "192.168.158.161"  # Felipe
localhost = "localhost"

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish("bedroom/temperature", "bedroom_temperature celsius=15", 0)

client.disconnect
