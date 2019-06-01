#!/bin/bash
now=$(date +"%m_%d_%Y")
mkdir /home/pi/Desktop/sensor_data/$now
touch /home/pi/Desktop/sensor_data/$now/salt
touch /home/pi/Desktop/sensor_data/$now/oxygen
touch /home/pi/Desktop/sensor_data/$now/ph
touch /home/pi/Desktop/sensor_data/$now/temperature
touch /home/pi/Desktop/sensor_data/$now/orp
