import RPi.GPIO as GPIO
import time

ServoPwm = 22 # pin 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(ServoPwm, GPIO.OUT)

servo = GPIO.PWM(ServoPwm, 50) # GPIO 22 with 50hz 

servo.start(5)
time.sleep(10)

servo.stop()
GPIO.cleanup()
