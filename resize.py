import cv2 as cv


def resize_img(img, new_height, new_width):
    new_img = cv.resize(img, (new_width, new_height))
    return new_img
