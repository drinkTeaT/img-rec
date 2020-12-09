import cv2  # 导入opencv库
import numpy as np


# 调用摄像头
def videox():
    vix = cv2.VideoCapture(0)  # 打开摄像头
    while True:
        ret, tu = vix.read()  # ret为返回值，tu为当前帧
        tu1 = cv2.flip(tu, 1)  # 图像反转，1为左右对换，-1为上下对换
        cv2.imshow("东小东标题", tu1)  # 显示图片在窗口上
        if 65 == cv2.waitKey(10):  # 等待大写 A 键盘按键按下
            cv2.imwrite("DONG.jpg", tu1)  # 保存停止帧图片
            break


cv2.namedWindow("东小东标题")  # 创建一个窗口，中文显示会出乱码问题

videox()  # 调用摄像头函数

print(cv2.waitKey(0))  # 等待任意键按下，并输出该按键的值

cv2.destroyAllWindows()  # 销毁窗口
