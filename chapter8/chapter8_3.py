"""
图像闭运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena_noise.jpg", 0)
mu, sigma = 0.0, 10.0
noiseGause = np.random.normal(mu, sigma, imgGray.shape)
imgNoisy = imgGray + noiseGause
imgNoisy = np.uint8(cv2.normalize(imgNoisy, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]
ret, imgBin = cv2.threshold(imgNoisy, 125, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 图像的闭运算
kSize = (2, 2)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose1 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)

kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose2 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)

kSize = (5, 5)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose3 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgNoisy, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("Closed kSize=(2,2)"), plt.axis('off')
plt.imshow(imgClose1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("Closed kSize=(3,3)"), plt.axis('off')
plt.imshow(imgClose2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("Closed kSize=(5,5)"), plt.axis('off')
plt.imshow(imgClose3, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
