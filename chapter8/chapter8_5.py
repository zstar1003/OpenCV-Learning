"""
图像底帽运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

kernel = np.ones((5, 5), np.uint8)  # 卷积核
imgClose = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)  # 闭运算
imgBhat = cv2.morphologyEx(imgBin, cv2.MORPH_BLACKHAT, kernel)  # 底帽运算

plt.figure(figsize=(9, 5))
plt.subplot(131), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("MORPH_CLOSE"), plt.axis('off')
plt.imshow(imgClose, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title("MORPH_BLACKHAT"), plt.axis('off')
plt.imshow(imgBhat, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
