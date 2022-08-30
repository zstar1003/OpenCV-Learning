"""
图像顶帽运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena_noise.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 205, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

kernel = np.ones((5, 5), np.uint8)  # 卷积核
imgOpen = cv2.morphologyEx(imgBin, cv2.MORPH_OPEN, kernel)  # 开运算
imgThat = cv2.morphologyEx(imgBin, cv2.MORPH_TOPHAT, kernel)  # 顶帽运算

plt.figure(figsize=(9, 5))
plt.subplot(131), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("MORPH_OPEN"), plt.axis('off')
plt.imshow(imgOpen, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title("MORPH_TOPHAT"), plt.axis('off')
plt.imshow(imgThat, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
