import cv2

img = cv2.imread('img/sk1.jpg')
img[:, :, 1] = 0
cv2.imshow("No Green", img)
cv2.waitKey()
cv2.destroyWindow("No Green")
exit()
