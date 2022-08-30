"""
灰度膨胀
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


imgGray = cv2.imread("../img/lena.jpg", 0)

# 灰度膨胀
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
imgDilate1 = cv2.dilate(imgGray, kernel=element)  # 图像膨胀

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
imgDilate2 = cv2.dilate(imgGray, kernel=element)  # 图像膨胀

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Origin")
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Dilate kSize=(3,3)"), plt.axis('off')
plt.imshow(imgDilate1, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title("Dilate kSize=(5,5)"), plt.axis('off')
plt.imshow(imgDilate2, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
