"""
DoG边缘检测算子
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

img = cv2.imread("../img/lena.jpg", flags=0)


# 高斯核低通滤波器，sigmaY 缺省时 sigmaY=sigmaX
kSize = (5, 5)
imgGaussBlur1 = cv2.GaussianBlur(img, (5, 5), sigmaX=1.0)  # sigma=1.0
imgGaussBlur2 = cv2.GaussianBlur(img, (5, 5), sigmaX=2.0)  # sigma=2.0
imgGaussBlur3 = cv2.GaussianBlur(img, (5, 5), sigmaX=4.0)  # sigma=4.0
imgGaussBlur4 = cv2.GaussianBlur(img, (5, 5), sigmaX=16.0)  # sigma=16.0

# 高斯差分算子 (Difference of Gaussian)
imgDoG1 = imgGaussBlur2 - imgGaussBlur1  # sigma=1.0,2.0
imgDoG2 = imgGaussBlur3 - imgGaussBlur2  # sigma=2.0,4.0
imgDoG3 = imgGaussBlur4 - imgGaussBlur3  # sigma=4.0,16.0

plt.figure(figsize=(10, 6))
plt.subplot(231), plt.title("GaussBlur (sigma=2.0)"), plt.imshow(imgGaussBlur2, cmap='gray'), plt.axis('off')
plt.subplot(232), plt.title("GaussBlur (sigma=4.0)"), plt.imshow(imgGaussBlur3, cmap='gray'), plt.axis('off')
plt.subplot(233), plt.title("GaussBlur (sigma=16.)"), plt.imshow(imgGaussBlur4, cmap='gray'), plt.axis('off')
plt.subplot(234), plt.title("DoG (sigma=1.0,2.0)"), plt.imshow(imgDoG1, cmap='gray'), plt.axis('off')
plt.subplot(235), plt.title("DoG (sigma=2.0,4.0)"), plt.imshow(imgDoG2, cmap='gray'), plt.axis('off')
plt.subplot(236), plt.title("DoG (sigma=4.0,16.)"), plt.imshow(imgDoG3, cmap='gray'), plt.axis('off')
plt.tight_layout()
plt.show()
