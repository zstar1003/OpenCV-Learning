"""
Canny边缘检测算子
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)

# 高斯核低通滤波器，sigmaY 缺省时 sigmaY=sigmaX
kSize = (5, 5)
imgGauss1 = cv2.GaussianBlur(img, kSize, sigmaX=1.0)  # sigma=1.0
imgGauss2 = cv2.GaussianBlur(img, kSize, sigmaX=10.0)  # sigma=2.0

# 高斯差分算子 (Difference of Gaussian)
imgDoG = imgGauss2 - imgGauss1  # sigma=1.0, 10.0

# Canny 边缘检测， kSize 为高斯核大小，t1,t2为阈值大小
t1, t2 = 50, 150
imgCanny = cv2.Canny(imgGauss1, t1, t2)

plt.figure(figsize=(10, 6))
plt.subplot(131), plt.title("Origin"), plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(132), plt.title("DoG"), plt.imshow(imgDoG, cmap='gray'), plt.axis('off')
plt.subplot(133), plt.title("Canny"), plt.imshow(imgCanny, cmap='gray'), plt.axis('off')
plt.tight_layout()
plt.show()
