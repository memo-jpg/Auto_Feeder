import cv2 as cv

img = cv.imread('Photos/cat.jpg') #reading in an image
#takes a path to an image and returns image as a matrix of pixels
    #placing the matrix of pixels into img

cv.imshow('Cat', img) #Displays the image as a new window
    #2 parameters:
        #1) Name of the window
        #2) The actual matrix of pixels to display

cv.waitKey(0) #Keyboard Binding Function
#waits for a specific delay, or time in milliseconds, for a key to be pressed
    #if you pass in 0, it waits for an infinite amount of time for a keyboard key to be pressed

#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
        isTrue, frame = capture.read()

        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows()
