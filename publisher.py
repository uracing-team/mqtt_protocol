import paho.mqtt.client as mqtt

mqttBroker = "127.0.0.1"
port = 1883

def on_publish(client, userdata, result):
    print("Data published")
    pass

client = mqtt.Client("Speed_sensor")
client.on_publish = on_publish
client.connect(mqttBroker, port)
ret = client.publish("speed", "300")

