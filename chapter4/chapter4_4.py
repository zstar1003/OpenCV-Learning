"""
灰度直方图
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", flags=0)  # flags=0 读取为灰度图像

histCV = cv2.calcHist([img], [0], None, [256], [0, 256])  # OpenCV 函数 cv2.calcHist
histNP, bins = np.histogram(img.flatten(), 256)

plt.figure(figsize=(10, 3))
plt.subplot(131), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title("Original"), plt.axis('off')
plt.subplot(132, xticks=[], yticks=[]), plt.axis([0, 255, 0, np.max(histCV)])
plt.bar(range(256), histCV[:, 0]), plt.title("Gray Hist(cv2.calcHist)")
plt.subplot(133, xticks=[], yticks=[]), plt.axis([0, 255, 0, np.max(histCV)])
plt.bar(bins[:-1], histNP), plt.title("Gray Hist(np.histogram)")
plt.show()
