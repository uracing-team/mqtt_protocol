import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, message):
    now = datetime.now()
    print(f"[{now.hour}:{now.minute}:{now.second}] Received message: {message.payload.decode()}")

topics = [
    "uracing/demo",
    "test"
]

if __name__ == "__main__":
    host = ""  # Replace this with IP address of machine
    client = mqtt.Client("HQ")
    client.connect(host=host, port=1883)
    client.subscribe("test")
    client.on_message = on_message
    client.loop_forever()
