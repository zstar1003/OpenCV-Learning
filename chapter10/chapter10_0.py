"""
颜色空间转换
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

imgBGR = cv.imread("../img/img.jpg", flags=1)

imgRGB = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB)  # BGR 转换为 RGB, 用于 PyQt5, matplotlib
imgGRAY = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)  # BGR 转换为灰度图像
imgHSV = cv.cvtColor(imgBGR, cv.COLOR_BGR2HSV)  # BGR 转换为 HSV 图像
imgYCrCb = cv.cvtColor(imgBGR, cv.COLOR_BGR2YCrCb)  # BGR转YCrCb
imgHLS = cv.cvtColor(imgBGR, cv.COLOR_BGR2HLS)  # BGR 转 HLS 图像
imgXYZ = cv.cvtColor(imgBGR, cv.COLOR_BGR2XYZ)  # BGR 转 XYZ 图像
imgLAB = cv.cvtColor(imgBGR, cv.COLOR_BGR2LAB)  # BGR 转 LAB 图像
imgYUV = cv.cvtColor(imgBGR, cv.COLOR_BGR2YUV)  # BGR 转 YUV 图像

# 调用matplotlib显示处理结果
titles = ['BGR', 'RGB', 'GRAY', 'HSV', 'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
images = [imgBGR, imgRGB, imgGRAY, imgHSV, imgYCrCb,
          imgHLS, imgXYZ, imgLAB, imgYUV]
plt.figure(figsize=(10, 8))
for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
