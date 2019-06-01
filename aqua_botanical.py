#Aqua Botanical System
#Author: Barry Hao, Tony Tsai

from sensor_monitor import *
from time import *
import os.path
import time

#Sensor Info
PORT_NAME = '/dev/tty.usbserial-DN03VH4V'
BAUDRATE = 9600
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

#Global sensor objects
gSensorsId = SensorAssignment(ORP_ID, PH_ID, TEMP_ID, OXYGEN_ID, SALT_ID, \
WATER1_HIGH_ID, WATER1_LOW_ID, WATER2_HIGH_ID, WATER2_LOW_ID)

gActuatorsId = ActuatorAssignment(PUMP_ID, HEATER_ID, FEEDIND_MOTOR_ID, \
FILTERING_MOTOR_ID, FILLING_MOTOR_ID, MAGNETIC_DOOR_ID, BUZZER_ID)

gMonitor = Monitor(PORT_NAME, BAUDRATE, BOX_ID, gSensorsId, gActuatorsId)

#Constants
HIGH_ORP_THRESHOLD = 250 #mv
LOW_ORP_THRESHOLD = 200 #mv
HIGH_PH_THRESHOLD_1 = 8.5
HIGH_PH_THRESHOLD_2 = 8
LOW_PH_THRESHOLD_1 = 6.5
LOW_PH_THRESHOLD = 7
LOW_TEMPERATURE_THRESHOLD = 20
MID_TEMPERATURE_THRESHOLD = 25
HIGH_TEMPERATURE_THRESHOLD = 30
LOW_OXYGEN_THRESHOLD = 6 #ppm
HIGH_OXYGEN_THRESHOLD = 6.5 #ppm
LOW_SALT_THRESHOLD = 20
MID_SALT_THRESHOLD = 25
HIGH_SALT_THRESHOLD = 30
ABNORMAL_TIME_LIMIT = 5 #minute

#Read from perception sensors
gFeedingTankWaterLevel = None # 0 for low, 1 for mid, 2 for high
gFilteringTankWaterLevel = None # 0 for low, 1 for mid, 2 for high
gORP = None
gPH = None
gTemperature = None
gOxygen = None
gSalt = None

#Electrical Magnetic Door
gElectricalMagneticDoorState = False

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
    gMonitor.writeBuzzer(command)

def warningForLowSalt():
    print("Warning for low salt")
    warningBuzzer(1)
    time.sleep(10)
    warningBuzzer(0)

def orpPerception():
    print("ORP perception, the orp value now is:")
    print(gMonitor.readORP())
    gORP = gMonitor.readORP()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/path_in_raspberry_pi")
    if fileExist:
        f = open("/path_in_raspberry_pi", "a")
        f.write(strftime("%H:%M:%S")+ ' ' + gORP)
        f.close()
    else:
        print("File not created")

    if gORP < LOW_ORP_THRESHOLD:
        gAbnormalState['abnormalORP'] = True

def phPerception():
    print("PH perception, the ph value now is:")
    print(gMonitor.readPH())
    gPH = gMonitor.readPH()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/path_in_raspberry_pi")
    if fileExist:
        f = open("/path_in_raspberry_pi", "a")
        f.write(strftime("%H:%M:%S")+ ' ' + gPH)
        f.close()
    else:
        print("File not created")
    if gPH > HIGH_PH_THRESHOLD_1 or \
    gPH < LOW_PH_THRESHOLD_1:
        gAbnormalState['abnormalPH'] = True

def temperaturePerception():
    print("Temperature perception, the temperature value now is:")
    print(gMonitor.readtemp())
    gTemperature = gMonitor.readtemp()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/path_in_raspberry_pi")
    if fileExist:
        f = open("/path_in_raspberry_pi", "a")
        f.write(strftime("%H:%M:%S")+ ' ' + gTemperature)
        f.close()
    else:
        print("File not created")

    if gTemperature > HIGH_TEMPERATURE_THRESHOLD or \
    gTemperature < LOW_TEMPERATURE_THRESHOLD:
        gAbnormalState['abnormalTemperature'] = True

