#!/usr/bin/env python
#Author: Barry Hao, Tony Tsai
from sensor_monitor import *

def operation():
    # communication setting
    PORT_NAME = '/dev/ttyp0'
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
    BUZZER_ID = 8

    # box 2
    BOX2_ID = 98
    HEATER_ID = 3
    FILLING_MOTOR_ID = 1
    LED_ID = 2
    MAGNETIC_DOOR_ID = 4
    GROUP1_ID = 5
    GROUP2_ID = 6
    GROUP3_ID = 7
    GROUP4_ID = 8

    # init monitor
    box1_sensors_id = Box1SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID,\
        WATER1_HIGH_ID, WATER1_LOW_ID, WATER2_HIGH_ID, WATER2_LOW_ID)
    box1_actuators_id = Box1ActuatorAssignment(PUMP_ID, FEEDIND_MOTOR_ID, FILTERING_MOTOR_ID, BUZZER_ID)
    box2_sensors_id = Box2SensorAssignment(GROUP1_ID, GROUP2_ID, GROUP3_ID, GROUP4_ID)
    box2_actuators_id = Box2ActuatorAssignment(HEATER_ID, FILLING_MOTOR_ID, LED_ID,\
        MAGNETIC_DOOR_ID, GROUP1_ID, GROUP2_ID, GROUP3_ID, GROUP4_ID)

    monitor1 = Monitor1(PORT_NAME, BAUDRATE, BOX1_ID, box1_sensors_id, box1_actuators_id)
    monitor2 = Monitor2(PORT_NAME, BAUDRATE, BOX2_ID, box2_sensors_id, box2_actuators_id)

    # test
    box1_type_list = monitor1.modbus.checkIOBoardType(0xE0)
    print(" ")
    if box1_type_list == None:
        print("No answer form box1")
    else:
        print("box1_type_list:")
        for type in box1_type_list:
            print(type)

    box2_type_list = monitor2.modbus.checkIOBoardType(0xE0)
    print(" ")
    if box2_type_list == None:
        print("No answer form box2")
    else:
        print("box2_type_list:")
        for type in box2_type_list:
            print(type)

    # box1 test
    # you can mark "#" the interface you would not test
    if box1_type_list != None:
        print(" ")
        print("test box1 ...")
        print("read ORP:", monitor1.readORP(), ", raw:", monitor1.modbus.registerRead(ORP_ID, signed = False))
        print("read PH:", monitor1.readPH(), ", raw:", monitor1.modbus.registerRead(PH_ID, signed = False))
        print("read temp:", monitor1.readtemp(), ", raw:", monitor1.modbus.registerRead(TEMP_ID, signed = False))
        print("read Oxygen:", monitor1.readOxygen(), ", raw:", monitor1.modbus.registerRead(OXYGEN_ID, signed = False))
        print("read Salt:", monitor1.readSalt(), ", raw:", monitor1.modbus.registerRead(SALT_ID, signed = False))
        print("read Water1High:", monitor1.readWater1High(), ", raw:", monitor1.modbus.registerRead(WATER1_HIGH_ID, signed = False))
        print("read Water1Low:", monitor1.readWater1Low(), ", raw:", monitor1.modbus.registerRead(WATER1_LOW_ID, signed = False))
        print("read Water2High:", monitor1.readWater2High(), ", raw:", monitor1.modbus.registerRead(WATER2_HIGH_ID, signed = False))
        print("read Water2Low:", monitor1.readWater2Low(), ", raw:", monitor1.modbus.registerRead(WATER2_LOW_ID, signed = False))

        value_for_testing_box1 = 0
        print("write Pump:", monitor1.writePump(value_for_testing_box1))
        print("write FeedingMotor:", monitor1.writeFeedingMotor(value_for_testing_box1))
        print("write FilteringMotor:", monitor1.writeFilteringMotor(value_for_testing_box1))
        print("write Buzzer:", monitor1.writeBuzzer(value_for_testing_box1))

    # box2 test
    if box2_type_list != None:
        print(" ")
        print("test box2 ...")

        value_for_testing_box2 = 0
        print("write Heater:", monitor2.writeHeater(value_for_testing_box2))
        print("write FillingMotor:", monitor2.writeFillingMotor(value_for_testing_box2))
        print("write MagneticDoor:", monitor2.writeMagneticDoor(value_for_testing_box2))
        print("write LED:", monitor2.writeLED(value_for_testing_box2))
        print("read FillingMotorStatus:", monitor2.readFillingMotorStatus())
        print("read HeaterStatus:", monitor2.readHeaterStatus())
        print("read MagneticDoorStatus:", monitor2.readMagneticDoorStatus())
        print("read PumpStatus:", monitor2.readPumpStatus())
        print("read FeedingMotorStatus:", monitor2.readFeedingMotorStatus())
        print("read FilteringMotorStatus:", monitor2.readFilteringMotorStatus())

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
