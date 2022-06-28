import time
import RPi.GPIO as GPIO
import cv2 as cv


minimum_commutative_image_diff = 1
servo_power = 17
servo_channel = 27
servo_signal = 22
laser = 18

def get_image_difference(image_1, image_2):
    first_image_hist = cv.calcHist([image_1], [0], None, [256], [0,256])
    second_image_hist = cv.calcHist([image_2], [0], None, [256], [0,256])

    img_hist_diff = cv.compareHist(first_image_hist, second_image_hist, cv.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv.matchTemplate(first_image_hist, second_image_hist, cv.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match

    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff

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
    power_off() #maybe need?



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

#time.sleep(1)
#laser_dance()
#time.sleep(1)
#feed()
#time.sleep(1)

#GPIO.cleanup()

# Compare Images
#image_1 = cv.imread('/home/pi/Resume_Project/Photos/image.jpg')
image_1 = cv.imread('/home/pi/Resume_Project/Photos/class.jpg')
image_2 = cv.imread('/home/pi/Resume_Project/Photos/class2.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/class_food.jpg')


#image_2 = cv.imread('/home/pi/Resume_Project/Photos/image4.jpg')

# just testing different images
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/image2.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/image3.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/cat.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/empty_dog-bowl.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/light-diff.jpg')
#image_2 = cv.imread('/home/pi/Resume_Project/Photos/light-different.jpg')
image_diff = get_image_difference(image_1, image_2)

if image_diff < minimum_commutative_image_diff:
    print('Matched')
    # Put the feed function in here
    time.sleep(1)
    laser_dance()
    time.sleep(1)
    feed()
    time.sleep(1)

    GPIO.cleanup()
else:
    print('Not Matched')

