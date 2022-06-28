#Histograms allow you to visualize the distribution of pixel intensities in an image.
    #whether it be in color or grayscale
#kind of like a graph or plot that will give you a high level intuition of the pixel distribution in the image
import cv2 as cv
import matplotlib.pylot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#For grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#circle = cv.circle(blank, img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

#mask = cv.bitwise_and(gray, gray, mask=circle)
#cv.imshow('Mask', mask)

# GRayscale histogram
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])

# Colour histogram
mask = cv.circle(blank, img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked', masked)


plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    #hist = cv.calcHist([img], [i], None, [256], [0,256])
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)
