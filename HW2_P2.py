# Lucas Hanson - Homework 2 - Problem 2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 17
led2 = 27
led3 = 22

but1 = 5
but2 = 6
but3 = 13
but4 = 12

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)

GPIO.setup(but1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(but2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(but3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(but4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.output(led1,False)
GPIO.output(led2,False)
GPIO.output(led3,False)

print("Push any of the 4 buttons")

try:
	while True:
		if GPIO.input(but1) == False:
			GPIO.output(led1,True)
			GPIO.output(led2,False)
			GPIO.output(led3,False)
		elif GPIO.input(but2) == False:
			GPIO.output(led1,True)
			GPIO.output(led2,True)
			GPIO.output(led3,False)
		elif GPIO.input(but3) == False:
			GPIO.output(led1,True)
			GPIO.output(led2,True)
			GPIO.output(led3,True)
		elif GPIO.input(but4) == False:
			GPIO.output(led1,False)
			GPIO.output(led2,False)
			GPIO.output(led3,False)
			
finally:
	print("Cleaning Up")
	GPIO.cleanup()
	

