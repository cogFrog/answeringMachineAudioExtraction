# Importing Libraries
import serial
import time


class ArduinoSerial:
    def __init__(self, port):
        self.port = serial.Serial(port=port, baudrate=115200, timeout=.1)
        time.sleep(2)  # sleep while waiting for Arduino to get running

    def fetchBytes(self, pageNum):
        self.port.write(bytes(str(pageNum), 'utf-8'))
        time.sleep(0.05)
        data = self.port.readline()
        return data


if __name__ == "__main__":
    arduino = ArduinoSerial('/dev/ttyUSB0')
    value = arduino.fetchBytes(8191)  # retrieving all 2 MB takes ~6 minutes, be patient
    print(type(value))  # printing the value
    value = value.strip()
    print(value)
    print(len(value))

# todo: figure out if pyaudio wants a "bytes" object
