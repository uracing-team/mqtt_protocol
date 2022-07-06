
# Importing Libraries
import serial
import time
import csv

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

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

def write_read(x):
    # arduino.write(bytes(x, 'utf-8'))
    arduino.write(x.encode('utf-8'))
    time.sleep(0.75)                               # Data Frequency
    data = arduino.readline()
    # data = "Testing"
    return data

while True:
    line = arduino.readline().decode()
    if line:
        print(line)
        if "DONE" in line:
            print("Break")
            break

for row in rows:
    # num = input("Enter a number: ") # Taking input from user
    payload_1 = f"speed km/h={row[3]}"
    # payload_2 = f"gear disc={row[7]}"
    # value = write_read(payload)
    value = write_read(payload_1).decode()
    """
    print(value)
    print(type(value))
    print(type(value.decode()))
    break
    """
    hours = int(float(row[0])/3600)
    minutes = int((float(row[0])%3600)/60)
    seconds = round(float(row[0])%60, 3)
    print(f"Session Time {hours}:{minutes}:{seconds} | {payload} | {value}", end="\r")