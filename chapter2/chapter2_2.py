"""
图像的渐变切换
"""
import cv2
import numpy as np

img1 = cv2.imread("../img/lena.jpg")
img2 = cv2.imread("../img/img.jpg")
wList = np.arange(0.0, 1.0, 0.05)  # start, end, step
for w in wList:
    imgAddW = cv2.addWeighted(img1, w, img2, (1 - w), 0)
    cv2.imshow("imgAddWeight", imgAddW)
    cv2.waitKey(100)


