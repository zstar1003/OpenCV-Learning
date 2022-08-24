"""
图像翻转
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)

imgFlip1 = cv2.flip(img, 0)  # 垂直翻转
imgFlip2 = cv2.flip(img, 1)  # 水平翻转
imgFlip3 = cv2.flip(img, -1)  # 水平和垂直翻转

plt.figure(figsize=(9, 6))
plt.subplot(221), plt.axis('off'), plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 原始图像
plt.subplot(222), plt.axis('off'), plt.title("Flipped Horizontally")
plt.imshow(cv2.cvtColor(imgFlip2, cv2.COLOR_BGR2RGB))  # 水平翻转
plt.subplot(223), plt.axis('off'), plt.title("Flipped Vertically")
plt.imshow(cv2.cvtColor(imgFlip1, cv2.COLOR_BGR2RGB))  # 垂直翻转
plt.subplot(224), plt.axis('off'), plt.title("Flipped Horizontally & Vertically")
plt.imshow(cv2.cvtColor(imgFlip3, cv2.COLOR_BGR2RGB))  # 水平垂直翻转
plt.show()
