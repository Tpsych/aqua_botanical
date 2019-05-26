#!/usr/bin/env python
import minimalmodbus
from builtins import bytes
import binascii
import serial
import time

class modbus:
    def __init__(self, port_name, baudrate, box_ID):
        minimalmodbus.BAUDRATE = baudrate
        self.instrument = minimalmodbus.Instrument(port_name, box_ID, mode ='rtu')
        self.instrument.debug = True
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity   = serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout  = 0.05   # seconds
        # self.name = name

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
        request = '\x00'
        request += chr(int(registeraddress))
        request += chr(int(value/256))
        request += chr(int(value%256))

        print("output value:",value)
        return self.instrument._performCommand(6, request)

def operation():
    port_name = '/dev/tty.usbserial-DN03VH4V'
    baudrate = 9600
    box_ID = 99

    acct1 = modbus(port_name, baudrate, box_ID)
    # # test{
    # acct1.sensorOFF(9)
    # acct1.voltOutput(10, 368)
    # # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
