#Aqua Botanical System
#Author: Barry Hao, Tony Tsai

import time
import Queue

#Constants
ABNORMAL_ORP = 1
ABNORMAL_PH = 2
ABNORMAL_TEMPERATURE = 3
ABNORMAL_OXYGEN = 4
ABNORMAL_SALT = 5
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

#Motor Boolean
gFeedingTankMotorState = False
gFilteringTankMotorState = False
gWaterFillingMotorState = False

#Electrical Magnetic Door
gElectricalMagneticDoorState = False

#Global queue for storing abnormal sensor
gQueueForAbnormalSensor = Queue.Queue()

def orpPerception():
    print("ORP perception")

def phPerception():
    print("PH perception")

def temperaturePerception():
    print("Temperature perception")

def oxygenPerception():
    print("Oxygen perception")

def saltPerception():
    print("Salt perception")

def plantLightControl():
    print("Light control for the plant")

def pumpOxygen():
    print("Pump Oxygen")

#Turn on/off heater
def heaterControl(command):
    print("Heater control")

#Get gFeedingTankWaterLevel and gFilteringTankWaterLevel
def waterLevelDetection():
    print("Water level detection")

#Turn on/off motors in feeding/filtering tank
def motorControl(feedingMotorCommand, filteringMotorCommand):
    print("Motor control")

#Turn/off filling motor
def fillingMotorControl(command):
    print("Filling Motor Control")
    waterLevelDetection()

#Turn on/off electrical Door
def electricalMagneticDoor(command):
    print("Electrical magnetic door")

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
    orpPerception()
    phPerception()
    temperaturePerception()
    saltPerception()
    oxygenPerception()

    return sensorState
def sensorOperation(abnormalSensor)
    print("Abnormal State Operation")

def main():
    while True:
        print("Aqua Botanical System!")
        restartAfterSensorOperation = False
        timeout = time.time() + 1800 # 30 minutes
        while time.time() < timeout:
            # Should create a queue for all abnormal state
            if gQueueForAbnormalSensor.qsize() == 0:
                time.sleep(5) # delay for 5 seconds
                sensorPerception()
            else:
                sensorOperation()
                restartAfterSensorOperation = True
                break
        if restartAfterSensorOperation:
            break
        timeout = time.time() + 300 # 5 minutes
        while time.time() < timeout:
            circulation()
        waterLevelDetection()
        while gFeedingTankWaterLevel != 1 and gFilteringTankWaterLevel != 1:
            waterLevelJudgementSecondStepInCirculation()
        motorControl(0, 0)

if __name__ == "__main__":
    main()
