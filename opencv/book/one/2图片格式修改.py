import numpy
import cv2

# 新增图片并对格式进行修改
img = cv2.imread('img/1.jpg')
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
cv2.imwrite('img/1copy.png', img)
