# Lucas Hanson - Homework 2 - Problem 1

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 17
led2 = 27
led3 = 22

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)

try:
	while True:
		GPIO.output(led1,False)
		GPIO.output(led2,False)
		GPIO.output(led3,False)
		selection = int(input("Please enter a number between 1 and 3: "))
		if selection == 1:
			GPIO.output(led1,True)
			time.sleep(5.0)
		elif selection == 2:
			GPIO.output(led1,True)
			GPIO.output(led2,True)
			time.sleep(5.0)
		elif selection == 3:
			GPIO.output(led1,True)
			GPIO.output(led2,True)
			GPIO.output(led3,True)
			time.sleep(5.0)
		elif selection > 3:
			print("Error, number out of range")	
		elif selection < 1:
			print("Error, number out of range")
			
finally:
	print("Cleaning Up")
	GPIO.cleanup()
	
