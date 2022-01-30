import cv2 as cv
from read_image import minato

minato = cv.cvtColor(minato, cv.COLOR_BGR2GRAY)

# Simple Thresholding
_, simple = cv.threshold(minato, 125, 255, cv.THRESH_BINARY)
cv.imshow("Simple", simple)

# Inverse Thresholding
_, inverse = cv.threshold(minato, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow("iinverse", inverse)

# Adaptive Thresholding
adaptive = cv.adaptiveThreshold(minato, 225, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive", adaptive)

cv.waitKey(0)
