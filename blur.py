# We use blur to reduce the no. of features0

import cv2 as cv
from read_image import minato


# Simple Blur
blur = cv.blur(minato, (11, 11))
cv.imshow("blur", blur)

# median blur
median = cv.medianBlur(minato, 11)
cv.imshow("median", median)

# gaussian blur
gaussian = cv.GaussianBlur(minato, (11, 11), sigmaX=0.1)
cv.imshow("gau", gaussian)

cv.waitKey(0)