import cv2 as cv
import numpy as np


def shift_img(img, x, y):
    height, width, _ = img.shape
    shift_mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(img, shift_mat, (width, height))
