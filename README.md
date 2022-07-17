# mqtt_protocol

https://blog.feabhas.com/2020/02/running-the-eclipse-mosquitto-mqtt-broker-in-a-docker-container/
https://lucassardois.medium.com/handling-iot-data-with-mqtt-telegraf-influxdb-and-grafana-5a431480217

## Execute docker-compose
docker-compose up -d

## Exexute the following commands to enter database
docker exec -it mqtt_protocol_influxdb_1 bash
influx
use telegraf

## Publish files
- publisher.py sends data from data/processed_data.csv directly to the MQTT Broker.
- ESP8266/publisher/publisher.ino is the code to execute on the microcontroler Sparkfun Thing - Dev Board, it depends on data to be sent to it.
    - ESP8266_line_data_sender.py sends data from data/lap_6.py to the microcontroler through the USB cable, using a one line message.
    - ESP8266_json_data_sender.py sends data from data/lap_6.py to the microcontroler through the USB cable, using a json format message.

## Subscribe file
subscriber.py subscribes to all the topics on the MQTT Broker and prints out all the messages received.

## View visualizations
Enter 127.0.0.1:3000 on any browser, this is only if it's used on the computer running the docker compose file.

## Data sources
- data/processed_data.csv has usefull data to use for simulations or testing.
- data/lap_6.csv is the filtered data of the previous file, containing only values from lap 6 of the race data.

## Analysis
analysis.ipynb is a jupyter notebook file that is used to process and analysis data quickly.

## Testing
The testing folder contains files that can be modified to test diferent functionalities of the system.
