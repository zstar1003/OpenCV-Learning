"""
图像旋转(以任意点为中心)
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
height, width = img.shape[:2]  # 图片的高度和宽度

theta1, theta2 = 30, 45  # 顺时针旋转角度，单位为角度
x0, y0 = width // 2, height // 2  # 以图像中心作为旋转中心
MAR1 = cv2.getRotationMatrix2D((x0, y0), theta1, 1.0)
MAR2 = cv2.getRotationMatrix2D((x0, y0), theta2, 1.0)
imgR1 = cv2.warpAffine(img, MAR1, (width, height))  # 旋转变换，默认为黑色填充
imgR2 = cv2.warpAffine(img, MAR2, (width, height), borderValue=(255, 255, 255))  # 设置白色填充

plt.figure(figsize=(10, 6))
plt.subplot(131), plt.axis('off'), plt.title(r"$Origin$")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title(r"$Rotation {}^o$".format(theta1))
plt.imshow(cv2.cvtColor(imgR1, cv2.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('off'), plt.title(r"$Rotation {}^o$".format(theta2))
plt.imshow(cv2.cvtColor(imgR2, cv2.COLOR_BGR2RGB))
plt.show()
