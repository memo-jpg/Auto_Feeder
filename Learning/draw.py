import cv2 as cv
import numpy as np

#creates a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)



#1. Paint the image a certain colour

#blank[:] = 0,255,0 #whole image become green.
    # [:] means "referenceing all pixels"
#cv.imshow('Green', blank)

#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Red', blank)



#2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #if you want to fill you set thickness = cv.FILLED or -1
#we can also 
#cv.rectangle(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2, (0,255,0)), thickness=-1)
cv.imshow('Rectangle', blank)



#3. Draw A Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow('Circle' blank)



#4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2, (255,255,255)), thickness=3)
cv.imshow('Line', blank)



#5. Write text
cv.putText(blank, 'Hello, my name is Jason!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)



#img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat', img)

cv.waitKey(0)
