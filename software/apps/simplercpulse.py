#!/usr/bin/env python
##############################################################
# 700.496	Research Project in Pervasive Computing
# Project	Wireless switch interface
# date		17.05.2022
# Version	1.0
##############################################################
# description
# The source code was kept very simple for implementation in a uC. The main output of the code is to initialize the RFM69 module and decode RC switch codes. 
# After decoding, a corresponding command is executed, for example 
# ID: 83029 --> light on
# ID: 83028 --> light off
# ID: 86101 --> light brighter
# ID: 86100 --> light darker

from raspyrfm import *					# library raspyrfm from github
import sys						# library sys
import time						# libraray time			

module = 1						# set 1 module
RFM69 = True						# set RFM69 True
frequency = 433.92					# setup frequency
radio = RaspyRFM(module, RFM69)				# create RaspyRFM
radio.set_params(					# setup radio parameter
                        Freq = frequency,            	# MHz
                        Bandwidth = 500,             	# kHz
                        SyncPattern = [],		# pattern
                        RssiThresh = -105,           	# dBm
                        ModulationType = rfm69.OOK,	# OOK
                        OokThreshType = 1,           	# peak thresh
                        OokPeakThreshDec = 3,		# Treshold
                        Preamble = 0,			# preamble	
                        TxPower = 13			# Tx Power
                )

time.sleep(0.5)						# sleep time
bit = False						# default bit
cnt = 1							# init counter
train = []                 				# bit train 
state = 0						# decoding state
rx32bit = ""						# string 
cntone = 0						# counter bit 1
cntzero = 0						# counter bit 0
cntproto = 0						# counter protocol
try:							# try loop
    while True:						# main while loop
     rx32bit = ""					# init string
     cnt = 1						# init counter 
     state = 0						# init state
     value = radio.receive(64)				# read 64 bytes 
     for b in value[0]:					# for loop for decoding bits
      mask = 0x80					# mask for reading bit
      while mask != 0:					# loop for each bit
        newbit = (b & mask) != 0			# extract bit
        mask >>= 1					# shift mask to next bit
        if state == 0:         				# find sync bit 1000000000000000000000
         if newbit == bit:				# check zero bit
          cnt += 1 					# count zero
         else:						# else
          train *= 0					# reset train
          cnt = 1					# reset counter 
         if cnt == 55:         				# check counter = 55 zeros
          state = 1					# sync bits detected next state
          cnt = 1					# reset count
          rx32bit = ""					# reset string
        if state == 1:         				# decode bit sequence 10000,11110 
           if len(train) < 220:				# max. size
            train.append('X')				# add XX
            if newbit == True: 				# check bit == 1
             cntone += 1				# increment count one
             cntzero = 0				# reset count zero
            else:					# else
             cntzero += 1  				# increment count zero
             cntone = 0					# reset count one
            if cntone > 3: 				# check bit is one
             rx32bit = rx32bit.__add__("1")		# add string 1
             cntone = 0					# reset
             cntproto += 1				# increment count protocol 
            if cntzero > 3:				# check bit is zero 
             rx32bit = rx32bit.__add__("0")		# add string zero
             cntzero = 0				# reset count zero
             cntproto += 1				# increment count protocol
           else:					# else
            if cntproto > 20:				# check protocol counter > 20
             rx32bit = rx32bit[4:24]			# extract from 4 to 24
             prototyp = rx32bit[:4]			# decode device 
             if prototyp == "0001":			# check ID 0001
              rxdec = int(rx32bit,2)			# convert to integer value
              if rxdec == 83029:			# check for code light on
		print("light on")			# print light on	
	      if rxdec == 83028:			# check for code light off
		print("light off")			# print light off
	      if rxdec == 86101:			# check for code light brighter
		print("light brighter")			# print light brighter
	      if rxdec == 86100:			# check for code light darker
		print("light darker")			# print light darker 
            state = 3					# set state to 3
            train *= 0 					# reset train
except KeyboardInterrupt:				# stop with keyboardinterrupt
    pass						# pass

print("end")						# end code

