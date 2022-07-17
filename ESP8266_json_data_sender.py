
# Importing Libraries
import serial
import time
import csv
from datetime import datetime
import json


def unix_extractor(date_time):
    ms = date_time.strftime("%Y-%m-%dT%H:%M:%S:%f")
    format = datetime.strptime(ms, "%Y-%m-%dT%H:%M:%S:%f")
    return datetime.timestamp(format)


def write_json(payload, arduino, frequency_time_delta):
    json_payload = json.dumps(payload)
    arduino.write(json_payload.encode('utf-8'))
    t1 = time.time()
    while not arduino.in_waiting:
        print("Waiting for response ...", end="\r")
    t2 = time.time() - t1
    data = arduino.readline()
    return data, t2


def test(frequency_time_delta, amount_of_data_points, arduino, rows):
    payload = []
    t0 = -1
    init_time = time.time()
    send_count = 0

    for row in rows:
        if time.time() - init_time > 20:
            print("TEST DONE")
            break
        if t0 == -1:
            t0 = unix_extractor(datetime.now())
            data_point = {
                "measurement": "speed",
                "value": int(row[3]),
                "t0": str(t0)
            }
            payload.append(data_point)
        
        if len(payload) >= amount_of_data_points:
            response, waiting_time = write_json(payload, arduino, frequency_time_delta)
            response = response.decode()
            hours = int(float(row[0])/3600)
            minutes = int((float(row[0])%3600)/60)
            seconds = round(float(row[0])%60, 3)
            send_count += 1
            print(
                f"[{send_count} | {round(waiting_time, 2)}] Session Time {hours}:{minutes}:{seconds}\n\
| PAYLOAD: {payload} \n\
| RESPONSE: {response}", end="\r")
            payload = []
            t0 = -1
            
            min_frequency = frequency_time_delta

            if waiting_time < min_frequency:
                time.sleep(min_frequency - waiting_time)  # time.sleep(frequency_time_delta)
                print(f"FREQUENCY -> {min_frequency}")
            else:
                print(f"FREQUENCY -> {waiting_time}")

        else:
            data_point = {
                "measurement": "speed",
                "value": int(row[3]),
                "t0": str(t0 + (len(payload) * (frequency_time_delta / amount_of_data_points)))
            }
            payload.append(data_point)


if __name__ == "__main__":
    
    arduino = serial.Serial(port='COM3', baudrate=230400, timeout=.1)  # 115200

    if arduino.isOpen():
        arduino.close()
    arduino.open()
    arduino.isOpen()

    csv_file = "data/lap_6.csv"

    rows = []

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        measurements = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

    while True:
        line = arduino.readline().decode()
        if line:
            print(line)
            if "DONE" in line:
                print("Break")
                break

    test(frequency_time_delta=1, amount_of_data_points=16, arduino=arduino, rows=rows)
    