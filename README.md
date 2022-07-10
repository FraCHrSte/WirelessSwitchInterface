# Wireless Switch Interface

700.496	Research Project in Pervasive Computing
Project	Wireless switch interface
Date		17.05.2022
Version	1.0

Wireless Radio Switch Interface for Radio Controlled Switch based on RFM69 and raspberry 

# Hardware: 

- Raspbarry pi 1.0
- RFM69 

The project inculdes a pcb board file for the producing a test board. This file is created by the pcb program eagle V16
The File in the directory hardware. 

RFM pin	Pi pin
3V3	    17
DIO0	  18 (GPIO24)
MOSI	  19
MISO	  21
CLK	    23
NSS	    24 (CE0)
Ground	25
RESET	  22 (GPIO25)



# Software: 

Main repo
https://github.com/FraCHrSte/WirelessSwitchInterface.git



# Using

Start program: 
Goto  application folder "/apps"
Start with command: "./simplercpulse.py"
