#!/usr/bin/env python
#Author: Barry Hao, Tony Tsai
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
