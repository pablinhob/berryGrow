#!/usr/bin/python
import os
import RPi.GPIO as GPIO
import os.path, time
import pprint
import json
#from conf.machinesConf import *
#from conf.machinesStatus import *
from lib.Machine import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

pathMachinesConf = CURRENT_PATH + '/conf/machinesConf.json'
pathMachinesStatus = CURRENT_PATH + '/conf/machinesStatus.json'

machines = []

def updateMachines():
    try:
        machinesConf = json.loads( open( pathMachinesConf ).read() )
        machinesStatus = json.loads( open( pathMachinesStatus ).read() )
    except ValueError:
        print "Error reading JSON"
    else:
        for (i, mConf) in enumerate( machinesConf ):
            if( mConf['enabled'] == True ):
                machines.append( Machine( mConf, machinesStatus[i] ) )




confLastUpdate = False
statusLastUpdate = False

while True:

    dateUpdateConf = os.path.getmtime( pathMachinesConf )
    dateUpdateStatus = os.path.getmtime( pathMachinesStatus )
    #print time.ctime( dateUpdateConf )
    #print time.ctime( confLastUpdate )
    if(
        dateUpdateConf > confLastUpdate or
        dateUpdateStatus > statusLastUpdate or
        confLastUpdate == False
    ):
        confLastUpdate = dateUpdateConf
        statusLastUpdate = dateUpdateStatus
        schedule.clear()
        updateMachines()
        print "changes!!"


    schedule.run_pending()
    time.sleep(1)
