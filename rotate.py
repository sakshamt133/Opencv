import cv2 as cv


def rotate_img(img, angle):
    height, width, _ = img.shape
    rot_mat = cv.getRotationMatrix2D((width//2, height//2), angle, scale=1)
    return cv.warpAffine(img, rot_mat, (width, height))
