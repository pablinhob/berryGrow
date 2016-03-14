#!/usr/bin/python

import RPi.GPIO as GPIO
import schedule
import time
import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

conf = [
  {
    'name': 'Growing room',
    'enabled': True,
    'pins' :{ 'fan_extraction':19, 'lamp':7 },
    'timer': {'day': '21:00', 'night':'9:00'}
  },
  {
    'name': 'Flowering room',
    'Enabled': False,
    'pins':{ 'fan_extraction':19, 'lamp':7 },
    'timer': {'day':'21:00', 'night':'9:00'}
  }
]

status = [
  {
   'day': {
    'fan_extraction_power':90,
    'fan_inside_power':70,
    'air_pump': True
   },
   'night': {
    'fan_extraction_power':20,
    'fan_inside_power':10,
    'air_pump': False
   }
  }
]

# PINS
pin_ventilador = 19
pin_lampara = 22

GPIO.setup(pin_lampara ,GPIO.OUT)
GPIO.setup(pin_ventilador, GPIO.OUT)


pwm_ventilador = GPIO.PWM( pin_ventilador , 100)
pwm_ventilador.start(0)

potencia_ventilador_dia = 30
potencia_ventilador_noite = 100
hora_encendido = "12:00"
hora_apagado = "21:00"


def start():
	now = datetime.datetime.now()
	encendido = now.replace(hour= int(hora_encendido.split(':')[0]), minute=int(hora_encendido.split(':')[1]) )
	apagado = now.replace(hour= int(hora_apagado.split(':')[0]), minute=int(hora_apagado.split(':')[1]) )

	if(encendido <= now and apagado <= now):
		if(apagado > encendido):
			encendido = encendido + datetime.timedelta(days=1)
		else:
			apagado = apagado + datetime.timedelta(days=1)


	if( now >= encendido and now <= apagado):
		luzAcender()
	else:
		luzApagar()

def luzAcender():
        GPIO.output( pin_lampara ,GPIO.LOW)
        pwm_ventilador.ChangeDutyCycle(potencia_ventilador_dia)
	print "Luz Acendida"

def luzApagar():
	GPIO.output( pin_lampara ,GPIO.HIGH)
	pwm_ventilador.ChangeDutyCycle(potencia_ventilador_noite)
	print "Luz apagada"



start()
schedule.every().day.at( hora_encendido ).do( luzAcender )
schedule.every().day.at( hora_apagado ).do( luzApagar )


while True:
    schedule.run_pending()
    time.sleep(1)
