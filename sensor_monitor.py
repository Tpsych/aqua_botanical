#!/usr/bin/env python
from modbus import *
import math

class SensorAssignment():
    def __init__(self, ORP_id, PH_id, temp_id, oxygen_id, salt_id, water_high_id, water_low_id):
        self.ORP = ORP_id
        self.PH = PH_id
        self.temp = temp_id
        self.oxygen = oxygen_id
        self.salt = salt_id
        self.water_high = water_high_id
        self.water_low = water_low_id

class ActuatorAssignment():
    def __init__(self, pump_id, heater_id, feeding_motor_id, filtering_motor_id, \
            filling_motor_id, magnetic_door_id, buzzer_id):
        self.pump = pump_id
        self.heater = heater_id
        self.feeding_motor = feeding_motor_id
        self.filtering_motor = filtering_motor_id
        self.filling_motor = filling_motor_id
        self.magnetic_door = magnetic_door_id
        self.buzzer = buzzer_id

class Monitor:
    def __init__(self, port_name, baudrate, box_id, sensors_id, actuators_id):
        self.modbus = Modbus(port_name, baudrate, box_id)
        self.sensors_id = sensors_id
        self.actuators_id = actuators_id

    def readORP(self):
        answer = self.modbus.registerRead(self.sensors_id.ORP, signed = False)
        if answer == None:
            return
        else:
            answer = answer * 20.0 /4000.0
            answer = (answer - 4.0) * 14.0 / 16.0
            return answer

    def readPH(self):
        answer =  self.modbus.registerRead(self.sensors_id.PH, signed = False)
        if answer == None:
            return
        else:
            answer = answer * 20.0 /4000.0
            answer = (answer - 4.0) * 14.0 / 16.0
            return answer

    def readtemp(self):
        return self.modbus.registerRead(self.sensors_id.temp)

    def readOxygen(self):
        answer = self.modbus.registerRead(self.sensors_id.oxygen, signed = False)
        if answer == None:
            return
        else:
            answer = answer * 20.0 /4000.0
            answer = (answer - 4.0) * 20.0 / 16.0
            return answer

    def readSalt(self):
        answer = self.modbus.registerRead(self.sensors_id.salt)
        if answer == None:
            return
        else:
            answer =  answer * 20.0 /4000.0
            answer = (answer - 4.0) * 600.0 / 16.0
            return answer

    def readWaterHigh(self):
        return self.modbus.registerRead(self.sensors_id.water_high)

    def readWaterLow(self):
        return self.modbus.registerRead(self.sensors_id.water_low)

    def writePump(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.pump, value)
        else:
            print("Pump control parameter fault")
            return

    def writeHeater(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.heater, value)
        else:
            print("Heater control parameter fault")
            return

    def writeFeedingMotor(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.feeding_motor, value)
        else:
            print("FeedingMotor control parameter fault")
            return

    def writeFilteringMotor(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.filtering_motor, value)
        else:
            print("FilteringMotor control parameter fault")
            return

    def writeFillingMotor(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.filling_motor, value)
        else:
            print("FillingMotor control parameter fault")
            return

    def writeMagneticDoor(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.magnetic_door, value)
        else:
            print("MagneticDoor control parameter fault")
            return

    def writeBuzzer(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.buzzer, value)
        else:
            print("Buzzer control parameter fault")
            return

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
    WATER_HIGH_ID = 6
    WATER_LOW_ID = 7
    PUMP_ID = 8
    HEATER_ID = 9
    FEEDIND_MOTOR_ID = 10
    FILTERING_MOTOR_ID = 11
    FILLING_MOTOR_ID = 12
    MAGNETIC_DOOR_ID = 13
    BUZZER_ID = 14

    sensors_id = SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID,\
        WATER_HIGH_ID, WATER_LOW_ID)
    actuators_id = ActuatorAssignment(PUMP_ID, HEATER_ID, FEEDIND_MOTOR_ID,\
        FILTERING_MOTOR_ID, FILLING_MOTOR_ID, MAGNETIC_DOOR_ID, BUZZER_ID)
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

    value = 0
    print("ORP:", monitor1.readORP())
    print("PH:", monitor1.readPH())
    print("temp:", monitor1.readtemp())
    print("Oxygen:", monitor1.readOxygen())
    print("Salt:", monitor1.readSalt())
    print("WaterHigh:", monitor1.readWaterHigh())
    print("WaterLow:", monitor1.readWaterLow())
    monitor1.writePump(value)
    monitor1.writeHeater(value)
    monitor1.writeFeedingMotor(value)
    monitor1.writeFilteringMotor(value)
    monitor1.writeFillingMotor(value)
    monitor1.writeMagneticDoor(value)
    #
    # # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
