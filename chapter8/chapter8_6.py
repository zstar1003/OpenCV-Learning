"""
形态学梯度运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 15, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 图像的形态学梯度
kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgGrad1 = cv2.morphologyEx(imgBin, cv2.MORPH_GRADIENT, kernel)  # 形态学梯度

kSize = (5, 5)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgGrad2 = cv2.morphologyEx(imgBin, cv2.MORPH_GRADIENT, kernel)  # 形态学梯度

kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgOpen = cv2.morphologyEx(imgBin, cv2.MORPH_OPEN, kernel)  # 开运算
imgOpenGrad = cv2.morphologyEx(imgOpen, cv2.MORPH_GRADIENT, kernel)  # 形态学梯度

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("Gradient (size=3)"), plt.axis('off')
plt.imshow(imgGrad1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("Gradient (size=5)"), plt.axis('off')
plt.imshow(imgGrad2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("Opening -> Gradient"), plt.axis('off')
plt.imshow(imgOpenGrad, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()

