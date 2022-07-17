
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid =""; //replace this with your wifi  name
const char* password =""; //replace with your wifi password
char hostname[] =""; //replace this with IP address of machine 
//on which broker is installed
#define TOKEN "bytesofgigabytes_ESP8266_TOKEN"  // ????????????

WiFiClient wifiClient;
PubSubClient client(wifiClient);

int status = WL_IDLE_STATUS;

void setup() {
    Serial.begin(230400);  // 115200
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("Connected to WiFi");
    Serial.println("ESP8266 AS PUBLISHER");
    client.setServer(hostname, 1883 ); //default port for mqtt is 1883
    
    client.setBufferSize(2048);  // Maximum String size
}

void loop() {
    if ( !client.connected() ) {
        reconnect();
    }
    MQTTPOST();
    // delay(750);  // Publish Frequency (1000 = 1s)
}

String payload_1;

void MQTTPOST() {
    // while (payload_1.length() < 1) {
    while (payload_1.length() < 3) {
        
        if (Serial.available()) {
            payload_1 = Serial.readString();
        }
        
        if (payload_1.length() > 2) {
            
            // Deserialization
            DynamicJsonDocument doc(2048);  // String size (8->1024) (1->128,2->256)
            
            DeserializationError error = deserializeJson(doc, payload_1);

            if (error) {
                Serial.print(F("deserializeJson() failed: "));
                Serial.println(error.f_str());
                return;
            }

            for (JsonObject item: doc.as<JsonArray>()) {
                const char* measurement = item["measurement"]; // "speed"
                int value = item["value"]; // 245
                const char* t0 = item["t0"]; // "1657219492.002005"
            }
            
            // Serialize
            char JSONmessageBuffer[2048];  // String size (1024)
            serializeJson(doc, JSONmessageBuffer);
            Serial.println(JSONmessageBuffer);  // It is being received and printed

            // Publish
            client.publish("test", JSONmessageBuffer);  // It only publishes upto 4 data points
        }
        payload_1 = "";
    }
}

//this function helps you reconnect wifi as well as broker if connection gets disconnected.
void reconnect() {
    while (!client.connected()) {
        status = WiFi.status();
        if ( status != WL_CONNECTED) {
            WiFi.begin(ssid, password);
            while (WiFi.status() != WL_CONNECTED) {
                delay(500);
                Serial.print(".");
            }
            Serial.println("Connected to AP");
        }
        Serial.print("Connecting to Broker …");
        Serial.print("192.168.1.43");

        if ( client.connect("ESP8266 Device", TOKEN, NULL) ) {
            Serial.println("[DONE]" );
        }
        else {
            Serial.println( " : retrying in 5 seconds]" );
            delay( 5000 );
        }
    }
}
