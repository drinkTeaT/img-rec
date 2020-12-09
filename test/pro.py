# -*- coding: UTF-8 -*-
import cv2
import numpy as np

img = cv2.imread("img/1.jpg")

# 将图像转换为HSV像素空间，因为HSV空间对颜色比较敏感
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 分别设置HSV颜色空间中，红色、黄色、蓝色、绿色的阈值
lower_red = np.array([0, 43, 46])
upper_red = np.array([10, 255, 255])

lower_yellow = np.array([26, 43, 46])
upper_yellow = np.array([34, 255, 255])

lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])

lower_green = np.array([35, 43, 46])
upper_green = np.array([77, 255, 255])

# 使用inRange函数获取图像中目标颜色的索引
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

img_mask = np.copy(img)

color_1 = [128, 9, 21]
color_2 = [50, 14, 77]
color_3 = [61, 154, 124]
color_4 = [59, 170, 246]

# 给目标像素赋值
img_mask[mask_red != 0] = color_1
img_mask[mask_blue != 0] = color_2
img_mask[mask_green != 0] = color_3
img_mask[mask_yellow != 0] = color_4

cv2.imshow("changed", img_mask)
cv2.imshow("source", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
