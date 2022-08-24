"""
直方图规定化
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", flags=0)  # flags=0 读取为灰度图像
imgRef = cv2.imread("../img/mb.jpg", flags=0)  # 匹配模板图像, matching template

# 计算累计直方图
histImg, bins = np.histogram(img.flatten(), 256)  # 计算原始图像直方图
histRef, bins = np.histogram(imgRef.flatten(), 256)  # 计算匹配模板直方图
cdfImg = histImg.cumsum()  # 计算原始图像累积分布函数 CDF
cdfRef = histRef.cumsum()  # 计算匹配模板累积分布函数 CDF

# 计算直方图匹配转换函数
transM = np.zeros(256)
for i in range(256):
    index = 0
    vMin = np.fabs(cdfImg[i] - cdfRef[0])
    for j in range(256):
        diff = np.fabs(cdfImg[i] - cdfRef[j])
        if (diff < vMin):
            index = int(j)
            vMin = diff
    transM[i] = index


imgOut = transM[img].astype(np.uint8)

fig = plt.figure(figsize=(10, 7))
plt.subplot(231), plt.title("Original image"), plt.axis('off')
plt.imshow(img, cmap='gray')  # 原始图像
plt.subplot(232), plt.title("Matching template"), plt.axis('off')
plt.imshow(imgRef, cmap='gray')  # 匹配模板
plt.subplot(233), plt.title("Matching output"), plt.axis('off')
plt.imshow(imgOut, cmap='gray')  # 匹配结果
histImg, bins = np.histogram(img.flatten(), 256)  # 计算原始图像直方图
plt.subplot(234, yticks=[]), plt.bar(bins[:-1], histImg)
histRef, bins = np.histogram(imgRef.flatten(), 256)  # 计算匹配模板直方图
plt.subplot(235, yticks=[]), plt.bar(bins[:-1], histRef)
histOut, bins = np.histogram(imgOut.flatten(), 256)  # 计算匹配结果直方图
plt.subplot(236, yticks=[]), plt.bar(bins[:-1], histOut)
plt.show()
