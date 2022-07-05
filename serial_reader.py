
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

while True:
    line = arduino.readline().decode()
    if line:
        print(line)
