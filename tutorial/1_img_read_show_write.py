# 在这里，你将学习如何读取图像，如何显示图像以及如何将其保存回去
# 你将学习以下功能：cv.imread()，cv.imshow()，cv.imwrite()
import cv2 as cv
from matplotlib import pyplot as plt

# 加载图像 1-原始图像。2-灰度图像。-1加载图像包括alpha通道。
img = cv.imread('../static/img/1.jpg', 2)
# 展示
cv.imshow('image', img)
cv.waitKey(0)
# 存储图片
cv.imwrite('img/1-gray.jpg', img)
cv.destroyAllWindows()

# 使用matplotlib
# 图片加载进来
img = cv.imread('../static/img/1.jpg', 1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
