import cv2 as cv

img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat', img)


def changeRes(width,height):
    # Live Video only
    capture.set(3,width)
    capture.set(4,height)

#Large video/image files store a large amount of data
#takes *a lot* of processing power, so we downscale it
def rescaleFrame(frame, scale=0.75):
    # Images, Video, and Live Video
    width = int(frame.shape[1] * scale) #frame.shape[1] is basically the width of the image
    height = int(frame.shape[0] * scale) #frame.shape[0] is basically the height of the image
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
        isTrue, frame = capture.read()

        frame_resized = rescaleFrame(frame, scale=0.2)

        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows()

