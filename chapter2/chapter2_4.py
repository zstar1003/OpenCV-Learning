"""
圆形掩模
"""
import cv2
import numpy as np

img1 = cv2.imread("../img/img.jpg")

Mask1 = np.zeros((img1.shape[0], img1.shape[1]), dtype=np.uint8)  # 返回与图像 img1 尺寸相同的全零数组
Mask2 = Mask1.copy()
cv2.circle(Mask1, (285, 285), 110, (255, 255, 255), -1)  # -1 表示实心
cv2.ellipse(Mask2, (285, 285), (100, 150), 0, 0, 360, 255, -1)  # -1 表示实心

imgAddMask1 = cv2.add(img1, np.zeros(np.shape(img1), dtype=np.uint8), mask=Mask1)  # 提取圆形 ROI
imgAddMask2 = cv2.add(img1, np.zeros(np.shape(img1), dtype=np.uint8), mask=Mask2)  # 提取椭圆 ROI

cv2.imshow("circularMask", Mask1)  # 显示掩模图像 Mask
cv2.imshow("circularROI", imgAddMask1)  # 显示掩模加法结果 imgAddMask1
cv2.imshow("ellipseROI", imgAddMask2)  # 显示掩模加法结果 imgAddMask2
key = cv2.waitKey(0)  # 等待按键命令

