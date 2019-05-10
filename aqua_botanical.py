#Aqua Botanical System
#Author: Barry Hao, Tony Tsai
#Multi thread?
#Defition of the water level?
#Flow chart heater

import time

#Constants
FEEDING_TANK_WATER_HIGH_LEVEL = 200
FEEDING_TANK_WATER_MID_LEVEL = 150
FEEDING_TANK_WATER_LOW_LEVEL = 100
FILTERING_TANK_WATER_HIGH_LEVEL = 200
FILTERING_TANK_WATER_MID_LEVEL = 150
FILTERING_TANK_WATER_LOW_LEVEL = 100
HIGHER_ORP_THRESHOLD = 250 #mv
LOWER_ORP_THRESHOLD = 200 #mv
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

#Time elapsed since last abnormal state
gTimeElapsedFromAbnormalState = 0

def circulate():
    print("Circulating")

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
def heaterControl(command)
    print("Heater control")

#Get gFeedingTankWaterLevel and gFilteringTankWaterLevel
def waterLevelDetection():
    print("Water level detection")

#Turn on/off motors in feeding/filtering tank
def motorControl(feedingMotorCommand, filteringMotorCommand)
    print("Motor control")

#Turn/off filling motor
def fillingMotorControl(command)
    print("Filling Motor Control")
    waterLevelDetection()

#Turn on/off electrical Door
def electricalMagneticDoor(command)
    print("Electrical magnetic door")

def waterLevelJudgementFirstStepInCirculation():
    if gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 2:
        motorControl(0, 0)
        electricalMagneticDoor(1)
    elif gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 0 and gFilteringTankWaterLevel = 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel = 0 and gFilteringTankWaterLevel = 1:
        motorControl(0, 1)
    else:
        motorControl(0, 0)
        fillingMotorControl(1)

def waterLevelJudgementSecondStepInCirculation():
    if gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 2:
        motorControl(0, 0)
        electricalMagneticDoor(1)
    elif gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 1:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 2 and gFilteringTankWaterLevel = 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 1:
        motorControl(0, 0)
    elif gFeedingTankWaterLevel = 1 and gFilteringTankWaterLevel = 0:
        motorControl(1, 0)
    elif gFeedingTankWaterLevel = 0 and gFilteringTankWaterLevel = 2:
        motorControl(0, 1)
    elif gFeedingTankWaterLevel = 0 and gFilteringTankWaterLevel = 1:
        motorControl(0, 1)
    else:
        motorControl(0, 0)
        fillingMotorControl(1)

def operation():
    waterLevelDetection()
    waterLevelJudgementFirstStepInCirculation()

def main():
    print("Aqua Botanical System!")
    operation()

if __name__ == "__main__":
    main()
