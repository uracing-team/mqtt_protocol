import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload)}")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("HQ")
print(".", end="")
client.connect(mqttBroker, port=80)
print(".", end="")

client.loop_start()
print(".", end="")
client.subscribe("SPEED")
print(".", end="")
client.on_message = on_message
print(".", end="")
time.sleep(30)
print(".", end="")
# client.loop_end()
client.loop_stop()
