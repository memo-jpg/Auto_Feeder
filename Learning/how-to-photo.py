from picamera import PiCamera

camera = PiCamera()
time.sleep(2)

camera.capture("/home/pi/Pictures/img.jpg")
print("Done.")


#How to customize the pictures taken
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720) #changes the resolution of the pictures you take
camera.vflip = True #vertical flip of the image
camera.contrast = 10
camera.image_effect = "watercolor" #Premade effects to use on pictures; similar to filters
time.sleep(2)

camera.capture("/home/pi/Pictures/img.jpg")
print("Done.")
