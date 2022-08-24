"""
图像旋转(以原点为中心)
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
rows, cols, ch = img.shape

theta = np.pi / 8.0  # 顺时针旋转角度
cosTheta = np.cos(theta)
sinTheta = np.sin(theta)
MAT = np.float32([[cosTheta, -sinTheta, 0], [sinTheta, cosTheta, 0]])  # 构造旋转变换矩阵
# dst = cv2.warpAffine(img, MAT, (cols, rows))  # 默认为黑色填充
dst = cv2.warpAffine(img, MAT, (cols, rows), borderValue=(255, 255, 255))  # 设置白色填充

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Origin")
plt.subplot(122), plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)), plt.title("Rotation")
plt.show()
