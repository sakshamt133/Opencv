import cv2 as cv
from read_image import minato
from resize import resize_img
from rotate import rotate_img
from shift import shift_img
from read_video import read_video


new_minato = resize_img(minato, 600, 600)
cv.imshow("New", new_minato)

# new_minato = rotate_img(new_minato, 90)
# cv.imshow("new", new_minato)

new_minato = shift_img(new_minato, 40, 40)
cv.imshow("new", new_minato)

read_video("vid.mp4")

cv.waitKey(0)
