import numpy
import cv2

img = numpy.zeros((3, 3), dtype=numpy.uint8)
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)