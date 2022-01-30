import cv2 as cv
from read_image import minato
import numpy as np

blank = np.zeros(shape=(1978, 728), dtype=np.uint8)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 250, (0, 255, 255), -1)
cv.imshow("cir", blank)

# bit_and = cv.bitwise_and(minato, minato, mask=cir)
# cv.imshow("ANd", bit_and)

cv.waitKey(0)