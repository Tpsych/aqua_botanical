#!/usr/bin/env python
#Author: Barry Hao, Tony Tsai
from modbus import *
import math

class Box1SensorAssignment():
    def __init__(self, ORP_id, PH_id, temp_id, oxygen_id, salt_id,\
        water1_high_id, water1_low_id, water2_high_id, water2_low_id):
        self.ORP = ORP_id
        self.PH = PH_id
        self.temp = temp_id
        self.oxygen = oxygen_id
        self.salt = salt_id
        self.water1_high = water1_high_id
        self.water1_low = water1_low_id
        self.water2_high = water2_high_id
        self.water2_low = water2_low_id

class Box1ActuatorAssignment():
    def __init__(self, pump_id, feeding_motor_id, filtering_motor_id):
        self.pump = pump_id
        self.feeding_motor = feeding_motor_id
        self.filtering_motor = filtering_motor_id

class Box2ActuatorAssignment():
    def __init__(self, heater_id, filling_motor_id, led_id, magnetic_door_id, buzzer_id):
        self.heater = heater_id
        self.led = led_id
        self.filling_motor = filling_motor_id
        self.magnetic_door = magnetic_door_id
        self.buzzer = buzzer_id

class Monitor1:
    def __init__(self, port_name, baudrate, box_id, sensors_id, actuators_id):
        self.modbus = Modbus(port_name, baudrate, box_id)
        self.sensors_id = sensors_id
        self.actuators_id = actuators_id

    def readORP(self):
        answer = self.modbus.registerRead(self.sensors_id.ORP, signed = False)
        if answer == None:
            return
        else:
            answer = ((answer - 800.0) / 3200.0 * 200.0)
            return answer

    def readPH(self):
        answer =  self.modbus.registerRead(self.sensors_id.PH, signed = False)
        if answer == None:
            return
        else:
            answer = ((answer - 800.0) / 3200.0 * 14.0)
            return answer

    def readtemp(self):
        answer = self.modbus.registerRead(self.sensors_id.temp)
        if answer == None:
            return
        else:
            return answer / 10.0

    def readOxygen(self):
        answer = self.modbus.registerRead(self.sensors_id.oxygen, signed = False)
        if answer == None:
            return
        else:
            # answer = ((answer/200.0 - 4.0) * 20.0 / 16.0)
            answer = ((answer - 800.0) / 3200.0 * 20.0)
            return answer

    def readSalt(self):
        answer = self.modbus.registerRead(self.sensors_id.salt)
        if answer == None:
            return
        else:
            # answer = ((answer/200.0 - 4.0) * (66.7-1.32) / 16.0 + 1.32) * 10.0
            if answer < 800:
                print("Salt sensor disconnect")
                return
            else:
                answer = ((answer - 800.0) / 3200.0 * 600.0)
                return answer

    def readWater1High(self):
        return self.modbus.registerRead(self.sensors_id.water1_high)

    def readWater1Low(self):
        return self.modbus.registerRead(self.sensors_id.water1_low)

    def readWater2High(self):
        return self.modbus.registerRead(self.sensors_id.water2_high)

    def readWater2Low(self):
        return self.modbus.registerRead(self.sensors_id.water2_low)

    def writePump(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.pump, value)
        else:
            print("Pump control parameter fault")
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

class Monitor2:
    def __init__(self, port_name, baudrate, box_id, actuators_id):
        self.modbus = Modbus(port_name, baudrate, box_id)
        self.actuators_id = actuators_id

    def writeHeater(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.heater, value)
        else:
            print("Heater control parameter fault")
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

    def writeLED(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.led, value)
        else:
            print("Buzzer control parameter fault")
            return

    def writeBuzzer(self, value):
        if value == 0 or value == 1:
            return self.modbus.registerWrite(self.actuators_id.buzzer, value)
        else:
            print("Buzzer control parameter fault")
            return
