import cv2 as cv
from read_image import minato

# BGR to GrayScale
gray = cv.cvtColor(minato, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV
hsv = cv.cvtColor(minato, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to RGB
rgb = cv.cvtColor(minato, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

cv.waitKey(0)