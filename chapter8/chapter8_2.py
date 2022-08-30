"""
图像开运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena_noise.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 图像的开运算
kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgOpen = cv2.morphologyEx(imgGray, cv2.MORPH_OPEN, kernel)

plt.figure(figsize=(9, 5))
plt.subplot(121), plt.axis('off'), plt.title("Origin")
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
plt.subplot(122), plt.title("Opening kSize=(3,3)"), plt.axis('off')
plt.imshow(imgOpen, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
