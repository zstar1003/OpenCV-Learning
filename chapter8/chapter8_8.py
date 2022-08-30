"""
灰度腐蚀
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)

# 图像腐蚀
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
imgErode1 = cv2.erode(imgGray, kernel=element)  # 图像腐蚀

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
imgErode2 = cv2.erode(imgGray, kernel=element)  # 图像腐蚀

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
imgErode3 = cv2.erode(imgGray, kernel=element)  # 图像腐蚀

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("eroded kSize=(3,3)"), plt.axis('off')
plt.imshow(imgErode1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("eroded kSize=(9,9)"), plt.axis('off')
plt.imshow(imgErode2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("eroded kSize=(25,25)"), plt.axis('off')
plt.imshow(imgErode3, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
