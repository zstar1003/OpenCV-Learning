"""
图像平移
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
rows, cols, ch = img.shape

dx, dy = 100, 50  # dx=100 向右偏移量, dy=50 向下偏移量
MAT = np.float32([[1, 0, dx], [0, 1, dy]])  # 构造平移变换矩阵
# dst = cv2.warpAffine(img, MAT, (cols, rows))  # 默认为黑色填充
dst = cv2.warpAffine(img, MAT, (cols, rows), borderValue=(255, 255, 255))  # 设置白色填充

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(122), plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)), plt.title("Translational")
plt.show()
