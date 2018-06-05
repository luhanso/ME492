# Lucas Hanson - Week 4 Day 1 - Assignment 1

import RPi.GPIO as GPIO
import time

pin_num = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num,GPIO.OUT)

switch1 = 27
GPIO.setup(switch1,GPIO.IN,pull_up_down=GPIO.PUD_UP)

switch2 = 21
GPIO.setup(switch2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

duty = 50

pwm_led = GPIO.PWM(pin_num,500)
pwm_led.start(duty)
i=1

while i > 0:
	if GPIO.input(switch1) == False:
		while duty < 100:
			print("Increase Duty Cycle")
			duty = duty+5
			pwm_led.ChangeDutyCycle(duty)
			time.sleep(0.2)
	elif GPIO.input(switch2) == False:
		while duty > 0:
			print("Decrease Duty Cycle")
			duty = duty-5
			pwm_led.ChangeDutyCycle(duty)
			time.sleep(0.2)
