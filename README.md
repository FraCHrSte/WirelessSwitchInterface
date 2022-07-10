# Wireless Switch Interface

- 700.496	Research Project in Pervasive Computing
- Project	Wireless switch interface
- Date		17.05.2022, Version	1.0

Wireless Radio Switch Interface for Radio Controlled Switch based on RFM69 and raspberry 

# Hardware: 

- Raspbarry pi 1.0
- RFM69 

The project inculdes a pcb board file for the producing a test board. This file is created by the pcb program eagle V16
The File in the directory hardware. 

The connection between the RFM69 and the raspberry pi is made as follows:

| RFM69 pin | RaspPi pin  
| ------- |-------
| 3V3     | 17  
| DIO0    | 18  
| MOSI    | 19  
| MISO    | 21  
| CLK     | 23  
| NSS     | 24   
| Ground  | 25  
| RESET   | 22   



# Software: 

Main repo
* https://github.com/WirelessSwitchInterface/software

External library
* https://github.com/etrombly/RFM69

The following Python packages must be installed for the Raspberry Pi:

* RPi.GPIO
* spidev

Be sure to enable the SPI interface on your GPIO header using either the command `raspi-config`

Then reboot the system in any case.


# Usage

- Start program: 
- Goto  application folder " cd /apps"
- Start with command: "./simplercpulse.py"
