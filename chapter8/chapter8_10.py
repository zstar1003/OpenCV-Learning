"""
灰度开运算和闭运算
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 全 1 结构元
imgErode = cv2.erode(imgGray, kernel=element)  # 灰度腐蚀
imgDilate = cv2.dilate(imgGray, kernel=element)  # 灰度膨胀
imgOpen = cv2.morphologyEx(imgGray, cv2.MORPH_OPEN, element)  # 灰度开运算
imgClose = cv2.morphologyEx(imgGray, cv2.MORPH_CLOSE, element)  # 灰度闭运算
imgGrad = cv2.morphologyEx(imgGray, cv2.MORPH_GRADIENT, element)  # 形态学梯度

plt.figure(figsize=(9, 7))
plt.subplot(231), plt.axis('off'), plt.title("Origin")
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
plt.subplot(232), plt.title("Eroded image"), plt.axis('off')
plt.imshow(imgErode, cmap='gray', vmin=0, vmax=255)
plt.subplot(233), plt.title("Dilated image"), plt.axis('off')
plt.imshow(imgDilate, cmap='gray', vmin=0, vmax=255)
plt.subplot(234), plt.title("Opening image"), plt.axis('off')
plt.imshow(imgOpen, cmap='gray', vmin=0, vmax=255)
plt.subplot(235), plt.title("Closing image"), plt.axis('off')
plt.imshow(imgClose, cmap='gray', vmin=0, vmax=255)
plt.subplot(236), plt.title("Gradient image"), plt.axis('off')
plt.imshow(imgGrad, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
