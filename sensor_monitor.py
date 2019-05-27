#!/usr/bin/env python
from modbus import *
import math

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
        answer = self.modbus.registerRead(self.sensors_id.ORP)
        if answer == None:
            return
        else:
            return answer

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
    # communication setting
    PORT_NAME = '/dev/tty.usbserial-DN03VH4V'
    BAUDRATE = 9600

    # part id
    BOX_ID = 99
    ORP_ID = 1
    PH_ID = 2
    TEMP_ID = 3
    OXYGEN_ID = 4
    SALT_ID = 5
    WATER_ID = 6
    PUMP_ID = 7
    HEATER_ID = 8
    FEEDIND_MOTOR_ID = 9
    FILTERING_MOTOR_ID = 10
    FILLING_MOTOR_ID = 11
    MAGNETIC_DOOR_ID = 12

    sensors_id = SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID, WATER_ID)
    actuators_id = ActuatorAssignment(PUMP_ID, HEATER_ID, FEEDIND_MOTOR_ID, FILTERING_MOTOR_ID, FILLING_MOTOR_ID, MAGNETIC_DOOR_ID)
    monitor1 = Monitor(PORT_NAME, BAUDRATE, BOX_ID, sensors_id, actuators_id)

    # # test{
    #
    answer = monitor1.modbus.sensorOFF(9)
    if answer == None:
        print("control fault")
    else:
        print("control success")

    # board_type_list = monitor1.modbus.checkIOBoardType(0xE0)
    #
    # if board_type_list == None:
    #     print("No answer")
    # else:
    #     for type in board_type_list:
    #         print(type)

    print("ORP:", monitor1.readORP())
    # print("PH:", monitor1.readPH())
    # print("temp:", monitor1.readtemp())
    # print("Oxygen:", monitor1.readOxygen())
    # print("Salt:", monitor1.readSalt())
    # print("Water:", monitor1.readWater())
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
