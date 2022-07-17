
import json
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=230400, timeout=.1)

if arduino.isOpen():
        arduino.close()
arduino.open()
arduino.isOpen()

def get_payload(data_points, init_value):
    payload = []
    i = 0
    while i < data_points:
        payload.append(
            {
                "measurement": "speed",
                "value": init_value + i,
                "t0": "1658069700.020328"
            }
        )
        i+=1
    return payload

t0 = time.time()

value = 200
send_count = 0

# TEST CONFIGURATION
data_points = 1
min_frequency = 1

while (time.time() - t0) < 10:
 
    payload = get_payload(data_points, value)

    json_payload = json.dumps(payload)
    arduino.write(json_payload.encode('utf-8'))
    # print(json_payload.encode('utf-8'))
    t1 = time.time()
    
    while not arduino.in_waiting:
        if time.time() - t0 > 10:
            break
        print("Waiting for response", end="\r")
    
    data = arduino.readline().decode()
    t2 = time.time() - t1
    send_count += 1
    print(f"[{send_count}] PAYLOAD: {payload} | RESPONSE: {data} | TIME WAITING: {t2}")
    
    # min_frequency = 0.5  # Minimum frequency
    
    if t2 < min_frequency:
        time.sleep(min_frequency-t2)
    value += data_points
