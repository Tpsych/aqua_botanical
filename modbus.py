#!/usr/bin/env python
import modbus_library
from builtins import bytes
import binascii
import serial
import math
import time

def twos_complement(hexstr,bits):
     value = int(hexstr,16)
     if value & (1 << (bits-1)):
         value -= 1 << bits
     return value

class Modbus:
    def __init__(self, port_name, baudrate, box_ID):
        modbus_library.BAUDRATE = baudrate
        self.instrument = modbus_library.Instrument(port_name, box_ID, mode ='rtu')
        self.instrument.debug = False
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity   = serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout  = 0.05   # seconds

    def optionalRead(self, request):
        answer = self.instrument._performCommand(3, request)
        if answer == None:
            return
        else:
            return answer

    def optionalWrite(self, request):
        answer = self.instrument._performCommand(6, request)
        if answer == None:
            return
        else:
            return answer

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
        answer = self.instrument._performCommand(6, request)

        if answer == None:
            return
        else:
            return answer

    def sensorOFF(self, registeraddress):
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x00'
        answer = self.instrument._performCommand(6, request)

        if answer == None:
            return
        else:
            return answer

    def registerRead(self, registeraddress, signed = True):
        request = '\x00'
        request += chr(int(registeraddress))
        request += '\x00\x01'
        answer = self.instrument._performCommand(3, request)

        if answer == None:
            return
        else:
            value = 0
            data_num = int(ord(answer[0]))
            for i in range(data_num):
                value = value + int(ord(answer[i+1])) * math.pow( 256, data_num - 1 - i)
                # value = hex(value) & 0xffff

            if signed == True:
                value = twos_complement(hex(int(value)), 16)

            return value

    def registerWrite(self, registeraddress, value):
        if value > 65535 or value < 0:
            print("value parameter fault")

        else:
            request = '\x00'
            request += chr(int(registeraddress))
            request += chr(int(value/256))
            request += chr(int(value%256))

            if self.instrument.debug:
                print("output value:",value)
                print("(hex)dataH:",hex(int(value/256)))
                print("(hex)dataL:",hex(int(value%256)))
            answer = self.instrument._performCommand(6, request)

            if answer == None:
                return
            else:
                return answer
