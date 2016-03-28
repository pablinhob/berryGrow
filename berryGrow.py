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

pathMachinesConf = os.getcwd()+'/conf/machinesConf.json')
pathMachinesStatus = os.getcwd()+'/conf/machinesStatus.json')

machines = []

def updateMachines():
    machinesConf = json.loads( open( pathMachinesConf ).read() )
    machinesStatus = json.loads( open( pathMachinesStatus ).read() )

    for (i, mConf) in enumerate( machinesConf ):
        if( mConf['enabled'] == True ):
            machines.append( Machine( mConf, machinesStatus[i] ) )



confLastUpdate = False
statusLastUpdate = False

while True:

    dateUpdateConf = time.ctime( os.path.getmtime( pathMachinesConf ) )
    dateUpdateStatus = time.ctime( os.path.getmtime( pathMachinesStatus ) )

    if(
        dateUpdateConf > confLastUpdate ||
        dateUpdateStatus > statusLastUpdate ||
        confLastUpdate == False
    ):
        confLastUpdate = dateUpdateConf
        statusLastUpdate = dateUpdateStatus
        schedule.clear()
        updateMachines()


    schedule.run_pending()
    time.sleep(1)
