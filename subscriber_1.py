import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print(f"Received message: {message.payload}")


if __name__ == "__main__":
    client = mqtt.Client("HQ")
    client.connect(host="127.0.0.1", port=1883)
    client.subscribe("SPEED")
    client.on_message = on_message
    client.loop_forever()
