from __future__ import print_function
import sys
import RPi.GPIO as GPIO
import spidev
import threading
import time

FXOSC = 32E6
FSTEP = FXOSC / (1<<19)

# Raspberry RFM Module connection
# RaspyRFM single module
# Connect to pins 17-26 on raspberry pi
#--------------------------------#
#Raspi|Raspi|Raspi|RFM69|RaspyRFM#
#Name |GPIO |Pin  |Name |PCB Pin #
#--------------------------------#
#3V3  |  -  | 17  |3.3V |   1    #
# -   | 24  | 18  |DIO1 |   2    # only when PCB jumper closed
#MOSI | 10  | 19  |MOSI |   3    #
#GND  |  -  | 20  |GND  |   4    #
#MISO |  9  | 21  |MISO |   5    #
# -   | 25  | 22  |DIO0 |   6    #
#SCKL | 11  | 23  |SCK  |   7    #
#CE0  |  8  | 24  |NSS  |   8    #
#CE1  |  7  | 26  |DIO2 |   10   # only when PCB jumper closed
#--------------------------------#

# RaspyRFM twin module with 10-pin connector
# Connect to pins 17-26 on raspberry pi
#---------------------------------#
#Raspi|Raspi|Raspi|RFM69 |RaspyRFM#
#Name |GPIO |Pin  |Name  |PCB Pin #
#---------------------------------#
#3V3  | -   | 17  |3.3V  |   1    #
#  -  | 24  | 18  |DIO0_2|   2    #
#MOSI | 10  | 19  |MOSI  |   3    #
#GND  |  -  | 20  |GND   |   4    #
#MISO | 9   | 21  |MISO  |   5    #
# -   | 25  | 22  |DIO0_1|   6    #
#SCKL | 11  | 23  |SCK   |   7    #
#CE0  | 8   | 24  |NSS1  |   8    #
#CE1  | 7   | 26  |NSS2  |   10   #
#---------------------------------#
