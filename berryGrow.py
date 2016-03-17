#!/usr/bin/python

import RPi.GPIO as GPIO
import schedule
import time
import datetime
import pprint
import conf/machinesConf
import conf/machinesStatus
import lib/Machine


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

machines = []

for (i, mConf) in enumerate( machinesConf ):
    if( mConf['enabled'] == True ):
        machines.append( Machine( mConf, machinesStatus[i] ) )



while True:
    schedule.run_pending()
    time.sleep(1)
