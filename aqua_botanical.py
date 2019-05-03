#Aqua Botanical System
#Author: Barry Hao

#Constant
FEEDING_TANK_WATER_HIGH_LEVEL = 200
FEEDING_TANK_WATER_MID_LEVEL = 150
FEEDING_TANK_WATER_LOW_LEVEL = 100
FILTERING_TANK_WATER_HIGH_LEVEL = 200
FILTERING_TANK_WATER_MID_LEVEL = 150
FILTERING_TANK_WATER_LOW_LEVEL = 100
ORP_THRESHOLD_1 = 250 #mv
ORP_THRESHOLD_1 = 200 #mv
ABNORMAL_TIME_LIMIT = 5 #minute

#Read from sensors
gFeedingTankWaterLevel = None
gFilteringTankWaterLevel = None
gORP = None

#Motor Boolean
gFeedingTankMotor = False
gFilteringTankMotor = False
gWaterFillingMotor = False

#Electrical Magnetic Door
gElectricalMagneticDoor = False

#Time elapsed since last abnormal state
gTimeElapsedFromAbnormalState = 0

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
