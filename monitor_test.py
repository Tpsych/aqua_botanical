#!/usr/bin/env python
#Author: Barry Hao, Tony Tsai
from sensor_monitor import *

def operation():
    # communication setting
    PORT_NAME = '/dev/ttyUSB0'
    BAUDRATE = 9600

    # part id
    # box 1
    BOX1_ID = 99
    ORP_ID = 4
    PH_ID = 3
    TEMP_ID = 13
    OXYGEN_ID = 1
    SALT_ID = 2
    WATER1_HIGH_ID = 15
    WATER1_LOW_ID = 16
    WATER2_HIGH_ID = 11
    WATER2_LOW_ID = 12
    PUMP_ID = 7
    FEEDIND_MOTOR_ID = 6
    FILTERING_MOTOR_ID = 5

    # box 2
    BOX2_ID = 98
    HEATER_ID = 3
    FILLING_MOTOR_ID = 1
    LED_ID = 2
    MAGNETIC_DOOR_ID = 4
    BUZZER_ID = 5

    # init monitor
    box1_sensors_id = Box1SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID,\
        WATER1_HIGH_ID, WATER1_LOW_ID, WATER2_HIGH_ID, WATER2_LOW_ID)
    box1_actuators_id = Box1ActuatorAssignment(PUMP_ID, FEEDIND_MOTOR_ID, FILTERING_MOTOR_ID)
    box2_actuators_id = Box2ActuatorAssignment(HEATER_ID, FILLING_MOTOR_ID, LED_ID, MAGNETIC_DOOR_ID, BUZZER_ID)
    monitor1 = Monitor1(PORT_NAME, BAUDRATE, BOX1_ID, box1_sensors_id, box1_actuators_id)
    monitor2 = Monitor2(PORT_NAME, BAUDRATE, BOX2_ID, box2_actuators_id)

    # test{
    box1_type_list = monitor1.modbus.checkIOBoardType(0xE0)
    if box1_type_list == None:
        print("No answer form box1")
    else:
        print("box1_type_list:")
        for type in box1_type_list:
            print(type)

    box2_type_list = monitor2.modbus.checkIOBoardType(0xE0)
    if box2_type_list == None:
        print("No answer form box2")
    else:
        print("box2_type_list:")
        for type in box2_type_list:
            print(type)

    # box1 test
    if board1_type_list != None:
        print("test box1")
        print("ORP:", monitor1.readORP())
        print("PH:", monitor1.readPH())
        print("temp:", monitor1.readtemp())
        print("Oxygen:", monitor1.readOxygen())
        print("Salt:", monitor1.readSalt())
        print("Water1High:", monitor1.readWater1High())
        print("Water1Low:", monitor1.readWater1Low())
        print("Water2High:", monitor1.readWater2High())
        print("Water2Low:", monitor1.readWater2Low())

        value_for_testing_box1 = 0
        print("writePump:", monitor1.writePump(value_for_testing_box1))
        print("writeFeedingMotor:", monitor1.writeFeedingMotor(value_for_testing_box1))
        print("writeFilteringMotor:", monitor1.writeFilteringMotor(value_for_testing_box1))

    # box2 test
    if board2_type_list != None:
        print("test box2")
        value_for_testing_box2 = 0
        print("writeHeater:", monitor2.writeHeater(value_for_testing_box2))
        print("writeFillingMotor:", monitor2.writeFillingMotor(value_for_testing_box2))
        print("writeMagneticDoor:", monitor2.writeMagneticDoor(value_for_testing_box2))
        print("writeLED:", monitor2.writeLED(value_for_testing_box2))
        print("writeBuzzer:", monitor2.writeBuzzer(value_for_testing_box2))
    # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
