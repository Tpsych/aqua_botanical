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
    WATER_HIGH_ID = 6
    WATER_LOW_ID = 7
    PUMP_ID = 8
    HEATER_ID = 9
    FEEDIND_MOTOR_ID = 10
    FILTERING_MOTOR_ID = 11
    FILLING_MOTOR_ID = 12
    MAGNETIC_DOOR_ID = 13
    BUZZER_ID = 14

    # init monitor
    sensors_id = SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID,\
        WATER_HIGH_ID, WATER_LOW_ID)
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
    print("WaterHigh:", monitor1.readWaterHigh())
    print("WaterLow:", monitor1.readWaterLow())

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
