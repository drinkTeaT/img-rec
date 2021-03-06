# 输出颜色的坐标点
# https://docs.opencv.org/master/d4/d70/tutorial_hough_circle.html
import time

import cv2 as cv
import numpy as np
from PIL import ImageGrab


def detect_circles(gray, rows, min_radius, max_radius, close):
    return cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 0.2, rows / close,
                           param1=100, param2=30,
                           minRadius=min_radius, maxRadius=max_radius)


def main():
    # Loads an image
    while True:
        src = np.array(ImageGrab.grab(bbox=(640, 800, 1500, 1080)))
        copy = np.copy(src)
        # 放大图片
        rows, cols, _channels = map(int, src.shape)
        src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))
        copy = cv.pyrUp(copy, dstsize=(2 * cols, 2 * rows))
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        gray_copy = cv.cvtColor(copy, cv.COLOR_BGR2GRAY)
        # 7只对白色敏感
        # 5对白色敏感蓝色不敏感
        # 3对蓝色(黑色)敏感白色不敏感
        # 1只对黑色敏感
        gray = cv.medianBlur(gray, 3)
        gray_copy = cv.medianBlur(gray_copy, 7)
        rows = gray.shape[0]
        # min(max)Radius 为最小(大)半径
        min_radius = 1
        max_radius = 10
        circles = detect_circles(gray, rows, min_radius, max_radius, 128)
        write_circles = detect_circles(gray_copy, rows, min_radius,max_radius, 128)
        if circles is not None and write_circles is not None:
            circles_copy = np.uint16(np.around(write_circles))
            for i in circles_copy[0, :]:
                center = (i[0], i[1])
                write_center = (i[0], i[1])
                radius = i[2]
                cv.circle(src, center, radius, (255, 0, 255), 3)
                print("白色点:" + str(write_center))
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                print(center)
                # circle center
                cv.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv.circle(src, center, radius, (255, 0, 255), 3)
        cv.imshow("detected circles", src)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break



main()
