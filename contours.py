
# It helps us to detect borders of objects

import cv2 as cv
from read_image import minato

print(minato.shape)

minato = cv.GaussianBlur(minato, (7, 7), 0)

gray = cv.cvtColor(minato, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 125, 225)

contours, hei = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print(f"no of contours is {len(contours)}")

cv.drawContours(minato, contours, -1, (0, 225, 225), 3)
cv.imshow("contours", minato)
cv.waitKey(0)