def oxygenPerception():
    print("Oxygen perception, the oxygen value now is:")
    print(gMonitor.readOxygen())
    gOxygen = gMonitor.readOxygen()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/path_in_raspberry_pi")
    if fileExist:
        f = open("/path_in_raspberry_pi", "a")
        f.write(strftime("%H:%M:%S")+ ' ' + gOxygen)
        f.close()
    else:
        print("File not created")

    if gOxygen < LOW_OXYGEN_THRESHOLD:
        gAbnormalState['abnormalOxygen'] = True

def saltPerception():
    print("Salt perception, the salt value now is:")
    print(gMonitor.readSalt())
    gSalt = gMonitor.readSalt()
    fileDate = strftime("%m_%d_%Y")
    fileExist = os.path.isfile("/path_in_raspberry_pi")
    if fileExist:
        f = open("/path_in_raspberry_pi", "a")
        f.write(strftime("%H:%M:%S")+ ' ' + gSalt)
        f.close()
    else:
        print("File not created")

    if gSalt > HIGH_SALT_THRESHOLD or \
    gSalt < LOW_SALT_THRESHOLD:
        gAbnormalState['abnormalSalt'] = True

def pumpOxygen(command):
    print("Pump Oxygen")
    gMonitor.writePump(command)

#Turn on/off heater
def heaterControl(command):
    print("Heater control")
    gMonitor.writeHeater(command)

#Get gFeedingTankWaterLevel and gFilteringTankWaterLevel
def waterLevelDetection():
    print("Water level detection")
    if readWater1High() == True and readWater1Low() == True:
        gFeedingTankWaterLevel = 2
    elif readWater1High() == False and readWater1Low() == True:
        gFeedingTankWaterLevel = 1
    else:
        gFeedingTankWaterLevel =0
    if readWater2High() == True and readWater2Low() == True:
        gFilteringTankWaterLevel = 2
    elif readWater2High() == False and readWater2Low() == True:
        gFilteringTankWaterLevel = 1
    else:
        gFilteringTankWaterLevel =0

#Turn on/off motors in feeding/filtering tank
def motorControl(feedingMotorCommand, filteringMotorCommand):
    print("Motor control")
    gMonitor.writeFeedingMotor(feedingMotorCommand)
    gMonitor.writeFilteringMotor(filteringMotorCommand)

#Turn/off filling motor
def fillingMotorControl(command):
    print("Filling Motor Control")
    gMonitor.writeFillingMotor(command)

#Turn on/off electrical Door
def electricalMagneticDoor(command):
    print("Electrical magnetic door")
    gMonitor.writeMagneticDoor(command)

def checkFeedingTankWaterLevel(expectedLevel):
    while gFeedingTankWaterLevel != expectedLevel:
        waterLevelDetection()
        time.sleep(5)

def waterLevelJudgementFirstStepInCirculation():
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
        checkFeedingTankWaterLevel(1)
        fillingMotorControl(0)

def waterLevelJudgementSecondStepInCirculation():
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
        checkFeedingTankWaterLevel(1)
        fillingMotorControl(0)

def circulation():
    waterLevelDetection()
    waterLevelJudgementFirstStepInCirculation()

def sensorPerception():
    todayDate = date.today()
    orpPerception()
    phPerception()
    temperaturePerception()
    saltPerception()
    oxygenPerception()

def temperatureOperation():
    print("Abnormal temperature operation")
    global gTemperature
    if gTemperature > HIGH_TEMPERATURE_THRESHOLD:
        timeout = time.time() + 300
        while gTemperature > MID_TEMPERATURE_THRESHOLD and \
        time.time() < timeout:
            circulation()
            time.sleep(5)
            temperaturePerception()
        gAbnormalState['abnormalTemperature'] = False

    if gTemperature < LOW_TEMPERATURE_THRESHOLD:
        timeout = time.time() + 300
        heaterControl(1)
        while gTemperature < MID_TEMPERATURE_THRESHOLD and \
        time.time() < timeout:
            time.sleep(10)
            temperaturePerception()
        heaterControl(0)
        gAbnormalState['abnormalTemperature'] = False

