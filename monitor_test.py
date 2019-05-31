#!/usr/bin/env python
#Author: Barry Hao, Tony Tsai
from sensor_monitor import *

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
    WATER1_HIGH_ID = 6
    WATER1_LOW_ID = 7
    WATER2_HIGH_ID = 8
    WATER2_LOW_ID = 9
    PUMP_ID = 10
    HEATER_ID = 11
    FEEDIND_MOTOR_ID = 12
    FILTERING_MOTOR_ID = 13
    FILLING_MOTOR_ID = 14
    MAGNETIC_DOOR_ID = 15
    BUZZER_ID = 16

    # init monitor
    sensors_id = SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID,\
        WATER1_HIGH_ID, WATER1_LOW_ID, WATER2_HIGH_ID, WATER2_LOW_ID)
    actuators_id = ActuatorAssignment(PUMP_ID, HEATER_ID, FEEDIND_MOTOR_ID,\
        FILTERING_MOTOR_ID, FILLING_MOTOR_ID, MAGNETIC_DOOR_ID, BUZZER_ID)
    monitor1 = Monitor(PORT_NAME, BAUDRATE, BOX_ID, sensors_id, actuators_id)

    # test{
    answer = monitor1.modbus.sensorOFF(9)
    if answer == None:
        print("control fault")
    else:
        print("control success")

    board_type_list = monitor1.modbus.checkIOBoardType(0xE0)

    if board_type_list == None:
        print("No answer")
    else:
        for type in board_type_list:
            print(type)

    print("ORP:", monitor1.readORP())
    print("PH:", monitor1.readPH())
    print("temp:", monitor1.readtemp())
    print("Oxygen:", monitor1.readOxygen())
    print("Salt:", monitor1.readSalt())
    print("Water1High:", monitor1.readWater1High())
    print("Water1Low:", monitor1.readWater1Low())
    print("Water2High:", monitor1.readWater2High())
    print("Water2Low:", monitor1.readWater2Low())

    value = 0
    monitor1.writePump(value)
    monitor1.writeHeater(value)
    monitor1.writeFeedingMotor(value)
    monitor1.writeFilteringMotor(value)
    monitor1.writeFillingMotor(value)
    monitor1.writeMagneticDoor(value)
    # }test

def main():
    print("Aqua Botanical Actuator Drive!")
    operation()

if __name__ == "__main__":
    main()
