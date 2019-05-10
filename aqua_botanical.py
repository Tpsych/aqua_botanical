#Aqua Botanical System
#Author: Barry Hao

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
gFeedingTankMotor = False
gFilteringTankMotor = False
gWaterFillingMotor = False

#Electrical Magnetic Door
gElectricalMagneticDoor = False

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

def operation():
    if gFeedingTankWaterLevel > FEEDING_TANK_WATER_HIGH_LEVEL and \
    gFilteringTankWaterLevel > FILTERING_TANK_WATER_HIGH_LEVEL:
        gFeedingTankMotor = False
        gFilteringTankMotor = False
        gWaterFillingMotor = True

def main():
    print("Aqua Botanical System!")
    if gORP > LOWER_ORP_THRESHOLD:
        if gORP > HIGH_ORP_THRESHOLD:
            operation()
        else:
            circulate()

if __name__ == "__main__":
    main()
