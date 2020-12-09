# 输出颜色的坐标点
import cv2 as cv
import numpy as np
from PIL import ImageGrab


def main():
    # Loads an image
    while True:
        src = np.array(ImageGrab.grab(bbox=(0, 0, 1920 / 2, 1080 / 2)))
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, 1)
        rows = gray.shape[0]
        # min(max)Radius 为最小(大)半径
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                                  param1=100, param2=30,
                                  minRadius=5, maxRadius=7)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                print(center)
                # circle center
                # cv.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv.circle(src, center, radius, (255, 0, 255), 3)

        cv.imshow("detected circles", src)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break


main()
