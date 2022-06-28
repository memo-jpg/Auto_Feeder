#Masking allows us to focus on certain parts of an image that we'd like to focus on.
    #removes all the stuff we don't want(?)
import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8') #the dimensions of the mask have to be the same size as that of the image
    #if it isn't, it won't work
cv.imshow('Blank Image', blank)

#Draw a circle over the blank image, and call it the mask
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
#cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

#masked = cv.bitwise_and(img,img,mask=mask)
#cv.imshow('Masked Image', masked)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)
