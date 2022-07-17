
void setup() {
    Serial.begin(115200);
}

void loop() {
	String payload;

	if (Serial.available())  // Serial port message available.
	{
		payload = Serial.readString();  // Reads message from Serial port.
	}
	
	if (payload.length() > 2)  // Message isn't empty.
	{
		char JSONmessageBuffer[1024];  // 1024 is the maximum message size in bytes.
		serializeJSON(payload, JSONmessageBuffer);  // payload is serialized into JSONmessageBuffer.
		Serial.println(payload);  // Message received is sent through the Serial port.
		mqtt_broker.publish("topic", payload);  // Serialized message is sent to MQTT Broker.
	}
    payload = "";
}