#!/usr/bin/python

import RPi.GPIO as GPIO
import schedule
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

hora_encendido = "21:00"
hora_apagado = "9:00"


def arrancar():
	now = datetime.datetime.now()	
	encendido = now.replace(hour= int(hora_encendido.split(':')[0]), minute=int(hora_encendido.split(':')[1]) )
	apagado = now.replace(hour= int(hora_apagado.split(':')[0]), minute=int(hora_apagado.split(':')[1]) ) 

	if(encendido <= now and apagado <= now):
		if(apagado > encendido):
			encendido = encendido + datetime.timedelta(days=1)
		else:
			apagado = apagado + datetime.timedelta(days=1)
			
        print now
        print encendido
        print apagado		

	if( now >= encendido and now <= apagado):
		luzAcender()
	else:
		luzApagar()

def luzAcender():
	#GPIO.output(7,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
	print "Luz Acendida"
def luzApagar():
#	GPIO.output(7,GPIO.LOW)
	GPIO.output(7,GPIO.HIGH)
	print "Luz apagada"



arrancar()
schedule.every().day.at( hora_encendido ).do( luzAcender )
schedule.every().day.at( hora_apagado ).do( luzApagar )


while True:
    schedule.run_pending()
    time.sleep(1)

