"""
Sobel算子
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)

# 使用 cv2.Sobel 实现 Sobel 算子
SobelX = cv2.Sobel(img, cv2.CV_16S, 1, 0)  # 计算 x 轴方向
SobelY = cv2.Sobel(img, cv2.CV_16S, 0, 1)  # 计算 y 轴方向
absX = cv2.convertScaleAbs(SobelX)  # 转回 uint8
absY = cv2.convertScaleAbs(SobelY)  # 转回 uint8
SobelXY = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)  # 用绝对值近似平方根

plt.figure(figsize=(10, 6))
plt.subplot(141), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.axis('off'), plt.title("SobelX")
plt.imshow(SobelX, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.axis('off'), plt.title("SobelY")
plt.imshow(SobelY, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.axis('off'), plt.title("SobelXY")
plt.imshow(SobelXY, cmap='gray')
plt.tight_layout()
plt.show()
