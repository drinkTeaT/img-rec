import cv2
import numpy as np

img = cv2.imread('img/sk1.jpg')
my_roi = img[860:1020, 800:1060]
cv2.imshow("ROI", my_roi)
cv2.waitKey()
exit()
