"""
边界提取
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 25, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 二值化处理

kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgErode1 = cv2.erode(imgBin, kernel=kernel)  # 图像腐蚀
imgBound1 = imgBin - imgErode1  # 图像边界提取

plt.figure(figsize=(9, 5))
plt.subplot(131), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Eroded kSize=(3,3)"), plt.axis('off')
plt.imshow(imgErode1, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title("Boundary extraction"), plt.axis('off')
plt.imshow(imgBound1, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
