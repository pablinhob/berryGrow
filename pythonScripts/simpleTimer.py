#!/usr/bin/python

import RPi.GPIO as GPIO
import schedule
import time
import datetime





machinesConf = [
  # Grow room
  {
    'name': 'Growing room',
    'enabled': True,
    'pins' :{
        'fan_extraction':19,
        'fan_intraction': False,
        'fan_room': False,
        'lamp':7
    },
    'timer': {'day': '21:00', 'night':'9:00'}
  },
  # Flowering room
  {
    'name': 'Flowering room',
    'Enabled': False,
    'pins' :{
        'fan_extraction':21,
        'fan_intraction': False,
        'fan_room': False,
        'lamp':8
    },
    'timer': {'day':'21:00', 'night':'9:00'}
  }
]

machinesStatus = [
  # Grow room
  {
   'day': {
    'fan_extraction':90, #Fan power
    'air_pump': True
   },
   'night': {
    'fan_extraction':20, #Fan power
    'air_pump': False
   }
  },
  # Flowering room
  {
   'day': {
    'fan_extraction':40, #Fan power
    'air_pump': True
   },
   'night': {
    'fan_extraction':20, #Fan power
    'air_pump': False
   }
  }
]






class Machine:

    conf = False
    status = False

    pwm_fan_extraction = False

    def __init__( self, conf, status):
        self.setConf( conf )
        self.setStatus( status )
        self.setPins()
        self.start()

    def setConf( self, conf ):
        self.conf = conf

    def setStatus( self, status):
        self.status = status

    def setPins( self ):
        GPIO.setup( self.conf.['pins']['lamp'] ,GPIO.OUT)
        GPIO.setup( self.conf.['pins']['fan_extraction'] ,GPIO.OUT)

        # set fans PWM
        self.pwm_fan_extraction = GPIO.PWM( self.conf.['pins']['fan_extraction'] , 100)
        self.pwm_fan_extraction.start(0)

    def start( self ):
    	now = datetime.datetime.now()
    	encendido = now.replace(hour= int(hora_encendido.split(':')[0]), minute=int(hora_encendido.split(':')[1]) )
    	apagado = now.replace(hour= int(hora_apagado.split(':')[0]), minute=int(hora_apagado.split(':')[1]) )

    	if(encendido <= now and apagado <= now):
    		if(apagado > encendido):
    			encendido = encendido + datetime.timedelta(days=1)
    		else:
    			apagado = apagado + datetime.timedelta(days=1)

    	if( now >= encendido and now <= apagado):
    		self.isDay()
    	else:
    		self.isNight()

        schedule.every().day.at( hora_encendido ).do( self.isDay )
        schedule.every().day.at( hora_apagado ).do( self.isNight )


    def isDay( self ):
        GPIO.output( self.conf.['pins']['lamp'] ,GPIO.HIGH)
        self.pwm_fan_extraction.ChangeDutyCycle( self.conf.['day']['fan_extraction'] )
    	print "Luz Acendida"

    def isNight( self ):
    	GPIO.output( self.conf.['pins']['lamp'] ,GPIO.LOW)
    	self.pwm_fan_extraction.ChangeDutyCycle( self.conf.['night']['fan_extraction'] )
    	print "Luz apagada"




#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

machines = []

for (i, mConf) in enumerate( machinesConf ):
    machine[i] = new Machine( mConf, machinesStatus[i] )



while True:
    schedule.run_pending()
    time.sleep(1)
