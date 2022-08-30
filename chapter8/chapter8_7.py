"""
击中-击不中变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)
ret, imgBin = cv2.threshold(imgGray, 25, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 闭运算
kernel = np.ones((3, 3), dtype=np.uint8)  # 生成盒式卷积核
imgClose = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)  # 闭运算
# 击中击不中变换
kernB1 = np.array([[0, 0, 0], [0, -1, 1], [0, 0, 0]], dtype=np.int32)  # B1
kernB2 = np.array([[0, 0, 0], [1, -1, 0], [0, 0, 0]], dtype=np.int32)  # B2
imgH1 = cv2.morphologyEx(imgClose, cv2.MORPH_HITMISS, kernB1)
imgH2 = cv2.morphologyEx(imgClose, cv2.MORPH_HITMISS, kernB2)
imgHMT = cv2.add(imgH1, imgH2)  # 击中击不中

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("kern B1"), plt.axis('off')
plt.imshow(imgH1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("kern B2"), plt.axis('off')
plt.imshow(imgH2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("HMT"), plt.axis('off')
plt.imshow(imgHMT, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
