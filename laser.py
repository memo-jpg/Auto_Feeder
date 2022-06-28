import RPi.GPIO as GPIO
import time

laser = 27 # pin 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(laser, GPIO.OUT)


GPIO.output(laser, GPIO.LOW)
time.sleep(10)
GPIO.output(laser, GPIO.HIGH)

GPIO.cleanup()
