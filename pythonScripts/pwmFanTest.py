#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
  
GPIO.setmode(GPIO.BCM)  
  
GPIO.setup(19, GPIO.OUT) 
  
white = GPIO.PWM(19, 100)  
  
white.start(0)          
  
  
pause_time = 0.1       
  
try:
    while True:
        for i in range(0,100):
            white.ChangeDutyCycle(100-i)  
            sleep(pause_time)        
	white.ChangeDutyCycle(i)
	sleep(8)
  
except KeyboardInterrupt:
    white.stop()
    GPIO.cleanup()
