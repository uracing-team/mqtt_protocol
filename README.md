# mqtt_protocol

https://blog.feabhas.com/2020/02/running-the-eclipse-mosquitto-mqtt-broker-in-a-docker-container/
https://lucassardois.medium.com/handling-iot-data-with-mqtt-telegraf-influxdb-and-grafana-5a431480217

## Create Image
docker pull eclipse-mosquitto

mkdir mosquitto
mkdir mosquitto/config/ 
mkdir mosquitto/data/
mkdir mosquitto/log/

touch mosquitto/config/mosquitto.conf

## Modify mosquitto.conf to:
allow_anonymous true
listener 1883
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log

## Run cointainer
docker run -it --name mosquitto -p 1883:1883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto

## Publish
mosquitto_pub -t "Topic" -m "Message"
docker container exec mqtt_protocol_mosquitto_1 mosquitto_pub -t "bedroom/temperature" -m "bedroom_temperature celsius=20"

## Subscribe
mosquitto_sub -t "Topic"

## With docker-compose
docker-compose up
docker container exec mqtt_protocol_mosquitto_1 mosquitto_pub -t "bedroom/temperature" -m "bedroom_temperature celsius=20"