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

    def sensorWrite(self, request):
        return self.instrument._performCommand(6, request)

    def sensorON(self, registeraddress):
        request = "\x00"
        request += str(registeraddress)
        request += "\x00\x01"
        print("iensorONensorONuc",len(request))
        return self.sensorWrite(request)

    def sensorOFF(self, registeraddress):
        request = '\x00'
        request += str(registeraddress)
        request += '\x00\x00'
        return self.sensorWrite(request)

    def voltOutput(self, registeraddress, value):
        request = "\x00"
        request += registeraddress
        print("value:",value)
        value_string = str(hex(value))

        if ((len(value_string) - 2)%2) != 0:
            value_string = value_string[2:len(value_string)]
            value_string = "0" + value_string
        else:
            value_string = value_string[2:len(value_string)]

        print("iuahc",value_string)


        for i in value_string:
            print(i)

        for i in range(int(len(value_string)/2)):
            print("i:",i)
            print("ii:", str(int(value_string[i*2:i*2+2])))
            request = request + str(int(value_string[i*2:i*2+2]))

        print("ienuc",request)
        return self.sensorWrite(request)



        # for i in case:
        #     print("case:",i)
        #
        # for i in value_string:
        #     print(i)


# for i in range((len(s) - 2)/2 + 1):
#     request += "\x"
#     request += str(s[3:2])
#
# (len(s) - 2)%2


        # print("iuaijosvsvrijhc", s[3:5])


        value = minimalmodbus._numToTwoByteString(value)
        print("iuahsiuhisc", value)
        # request += str(hex(value))
        # print(request)
        # return self.sensorWrite(request)

def operation():
    port_name = '/dev/tty.usbserial-DN03VH4V'
    baudrate = 9600
    box_ID = 99

    acct1 = modbus(port_name, baudrate, box_ID)
    acct1.sensorON('\x07')

    acct1.voltOutput("\x10", 368)

    # print(acct1.instrument.read_register(13,3))
    # request = '\x00\x07\x00\x00'
    # request = '\x00'
    # request += str(registeraddress)
    # request += '\x00\x01'
    # return self.sensorWrite(request)
    # print(acct1.sensorRead(request) == '')
    #
    # for i in acct1.sensorRead(request) :
    #     print(i)

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
