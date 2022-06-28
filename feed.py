import time
import RPi.GPIO as GPIO


servo_power = 17
servo_channel = 27
servo_signal = 22
laser = 18

def power_on():
    GPIO.output(servo_power, GPIO.LOW)

def power_off():
    GPIO.output(servo_power, GPIO.HIGH)

def laser_dance():
    power_on()

    time.sleep(.1)
    GPIO.output(servo_channel, GPIO.HIGH) #channel is correct
    GPIO.output(laser, GPIO.LOW)

    for i in range(4):
        signal.ChangeDutyCycle(10)
        time.sleep(.25)
        signal.ChangeDutyCycle(12)
        time.sleep(1)

    signal.ChangeDutyCycle(8)
    time.sleep(.25)
    signal.ChangeDutyCycle(12)
    time.sleep(1)
    signal.ChangeDutyCycle(0)

    GPIO.output(laser, GPIO.HIGH)
    power_off()

def feed():
    power_on()
    GPIO.output(servo_channel, GPIO.LOW) #now controlls feed servo

    time.sleep(.1)
    signal.ChangeDutyCycle(10)
    time.sleep(2)
    signal.ChangeDutyCycle(2.5)
    time.sleep(1)
    signal.ChangeDutyCycle(0)



GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_power, GPIO.OUT)
GPIO.setup(servo_channel, GPIO.OUT)
GPIO.setup(servo_signal, GPIO.OUT)
GPIO.setup(laser, GPIO.OUT)

GPIO.output(servo_power, GPIO.HIGH) #set to off
GPIO.output(servo_channel, GPIO.LOW) #set to control the laser servo in high
GPIO.output(laser, GPIO.HIGH)

signal = GPIO.PWM(servo_signal, 50) #setting servo_signal to 50Hz

signal.start(0) #starting the servo with 0 control pulse

feed()

GPIO.cleanup()
