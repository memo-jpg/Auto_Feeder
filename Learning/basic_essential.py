import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #to increase blur, change the kernel size ( (7,7) )
cv.imshow('Blur', blur)

# Edge Cascade
    #trying to find the edges present in the image
canny = cv.Canny(img, 125, 175) #pass in blur to reduce amount of edges
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #ignoring resolution
cv.imshow('Resize', resized)

# Cropping
    #array slicing, taking advantage of fact that images are arrays
cropping = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