def oxygenOperation():
    print("Abnormal oxygen operation")
    global gOxygen
    if gOxygen < LOW_OXYGEN_THRESHOLD:
        pumpOxygen(1)
        while gOxygen < HIGH_OXYGEN_THRESHOLD:
            time.sleep(10)
            oxygenPerception()
        pumpOxygen(0)
        gAbnormalState['abnormalOxygen'] = False

def saltOperation():
    print("Abnormal salt operation")
    global gSalt
    if gSalt > HIGH_SALT_THRESHOLD:
        timeout = time.time() + 300
        while gSalt > MID_SALT_THRESHOLD and \
        time.time() < timeout:
            circulation()
            time.sleep(5)
            saltPerception()
        gAbnormalState['abnormalSalt'] = False

    if gSalt < LOW_SALT_THRESHOLD:
        warningForLowSalt()
        while gSalt < MID_SALT_THRESHOLD:
            warningForLowSalt()
            time.sleep(10)
            saltPerception()
        gAbnormalState['abnormalSalt'] = False

def phOperation():
    print("Abnormal ph operation")
    global gPH
    if gPH > HIGH_PH_THRESHOLD_1 or \
    gPH < LOW_PH_THRESHOLD_1:
        timeout = time.time() + 300
        while gPH > HIGH_PH_THRESHOLD_2 or \
        gPH < LOW_PH_THRESHOLD_2 and \
        time.time() < timeout:
            circulation()
            time.sleep(5)
            phPerception()
        gAbnormalState['abnormalPH'] = False

def orpOperation():
    print("Abnormal orp operation")
    global gORP
    if gORP < LOW_ORP_THRESHOLD:
        timeout = time.time() + 300
        while gORP < HIGH_ORP_THRESHOLD and \
        time.time() < timeout:
            time.sleep(10)
            orpPerception()
        gAbnormalState['abnormalORP'] = False

def sensorOperation():
    print("Abnormal State Operation")
    if gAbnormalState['abnormalORP'] == True:
        orpOperation()
        gAbnormalState['abnormalORP'] = False
    if gAbnormalState['abnormalPH'] == True:
        phOperation()
        gAbnormalState['abnormalPH'] = False
    if gAbnormalState['abnormalTemperature'] == True:
        temperatureOperation()
        gAbnormalState['abnormalTemperature'] = False
    if gAbnormalState['abnormalOxygen'] == True:
        oxygenOperation()
        gAbnormalState['abnormalOxygen'] = False
    if gAbnormalState['abnormalSalt'] == True:
        saltOperation()
        gAbnormalState['abnormalSalt'] = False

def main():
    while True:
        print("Aqua Botanical System!")
        restartFlag = False
        timeout = time.time() + 1800 # 30 minutes
        while time.time() < timeout:
            if gAbnormalState['abnormalORP'] == False and \
            gAbnormalState['abnormalPH'] == False and \
            gAbnormalState['abnormalTemperature'] == False and \
            gAbnormalState['abnormalOxygen'] == False and \
            gAbnormalState['abnormalSalt'] == False:
                time.sleep(10)
                sensorPerception()
            else:
                sensorOperation()
                restartFlag = True
                break
        if restartFlag == False:
            timeout = time.time() + 300 # 5 minutes
            while time.time() < timeout:
                time.sleep(10)
                circulation()
            waterLevelDetection()
            while gFeedingTankWaterLevel != 1 and gFilteringTankWaterLevel != 1:
                waterLevelJudgementSecondStepInCirculation()
                time.sleep(10)
                waterLevelDetection()
            motorControl(0, 0)
            print("Restart circulation")

if __name__ == "__main__":
    main()
