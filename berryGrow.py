#!/usr/bin/python

import RPi.GPIO as GPIO
import pprint
from conf.machinesConf import *
from conf.machinesStatus import *
from lib.Machine import *



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

machines = []
#pprint.pprint(machinesStatus)
for (i, mConf) in enumerate( machinesConf ):
    if( mConf['enabled'] == True ):
        machines.append( Machine( mConf, machinesStatus[i] ) )



while True:
    schedule.run_pending()
    time.sleep(1)
