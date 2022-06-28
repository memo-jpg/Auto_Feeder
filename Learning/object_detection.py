import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np


#we create trackbars to help us with selecting a color
def nothing(x):
    pass
 
cv2.namedWindow("Trackbars")

#To create the trackbars, we have the 'cv2.createTrackbar()' function. It takes 5 arguments:
	#The trackbar name
	#The window name to which it is attached
	#The default value
	#The maximum value
	#The callback function executed every time trackbar value changes 
		#The callback function always has a default argument, which is the trackbar position.
		#In our case, the function does nothing, so we will simply pass.

#We're going to create 3 trackbars for blue, green, and red.
#Each trackbar will have a default value of 0 and a max of 255; they will be attached to the window named "Trackbars"
cv2.createTrackbar("B", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("R", "Trackbars", 0, 255, nothing)

#Setting up the Raspberry Pi Camera
camera = PiCamera()
camera.resolution = (640, 480) #640x480
camera.framerate = 30

#PiRGBArray
	#avoids conversion from Jpg to OpenCV format; saves time
#takes 2 arguments:
	#camera object
	#resolution
rawCapture = PiRGBArray(camera, size=(640, 480))

#We're going to use the 'capture_continuous' function to start reading the frames from the camera module

#The capture_continuous function takes three arguments:
	#rawCapture
	#The format in which we want to read each frame. Since OpenCV expects the image to be in the BGR format rather than the RGB, we need to specify the format to be BGR.
	#The 'use_video_port' boolean. Making this true means that we treat the stream as video.

#Once we have the frame, we can access the raw NumPy array via the .array attribute. 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

#Setting up the Color Recognition

#Now we are going to convert images from the BGR to the HSV color space. The HSV (hue saturation value) space gives us better results when doing color-based segmentation.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV

#Next, we create the trackbars used to select the color.
    B = cv2.getTrackbarPos("B", "Trackbars")
    G = cv2.getTrackbarPos("G", "Trackbars")
    R = cv2.getTrackbarPos("R", "Trackbars")

#After that, we can find out the lower and upper limit of the color in HSV
    green = np.uint8([[[B, G, R]]])
    hsvGreen = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    lowerLimit = np.uint8([hsvGreen[0][0][0]-10,100,100])
    upperLimit = np.uint8([hsvGreen[0][0][0]+10,255,255])

#Next, we adjust the threshold of the HSV image for a range of each selected color.
    mask = cv2.inRange(hsv, lowerLimit, upperLimit)

#Now we can extract the objects of the colors in the frame.
    result = cv2.bitwise_and(image  , image , mask=mask)

#Now, the program can detect the objects that contain the colors you set.

#Let's show the result in the output window.
    cv2.imshow("frame", image)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    key = cv2.waitKey(1)

#Always clear the stream in prepartation for the next frame by calling truncate(0) between captures.
    rawCapture.truncate(0)

    if key == 27:
        break

cv2.destroyAllWindows()
