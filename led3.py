import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)  
GPIO.setup(17, GPIO.OUT)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

i = .05
ii = 15
while ii > 0:

#####
	GPIO.output(4, GPIO.LOW)  
	GPIO.output(4, GPIO.HIGH)  
	GPIO.output(18, GPIO.LOW)  
	#GPIO.output(18, GPIO.HIGH)  
	GPIO.output(17, GPIO.LOW)  
	#GPIO.output(17, GPIO.HIGH)  

	GPIO.output(27, GPIO.LOW)  
	GPIO.output(27, GPIO.HIGH)  
	GPIO.output(22, GPIO.LOW)  
	#GPIO.output(22, GPIO.HIGH)  
	GPIO.output(23, GPIO.LOW)  
	#GPIO.output(23, GPIO.HIGH)  
	time.sleep(i)
	ii = ii - 1.
########################
#####
	GPIO.output(4, GPIO.LOW)  
	#GPIO.output(4, GPIO.HIGH)  
	GPIO.output(18, GPIO.LOW)  
	GPIO.output(18, GPIO.HIGH)  
	GPIO.output(17, GPIO.LOW)  
	#GPIO.output(17, GPIO.HIGH)  

	GPIO.output(27, GPIO.LOW)  
	GPIO.output(27, GPIO.HIGH)  
	GPIO.output(22, GPIO.LOW)  
	#GPIO.output(22, GPIO.HIGH)  
	GPIO.output(23, GPIO.LOW)  
	#GPIO.output(23, GPIO.HIGH)  
	time.sleep(i)
	ii = ii - 1.
########################

GPIO.cleanup()
