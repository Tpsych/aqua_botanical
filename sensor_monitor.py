#!/usr/bin/env python
from modbus import *

class sensorAssignment():
    def __init__(self, ORP_sensor_num, PH_sensor_num, temp_sensor_num, Oxygen_sensor_num, salt_sensor_num):
        self.ORP = ORP_sensor_num
        self.PH = PH_sensor_num
        self.temp = temp_sensor_num
        self.Oxygen = Oxygen_sensor_num
        self.salt = salt_sensor_num

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
    q = monitor1.modbus.registerWrite(10, 368)
    # q = monitor1.readSalt()
    # # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
