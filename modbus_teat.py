#!/usr/bin/env python
import minimalmodbus
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

    def sensorRead(self, request):
        return self.instrument._performCommand(3, request)

    def writeRead(self, request):
        return self.instrument._performCommand(6, request)
