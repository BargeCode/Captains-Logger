import os
import serial
import time
import csv


"""
On board our vessel we have a computer with a GPS antenna hooked up on a
COMport. With the code below, it will filter incoming data on length because
GPRMC data is the longest of the data it sends trough the COMport.
I will try to apply some geo-fencing so that it knows which sector is active.
"""


ser = serial.Serial('COM8', baudrate=2400)
ser.flushInput()

file = r"C:\Users\Alsace-Tresco\Documents\Voyage-Journal-main\Voyage-Journal-main\GPSlog.txt"

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode('utf-8')
        if len(decoded_bytes) > 40:
            print(decoded_bytes.rstrip('\n'))

            with open(file, "a") as log:
                log.writelines(decoded_bytes.rstrip('\n'))

    except:  # noqa (bare except)
        log.close()
        print("Logging stopped for some reason.")
        break
