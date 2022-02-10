import os
import serial
import time
import csv

ser = serial.Serial('COM8', baudrate=2400)
ser.flushInput()

file = r"C:\Users\Alsace-Tresco\Documents\Voyage-Journal-main"
file = file + r"\Voyage-Journal-main\GPSlog.txt"

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode('utf-8')
        if len(decoded_bytes) > 40:
            print(decoded_bytes.rstrip('\n'))

            with open(file, "a") as log:
                log.writelines(decoded_bytes.rstrip('\n'))
        print("Logging started")
        print("Press Cntrl / cmd + C to interrupt.")
    except:  # noqa (bare except)
        log.close()
        print("Logging stopped")
        break
