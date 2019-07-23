#Aqua Botanical System
#Author: Barry Hao, Tony Tsai

from sensor_monitor import *
from time import *
import os.path
import time

#Sensor Info
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
box2_actuators_id = Box2ActuatorAssignment(HEATER_ID, FILLING_MOTOR_ID, LED_ID,\
    MAGNETIC_DOOR_ID, GROUP1_ID, GROUP2_ID, GROUP3_ID, GROUP4_ID)
monitor1 = Monitor1(PORT_NAME, BAUDRATE, BOX1_ID, box1_sensors_id, box1_actuators_id)
monitor2 = Monitor2(PORT_NAME, BAUDRATE, BOX2_ID, box2_actuators_id)

############# START OF USER_DEFINE #############
# Constants
HIGH_ORP_THRESHOLD = 250 #mv
LOW_ORP_THRESHOLD = 200 #mv
HIGH_PH_THRESHOLD_1 = 8.5
HIGH_PH_THRESHOLD_2 = 8
LOW_PH_THRESHOLD_1 = 6.5
LOW_PH_THRESHOLD_2 = 7
LOW_TEMPERATURE_THRESHOLD = 20
MID_TEMPERATURE_THRESHOLD = 25
HIGH_TEMPERATURE_THRESHOLD = 30
LOW_OXYGEN_THRESHOLD = 6 #ppm
HIGH_OXYGEN_THRESHOLD = 6.5 #ppm
LOW_SALT_THRESHOLD = 200
MID_SALT_THRESHOLD = 300
HIGH_SALT_THRESHOLD = 400
############# END OF USER_DEFINE ###############

#Read from perception sensors
gFeedingTankWaterLevel = 4 # 0 for low, 1 for mid, 2 for high, 4 for initialization
gFilteringTankWaterLevel = 4 # 0 for low, 1 for mid, 2 for high, 4 for initialization
gORP = 0
gPH = 0
gTemperature = 0
gOxygen = 0
gSalt = 0

#Global table for storing abnormal sensor
gAbnormalState = dict(
    abnormalORP = False,
    abnormalPH = False,
    abnormalTemperature = False,
    abnormalOxygen = False,
    abnormalSalt = False
)

def warningBuzzer(command):
    print("Warning buzzer")
    monitor1.writeBuzzer(command)

def warningForLowSalt():
    print("Warning for low salt")
    warningBuzzer(1)
    time.sleep(10) ### USER_DEFINE ###
    warningBuzzer(0)

def orpPerception():
    print("ORP perception, the orp value now is: ")
    print(monitor1.readORP())
    gORP = monitor1.readORP()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/orp")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/orp", "a")
        f.write(strftime("%H:%M:%S") + ' ' + str(gORP) + '\n')
        f.close()
    else:
        print("Folder orp not created")

    if gORP < LOW_ORP_THRESHOLD:
        gAbnormalState['abnormalORP'] = True

def phPerception():
    print("PH perception, the ph value now is: ")
    print(monitor1.readPH())
    gPH = monitor1.readPH()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/ph")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/ph", "a")
        f.write(strftime("%H:%M:%S") + ' ' + str(gPH) + '\n')
        f.close()
    else:
        print("Folder ph not created")
    if gPH > HIGH_PH_THRESHOLD_1 or \
    gPH < LOW_PH_THRESHOLD_1:
        gAbnormalState['abnormalPH'] = True

def temperaturePerception():
    print("Temperature perception, the temperature value now is: ")
    print(monitor1.readtemp())
    gTemperature = monitor1.readtemp()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/temperature")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/temperature", "a")
        f.write(strftime("%H:%M:%S") + ' ' + str(gTemperature) + '\n')
        f.close()
    else:
        print("Folder temperature not created")

    if gTemperature > HIGH_TEMPERATURE_THRESHOLD or \
    gTemperature < LOW_TEMPERATURE_THRESHOLD:
        gAbnormalState['abnormalTemperature'] = True

