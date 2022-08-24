"""
Scharr算子
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)

# 使用 cv2.Scharr 实现 Scharr 算子
ScharrX = cv2.Scharr(img, cv2.CV_16S, 1, 0)  # 计算 x 轴方向
ScharrY = cv2.Scharr(img, cv2.CV_16S, 0, 1)  # 计算 y 轴方向
absX = cv2.convertScaleAbs(ScharrX)  # 转回 uint8
absY = cv2.convertScaleAbs(ScharrY)  # 转回 uint8
ScharrXY = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)  # 用绝对值近似平方根

plt.figure(figsize=(10, 6))
plt.subplot(141), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.axis('off'), plt.title("ScharrX")
plt.imshow(ScharrX, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.axis('off'), plt.title("ScharrY")
plt.imshow(ScharrY, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.axis('off'), plt.title("ScharrXY")
plt.imshow(ScharrXY, cmap='gray')
plt.tight_layout()
plt.show()
