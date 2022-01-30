import cv2 as cv
import numpy as np

blank = np.zeros(shape=(750, 750, 3), dtype=np.uint8)

# # Rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 255), -1)
# cv.imshow("Rect", blank)

# # Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 250, (0, 255, 255), -1)
# cv.imshow("cir", blank)

# # write text
# cv.putText(blank, "Saksham Thakur", (0, 100), cv.FONT_ITALIC, 1, (0, 255, 0), 3)
# cv.imshow("texy", blank)

cv.waitKey(0)