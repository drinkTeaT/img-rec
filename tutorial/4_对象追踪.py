# 在本教程中，你将学习如何将图像从一个色彩空间转换到另一个，像BGR↔灰色，BGR↔HSV等
# 除此之外，我们还将创建一个应用程序，以提取视频中的彩色对象
# 你将学习以下功能：cv.cvtColor，**cv.inRange**等。
import cv2 as cv

# 颜色转换。1： BGR->灰度 cv.COLOR_BGR2GRAY 2：BGR->HSV cv.COLOR_BGR2HSV HSV的色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]
import cv2 as cv
import numpy as np
from PIL import ImageGrab

frame = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
while 1:
    # 读取帧
    # _, frame = cap.read()
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中蓝色的范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 设置HSV的阈值使得只取蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 将掩膜和图像逐像素相加
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
