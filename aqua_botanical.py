#Aqua Botanical System
#Author: Barry Hao, Tony Tsai
#Multi thread?
#Defition of the water level?

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
gFeedingTankWaterLevel = None
gFilteringTankWaterLevel = None
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

#Get gFeedingTankWaterLevel and gFilteringTankWaterLevel
def waterLevelDetection():
    print("Water level detection")

def operation():
    waterLevelDetection()
    waterLevelJudgement()

def main():
    print("Aqua Botanical System!")
    operation()

if __name__ == "__main__":
    main()
