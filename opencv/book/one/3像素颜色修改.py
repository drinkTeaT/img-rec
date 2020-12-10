import cv2
import numpy as np

# 会有一个像素改变颜色
img = cv2.imread('img/1.jpg')
img[10][10] = [100, 100, 0]
cv2.imshow("spot", img)
cv2.waitKey()

# 效率更好的方式
print(img.item(150, 120, 0))
img.itemset((150, 120, 0), 255)
cv2.imshow("pixel", img)
cv2.waitKey()