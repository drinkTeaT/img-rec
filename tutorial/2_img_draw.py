# 学习使用OpenCV绘制不同的几何形状
# 您将学习以下功能：cv.line()，cv.circle()，cv.rectangle()，cv.ellipse()，cv.putText()等。
import numpy as np
import cv2 as cv

# 创建黑色的图像
img = cv.imread('../static/img/1.jpg', 2)
# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv.imshow('image', img)
cv.waitKey(0)