def oxygenPerception():
    print("Oxygen perception, the oxygen value now is: ")
    print(monitor1.readOxygen())
    gOxygen = monitor1.readOxygen()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/oxygen")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/oxygen", "a")
        f.write(strftime("%H:%M:%S") + ' ' + str(gOxygen) + '\n')
        f.close()
    else:
        print("Folder oxygen not created")

    if gOxygen < LOW_OXYGEN_THRESHOLD:
        gAbnormalState['abnormalOxygen'] = True

def saltPerception():
    print("Salt perception, the salt value now is: ")
    print(monitor1.readSalt())
    gSalt = monitor1.readSalt()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/salt")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/salt", "a")
        f.write(strftime("%H:%M:%S") + ' ' + str(gSalt) + '\n')
        f.close()
    else:
        print("Folder salt not created")

    if gSalt > HIGH_SALT_THRESHOLD or \
    gSalt < LOW_SALT_THRESHOLD:
        gAbnormalState['abnormalSalt'] = True

def pumpOxygen(command):
    if command == 1:
        print("Pump Oxygen")
    else:
        print("Stop pumping Oxygen")
    monitor1.writePump(command)

#Turn on/off heater
def heaterControl(command):
    print("Heater control")
    monitor2.writeHeater(command)

#Get gFeedingTankWaterLevel and gFilteringTankWaterLevel
def waterLevelDetection():
    print("Water level detection")
    global gFeedingTankWaterLevel
    global gFilteringTankWaterLevel
    if monitor1.readWater1High() == True and monitor1.readWater1Low() == True:
        gFeedingTankWaterLevel = 0
    elif monitor1.readWater1High() == True and monitor1.readWater1Low() == False:
        gFeedingTankWaterLevel = 1
    else:
        gFeedingTankWaterLevel = 2
    if monitor1.readWater2High() == True and monitor1.readWater2Low() == True:
        gFilteringTankWaterLevel = 0
    elif monitor1.readWater2High() == True and monitor1.readWater2Low() == False:
        gFilteringTankWaterLevel = 1
    else:
        gFilteringTankWaterLevel = 2
    print("Feeding tank level")
    print(gFeedingTankWaterLevel)
    print("Filtering tank level")
    print(gFilteringTankWaterLevel)
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/water_level")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/water_level", "a")
        f.write(strftime("%H:%M:%S") + ' ' + "feeding tank" + ' '+ str(gFeedingTankWaterLevel) + '\n')
        f.write(strftime("%H:%M:%S") + ' ' + "filtering tank" + ' '+ str(gFilteringTankWaterLevel) + '\n')
        f.close()
    else:
        print("Folder water_level not created")

#Turn on/off motors in feeding/filtering tank
def motorControl(feedingMotorCommand, filteringMotorCommand):
    print("Motor control")
    print("Feeding motor command: " + str(feedingMotorCommand))
    monitor1.writeFeedingMotor(feedingMotorCommand)
    print("Filtering motor command: " + str(filteringMotorCommand))
    monitor1.writeFilteringMotor(filteringMotorCommand)

    feedingMotorStatus = monitor2.readFeedingMotorStatus()
    filteringMotorStatus = monitor2.readFilteringMotorStatus()

    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/home/pi/Desktop/sensor_data/" + fileDate + "/motor_command")
    if fileExist:
        f = open("/home/pi/Desktop/sensor_data/" + fileDate + "/motor_command", "a")
        f.write(strftime("%H:%M:%S") + ' ' + "feeding tank motor" + ' '+ str(feedingMotorStatus) + '\n')
        f.write(strftime("%H:%M:%S") + ' ' + "filtering tank motor" + ' '+ str(filteringMotorStatus) + '\n')
        f.close()
    else:
        print("Folder motor_command not created")

#Turn/off filling motor
def fillingMotorControl(command):
    print("Filling Motor Control")
    print(command)
    monitor2.writeFillingMotor(command)

