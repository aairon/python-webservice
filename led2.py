import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)  
GPIO.setup(17, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

i = .15
ii = 25
while ii > 0:

	GPIO.output(18, GPIO.HIGH)  
	time.sleep(i)
	GPIO.output(17, GPIO.HIGH)
	time.sleep(i)

	GPIO.output(18, GPIO.HIGH)  
	time.sleep(i)
	GPIO.output(17, GPIO.LOW)
	time.sleep(i)

	GPIO.output(18, GPIO.LOW)  
	time.sleep(i)
	GPIO.output(17, GPIO.HIGH)
	time.sleep(i)

	GPIO.output(18, GPIO.LOW)  
	time.sleep(i)
	GPIO.output(17, GPIO.LOW)
	time.sleep(i)
	ii = ii - 1

GPIO.cleanup()
