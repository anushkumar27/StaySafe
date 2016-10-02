import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
        line = ser.readline()
        print(line)
        ser.write(b'1')
        sleep(2)
        ser.write(b'2')
        sleep(2)
        ser.write(b'1')
        sleep(2)
        ser.write(b'3')
        sleep(2)
        ser.write(b'1')
        sleep(2)
