"""
高斯低通滤波
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)  # # flags=0 读取为灰度图像

kSize = (5, 5)
imgGaussBlur1 = cv2.GaussianBlur(img, (5, 5), sigmaX=10)
imgGaussBlur2 = cv2.GaussianBlur(img, (11, 11), sigmaX=20)

# 计算高斯核
gaussX = cv2.getGaussianKernel(5, 0)
gaussXY = gaussX * gaussX.transpose(1, 0)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title("ksize=5, sigma=10")
plt.imshow(cv2.cvtColor(imgGaussBlur1, cv2.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('off'), plt.title("ksize=11, sigma=20")
plt.imshow(cv2.cvtColor(imgGaussBlur2, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()


