#!/usr/bin/env python
import minimalmodbus
from builtins import bytes
import binascii
import serial
import time

class sensorAssignment():
    def __init__(self, ORP_sensor_num, PH_sensor_num, temp_sensor_num, Oxygen_sensor_num, salt_sensor_num):
        self.ORP = ORP_sensor_num
        self.PH = PH_sensor_num
        self.temp = temp_sensor_num
        self.Oxygen = Oxygen_sensor_num
        self.salt = salt_sensor_num

class Modbus:
    def __init__(self, port_name, baudrate, box_ID):
        minimalmodbus.BAUDRATE = baudrate
        self.instrument = minimalmodbus.Instrument(port_name, box_ID, mode ='rtu')
        self.instrument.debug = True
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity   = serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout  = 0.05   # seconds

    def optionalRead(self, request):
        return self.instrument._performCommand(3, request)

    def optionalWrite(self, request):
        return self.instrument._performCommand(6, request)

    def sensorON(self, registeraddress):
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x01'
        return self.instrument._performCommand(6, request)

    def sensorOFF(self, registeraddress):
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x00'
        return self.instrument._performCommand(6, request)

    def registerRead(self, registeraddress):
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x01'
        return self.instrument._performCommand(3, request)

    def registerWrite(self, registeraddress, value):
        if value > 65535 or value < 0:
            print("value parameter fault")

        else:
            request = '\x00'
            request += chr(int(registeraddress))
            request += chr(int(value/256))
            request += chr(int(value%256))

            print("output value:",value)
            return self.instrument._performCommand(6, request)

class SensorMonitor:
    def __init__(self, port_name, baudrate, box_ID, sensors_num):
        self.modbus = Modbus(port_name, baudrate, box_ID)
        self.ORP_sensors_num = sensors_num.ORP
        self.PH_sensors_num = sensors_num.PH
        self.temp_sensors_num = sensors_num.temp
        self.Oxygen_sensors_num = sensors_num.Oxygen
        self.salt_sensors_num = sensors_num.salt

    def readORP(self):
        return self.modbus.registerRead(self.ORP_sensors_num)

    def readPH(self):
        return self.modbus.registerRead(self.PH_sensors_num)

    def readtemp(self):
        return self.modbus.registerRead(self.temp_sensors_num)

    def readOxygen(self):
        return self.modbus.registerRead(self.Oxygen_sensors_num)

    def readSalt(self):
        return self.modbus.registerRead(self.salt_sensors_num)

def operation():
    port_name = '/dev/tty.usbserial-DN03VH4V'
    baudrate = 9600
    box_ID = 99
    sensor_num = sensorAssignment(0, 0, 0, 0, 0)
    monitor1 = SensorMonitor(port_name, baudrate, box_ID, sensor_num)

    # # test{
    # acct1.sensorOFF(9)
    # q = monitor1.modbus.registerWrite(10, 368)
    # q = monitor1.readSalt()
    # # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
