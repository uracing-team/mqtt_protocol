
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

void setup() {
    Serial.begin(115200);
}

void loop() {
    if (Serial.available())
    {
        String payload = Serial.readString();
        if (payload.length() > 2)
        {
            Serial.println(payload);
        }
    }  
}
