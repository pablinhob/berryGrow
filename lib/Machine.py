import RPi.GPIO as GPIO
import time
import datetime
import schedule
import pprint

class Machine:

    conf = False
    status = False

    pwm_fan_extraction = False
    pwm_fan_intraction = False
    pwm_fan_room = False

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
        GPIO.setup( self.conf['pins']['lamp'] ,GPIO.OUT)
        GPIO.setup( self.conf['pins']['fanExtraction'] ,GPIO.OUT)

        # set fans PWM
        if( self.conf['pins']['fanExtraction'] != False ):
            self.pwm_fan_extraction = GPIO.PWM( self.conf['pins']['fanExtraction'] , 100)
            self.pwm_fan_extraction.start(0)
        if( self.conf['pins']['fanIntraction'] != False ):
            self.pwm_fan_intraction = GPIO.PWM( self.conf['pins']['fanIntraction'] , 100)
            self.pwm_fan_intraction.start(0)
        if( self.conf['pins']['fanRoom'] != False ):
            self.pwm_fan_room = GPIO.PWM( self.conf['pins']['fanRoom'] , 100)
            self.pwm_fan_room.start(0)


    def start( self ):

        turn_on_hour = self.status['day']['timer']
        turn_off_hour = self.status['night']['timer']

    	now = datetime.datetime.now()
    	encendido = now.replace(hour= int(turn_on_hour.split(':')[0]), minute=int(turn_on_hour.split(':')[1]) )
    	apagado = now.replace(hour= int(turn_off_hour.split(':')[0]), minute=int(turn_off_hour.split(':')[1]) )

    	if(encendido <= now and apagado <= now):
    		if(apagado > encendido):
    			encendido = encendido + datetime.timedelta(days=1)
    		else:
    			apagado = apagado + datetime.timedelta(days=1)

    	if( now >= encendido and now <= apagado):
    		self.isDay()
    	else:
    		self.isNight()

        schedule.every().day.at( turn_on_hour ).do( self.isDay )
        schedule.every().day.at( turn_off_hour ).do( self.isNight )


    def isDay( self ):
        if( self.conf['pins']['lamp'] != False ):
            GPIO.output( self.conf['pins']['lamp'] ,GPIO.LOW)

        if( self.conf['pins']['pump'] != False ):
            if( self.status['day']['pump'] == True ):
                GPIO.output( self.status['day']['pump'] , GPIO.LOW)
            else:
                GPIO.output( self.status['day']['pump'] , GPIO.HIGH)

        # FANS
        if( self.pwm_fan_extraction != False ):
    	   self.pwm_fan_extraction.ChangeDutyCycle( self.status['day']['fanExtraction'] )
        if( self.pwm_fan_intraction != False ):
    	   self.pwm_fan_intraction.ChangeDutyCycle( self.status['day']['fanIntraction'] )
        if( self.pwm_fan_room != False ):
    	   self.pwm_fan_room.ChangeDutyCycle( self.status['day']['fanRoom'] )

    	print self.conf['name'] +": Light ON"

    def isNight( self ):
        #pprint.pprint(self.status)
        if( self.conf['pins']['lamp'] != False ):
            GPIO.output( self.conf['pins']['lamp'] ,GPIO.HIGH)

        if( self.conf['pins']['pump'] != False ):
            if( self.status['day']['pump'] == True ):
                GPIO.output( self.status['night']['pump'] , GPIO.LOW)
            else:
                GPIO.output( self.status['night']['pump'] , GPIO.HIGH)

        # FANS
        if( self.pwm_fan_extraction != False ):
    	   self.pwm_fan_extraction.ChangeDutyCycle( self.status['night']['fanExtraction'] )
        if( self.pwm_fan_intraction != False ):
    	   self.pwm_fan_intraction.ChangeDutyCycle( self.status['night']['fanIntraction'] )
        if( self.pwm_fan_room != False ):
    	   self.pwm_fan_room.ChangeDutyCycle( self.status['night']['fanRoom'] )

    	print self.conf['name'] +": Light OFF"
