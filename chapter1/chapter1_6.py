"""
图像通道合并
"""
import cv2
import numpy as np

img1 = cv2.imread("../img/img.jpg", flags=1)  # flags=1 读取彩色图像(BGR)
bImg, gImg, rImg = cv2.split(img1)  # 拆分为 BGR 独立通道

# cv2.merge 实现图像通道的合并
imgMerge = cv2.merge([bImg, gImg, rImg])
cv2.imshow("cv2Merge", imgMerge)

# Numpy 拼接实现图像通道的合并
imgStack = np.stack((bImg, gImg, rImg), axis=2)
cv2.imshow("npStack", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口


