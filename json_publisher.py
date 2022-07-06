# paho-mqtt doesn't work for linux
from email import message
from pyexpat.errors import messages
from time import sleep
import paho.mqtt.client as mqtt
import sys
import csv
import json


if __name__ == "__main__":
    client = mqtt.Client()

    # IP Addresses
    felipe = "191.125.6.109"
    localhost = "localhost"
    iggy_external = "190.160.227.214"  # external ip address -> requires router port fowarding
    iggy_internal = "192.168.0.6" # internal ip address -> works when theyre in the same network
    uracing_pc_local_ip = "192.168.1.43"

    port_1 = 1883
    port_2 = 9001

    if client.connect(uracing_pc_local_ip, port_1, 60) != 0:
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    # client.publish("bedroom/temperature", "bedroom_temperature celsius=15", 0)
    # client.publish("uracing/car", "speed km/h=250", 0)

    csv_file = "data/processed_data.csv"

    rows = []

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        measurements = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

    """
    for i in range(0, 300, 5):
        client.publish("uracing/car", f"speed km/h={i}", 0)
        sleep(0.5)
    """

    payload = json.dumps(
        {
            "measurement": "speed",
            "someValue": 200
        }
    )

    for row in rows:
        hours = int(float(row[0])/3600)
        minutes = int((float(row[0])%3600)/60)
        seconds = round(float(row[0])%60, 3)
        print(f"Session Time {hours}:{minutes}:{seconds}", end="\r")
        """
        client.publish("uracing/demo", f"speed km/h={row[3]}", 0)
        client.publish("uracing/demo", f"gear disc={row[7]}", 0)
        client.publish("uracing/demo", f"enginerpm rpm={row[8]}", 0)
        client.publish("uracing/demo", f"enginetemperature celsius={row[9]}", 0)
        """
        client.publish("test", payload)
        
        sleep(5)  # dataset frequency is 0.05 seconds per data point
        break

    client.disconnect

    print("Client disconected")
