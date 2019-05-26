#!/usr/bin/env python
import minimalmodbus
from builtins import bytes
import binascii
import serial
import time

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

    def checkIOBoardType(self,registeraddress):
        # box address is 224~235
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x04'
        answer = self.instrument._performCommand(3, request)

        if answer == None:
            return
        else:
            IOBoardType = []
            for i in answer:
                IOBoardType.append(hex(ord(i)))

            return IOBoardType

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
            print("(hex)dataH:",hex(int(value/256)))
            print("(hex)dataL:",hex(int(value%256)))
            return self.instrument._performCommand(6, request)
