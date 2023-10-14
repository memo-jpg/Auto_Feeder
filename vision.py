import cv2 as cv

def get_image_difference(image_1, image_2):
    first_image_hist = cv.calcHist([image_1], [0], None, [256], [0,256])
    second_image_hist = cv.calcHist([image_2], [0], None, [256], [0,256])

    img_hist_diff = cv.compareHist(first_image_hist, second_image_hist, cv.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv.matchTemplate(first_image_hist, second_image_hist, cv.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match

    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


minimum_commutative_image_diff = 1

# Compare Images
image_1 = cv.imread('/home/pi/Resume_Project/Photos/image.jpg')
image_2 = cv.imread('/home/pi/Resume_Project/Photos/image4.jpg')

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
else:
    print('Not Matched')
