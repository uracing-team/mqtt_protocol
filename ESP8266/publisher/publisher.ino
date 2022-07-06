
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid ="Linderos"; //replace this with your wifi  name
const char* password ="moorerubio"; //replace with your wifi password
char hostname[] ="192.168.1.43"; //replace this with IP address of machine 
//on which broker is installed
#define TOKEN "bytesofgigabytes_ESP8266_TOKEN"  // ????????????

WiFiClient wifiClient;
PubSubClient client(wifiClient);

int status = WL_IDLE_STATUS;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("Connected to WiFi");
    Serial.println("ESP8266 AS PUBLISHER");
    client.setServer(hostname, 1883 ); //default port for mqtt is 1883
}

void loop() {
    if ( !client.connected() ) {
        reconnect();
    }
    MQTTPOST();
    delay(750);  // Publish Frequency (1000 = 1s)
}

String payload_1;

void MQTTPOST() {
    while (payload_1.length() < 1) {
        
        if (Serial.available()) {
            payload_1 = Serial.readString();
        }
        
        if (payload_1.length() > 0) {
            char attributes_1[1000];
            payload_1.toCharArray(attributes_1, 1000);
            client.publish("test", attributes_1);
            Serial.println(attributes_1);
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
