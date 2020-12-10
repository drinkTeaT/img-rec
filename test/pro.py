import cv2
import numpy as np

img = cv2.imread('img/sk1.jpg')
cv2.imshow('origin', img)
cv2.imshow('canny', cv2.Canny(img, 1000, 400))
cv2.waitKey()
cv2.destroyWindow()
