"""
直方图均衡化
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", flags=0)  # flags=0 读取为灰度图像

imgEqu = cv2.equalizeHist(img)  # 使用 cv2.qualizeHist 完成直方图均衡化变换

fig = plt.figure(figsize=(7, 7))
plt.subplot(221), plt.title("Original image (youcans)"), plt.axis('off')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)  # 原始图像
plt.subplot(222), plt.title("Hist-equalized image"), plt.axis('off')
plt.imshow(imgEqu, cmap='gray', vmin=0, vmax=255)  # 转换图像
histImg, bins = np.histogram(img.flatten(), 256)  # 计算原始图像直方图
plt.subplot(223, yticks=[]), plt.bar(bins[:-1], histImg)  # 原始图像直方图
plt.title("Histogram of original image"), plt.axis([0, 255, 0, np.max(histImg)])
histEqu, bins = np.histogram(imgEqu.flatten(), 256)  # 计算原始图像直方图
plt.subplot(224, yticks=[]), plt.bar(bins[:-1], histEqu)  # 转换图像直方图
plt.title("Histogram of equalized image"), plt.axis([0, 255, 0, np.max(histImg)])
plt.show()