#Turn on/off electrical Door
def electricalMagneticDoor(command):
    print("Electrical magnetic door")
    print(command)
    monitor2.writeMagneticDoor(command)

def checkFeedingTankWaterLevel(expectedLevel):
    while gFeedingTankWaterLevel != expectedLevel:
        waterLevelDetection()
        time.sleep(5) ### USER_DEFINE ###

def waterLevelJudgementFirstStepInCirculation():
    sensorPerception()
    print("Enter first step circulation")
    print("gFeedingTankWaterLevel in first circulation is: " + str(gFeedingTankWaterLevel))
    print("gFilteringTankWaterLevel in first circulation is: " + str(gFilteringTankWaterLevel))
    if gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 2:
        motorControl(0, 0)
        electricalMagneticDoor(1)
        checkFeedingTankWaterLevel(0)
        electricalMagneticDoor(0)
    elif gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 0 and gFilteringTankWaterLevel == 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel == 0 and gFilteringTankWaterLevel == 1:
        motorControl(0, 1)
    else:
        motorControl(0, 0)
        fillingMotorControl(1)
        checkFeedingTankWaterLevel(2)
        fillingMotorControl(0)

def waterLevelJudgementSecondStepInCirculation():
    sensorPerception()
    print("Enter second step circulation")
    print("gFeedingTankWaterLevel in second circulation is: " + str(gFeedingTankWaterLevel))
    print("gFilteringTankWaterLevel in second circulation is: " + str(gFilteringTankWaterLevel))
    if gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 2:
        motorControl(0, 0)
        electricalMagneticDoor(1)
        checkFeedingTankWaterLevel(0)
        electricalMagneticDoor(0)
    elif gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 2 and gFilteringTankWaterLevel == 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 1:
        motorControl(0, 0)
    elif gFeedingTankWaterLevel == 1 and gFilteringTankWaterLevel == 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel == 0 and gFilteringTankWaterLevel == 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel == 0 and gFilteringTankWaterLevel == 1:
        motorControl(0, 1)
    else:
        motorControl(0, 0)
        fillingMotorControl(1)
        checkFeedingTankWaterLevel(2)
        fillingMotorControl(0)

def circulation():
    print("Enter circulation")
    waterLevelDetection()
    waterLevelJudgementFirstStepInCirculation()

def sensorPerception():
    orpPerception()
    phPerception()
    temperaturePerception()
    saltPerception()
    oxygenPerception()

def temperatureOperation():
    print("Abnormal temperature operation")
    global gTemperature
    if gTemperature > HIGH_TEMPERATURE_THRESHOLD:
        timeout = time.time() + 30 ### USER_DEFINE ###
        while True:
            if time.time() < timeout:
                circulation()
                time.sleep(2) ### USER_DEFINE ###
            else:
                sensorPerception()
                if gTemperature < MID_TEMPERATURE_THRESHOLD:
                    break
                else:
                    timeout = time.time() + 30 ### USER_DEFINE ###
        gAbnormalState['abnormalTemperature'] = False

    if gTemperature < LOW_TEMPERATURE_THRESHOLD:
        timeout = time.time() + 30 ### USER_DEFINE ###
        heaterControl(1)
        while True:
            if time.time() < timeout:
                circulation()
                time.sleep(2) ### USER_DEFINE ###
            else:
                sensorPerception()
                if gTemperature > MID_TEMPERATURE_THRESHOLD:
                    break
                else:
                    timeout = time.time() + 30 ### USER_DEFINE ###
        heaterControl(0)
        gAbnormalState['abnormalTemperature'] = False

def oxygenOperation():
    print("Abnormal oxygen operation")
    gOxygen = monitor1.readOxygen()
    if gOxygen < LOW_OXYGEN_THRESHOLD:
        pumpOxygen(1)
        while gOxygen < HIGH_OXYGEN_THRESHOLD:
            print("Dbg: Oxygen value is: " + str(gOxygen))
            time.sleep(3) ### USER_DEFINE ###
            sensorPerception()
            gOxygen = monitor1.readOxygen()
        pumpOxygen(0)
        gAbnormalState['abnormalOxygen'] = False

