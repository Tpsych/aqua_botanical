#!/usr/bin/env python
from modbus import *

class SensorAssignment():
    def __init__(self, ORP_id, PH_id, temp_id, oxygen_id, salt_id, water_id):
        self.ORP = ORP_id
        self.PH = PH_id
        self.temp = temp_id
        self.oxygen = oxygen_id
        self.salt = salt_id
        self.water = water_id

class ActuatorAssignment():
    def __init__(self, pump_id, heater_id, feeding_motor_id, filtering_motor_id, filling_motor_id, magnetic_door_id):
        self.pump = pump_id
        self.heater = heater_id
        self.feeding_motor = feeding_motor_id
        self.filtering_motor = filtering_motor_id
        self.filling_motor = filling_motor_id
        self.magnetic_door = magnetic_door_id

class Monitor:
    def __init__(self, port_name, baudrate, box_id, sensors_id, actuators_id):
        self.modbus = Modbus(port_name, baudrate, box_id)
        self.sensors_id = sensors_id
        self.actuators_id = actuators_id

    def readORP(self):
        return self.modbus.registerRead(self.sensors_id.ORP)

    def readPH(self):
        return self.modbus.registerRead(self.sensors_id.PH)

    def readtemp(self):
        return self.modbus.registerRead(self.sensors_id.temp)

    def readOxygen(self):
        return self.modbus.registerRead(self.sensors_id.oxygen)

    def readSalt(self):
        return self.modbus.registerRead(self.sensors_id.salt)

    def readWater(self):
        return self.modbus.registerRead(self.sensors_id.water)

    def writePump(self, value):
        return self.modbus.registerWrite(self.actuators_id.pump, value)

    def writeHeater(self, value):
        return self.modbus.registerWrite(self.actuators_id.heater, value)

    def writeFeedingMotor(self, value):
        return self.modbus.registerWrite(self.actuators_id.feeding_motor, value)

    def writeFilteringMotor(self, value):
        return self.modbus.registerWrite(self.actuators_id.filtering_motor, value)

    def writeFillingMotor(self, value):
        return self.modbus.registerWrite(self.actuators_id.filling_motor, value)

    def writeMagneticDoor(self, value):
        return self.modbus.registerWrite(self.actuators_id.magnetic_door, value)

def operation():
    port_name = '/dev/tty.usbserial-DN03VH4V'
    baudrate = 9600
    box_id = 99
    sensors_id = SensorAssignment(1, 2, 3, 4, 5, 6)
    actuators_id = ActuatorAssignment(7, 8, 9, 10, 11, 12)
    monitor1 = Monitor(port_name, baudrate, box_id, sensors_id, actuators_id)

    # # test{
    #
    # monitor1.sensorOFF(9)
    # testValue = 585
    # testAnswer = monitor1.modbus.registerWrite(10, 369869868)
    # monitor1.readORP()
    # monitor1.readPH()
    # monitor1.readtemp()
    # monitor1.readOxygen()
    # monitor1.readSalt()
    # monitor1.readWater()
    # monitor1.writePump(value)
    # monitor1.writeHeater(value)
    # monitor1.writeFeedingMotor(value)
    # monitor1.writeFilteringMotor(value)
    # monitor1.writeFillingMotor(value)
    # monitor1.writeMagneticDoor(value)
    #
    # # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