def saltOperation():
    print("Abnormal salt operation")
    global gSalt
    if gSalt > HIGH_SALT_THRESHOLD:
        timeout = time.time() + 30 ### USER_DEFINE ###
        while True:
            if time.time() < timeout:
                    circulation()
                    time.sleep(2) ### USER_DEFINE ###
            else:
                sensorPerception()
                if gSalt < MID_SALT_THRESHOLD:
                    break
                else:
                    timeout = time.time() + 30 ### USER_DEFINE ###
        gAbnormalState['abnormalSalt'] = False

    if gSalt < LOW_SALT_THRESHOLD:
        warningForLowSalt()
        while gSalt < MID_SALT_THRESHOLD:
            warningForLowSalt()
            time.sleep(10) ### USER_DEFINE ###
            sensorPerception()
        gAbnormalState['abnormalSalt'] = False

def phOperation():
    print("Abnormal ph operation")
    global gPH
    if gPH > HIGH_PH_THRESHOLD_1 or \
    gPH < LOW_PH_THRESHOLD_1:
        timeout = time.time() + 30 ### USER_DEFINE ###
        while True:
            if time.time() < timeout:
                circulation()
                time.sleep(2) ### USER_DEFINE ###
            else:
                sensorPerception()
                if gPH < HIGH_PH_THRESHOLD_2 and \
                gPH > LOW_PH_THRESHOLD_2:
                    break
                else:
                    timeout = time.time() + 30 ### USER_DEFINE ###
        gAbnormalState['abnormalPH'] = False

def orpOperation():
    print("Abnormal orp operation")
    global gORP
    print("Current value is: " + str(gORP))
    if gORP < LOW_ORP_THRESHOLD:
        timeout = time.time() + 30 ### USER_DEFINE ###
        while True:
            if time.time() < timeout:
                    circulation()
                    time.sleep(2) ### USER_DEFINE ###
            else:
                sensorPerception()
                if gORP > HIGH_ORP_THRESHOLD:
                    break
                else:
                    timeout = time.time() + 30 ### USER_DEFINE ###
        gAbnormalState['abnormalORP'] = False

def sensorOperation():
    print("Abnormal State Operation")
    if gAbnormalState['abnormalORP'] == True:
        orpOperation()
    if gAbnormalState['abnormalPH'] == True:
        phOperation()
    if gAbnormalState['abnormalTemperature'] == True:
        temperatureOperation()
    if gAbnormalState['abnormalOxygen'] == True:
        oxygenOperation()
    if gAbnormalState['abnormalSalt'] == True:
        saltOperation()

def main():
    monitor2.writeLED(1)
    while True:
        print("Aqua Botanical System!")
        restartFlag = False
        timeout = time.time() + 40 ### USER_DEFINE ###
        while time.time() < timeout:
            if gAbnormalState['abnormalORP'] == False and \
            gAbnormalState['abnormalPH'] == False and \
            gAbnormalState['abnormalTemperature'] == False and \
            gAbnormalState['abnormalOxygen'] == False and \
            gAbnormalState['abnormalSalt'] == False:
                time.sleep(5)
                sensorPerception()
            else:
                sensorOperation()
                restartFlag = True
                print("Restart circulation")
                break
        if restartFlag == False:
            timeout = time.time() + 30 ### USER_DEFINE ###
            while time.time() < timeout:
                time.sleep(5) ### USER_DEFINE ###
                circulation()
            waterLevelDetection()
            while gFeedingTankWaterLevel != 1 and gFilteringTankWaterLevel != 1:
                waterLevelJudgementSecondStepInCirculation()
                time.sleep(5) ### USER_DEFINE ###
                waterLevelDetection()
            motorControl(0, 0)
            print("Restart circulation")

if __name__ == "__main__":
    main()
