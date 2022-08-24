"""
图像错切
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
height, width = img.shape[:2]  # 图片的高度和宽度

MAS = np.float32([[1, 0.2, 0], [0, 1, 0]])  # 构造错切变换矩阵
imgShear = cv2.warpAffine(img, MAS, (width, height))

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("imgOrigin")
plt.subplot(122), plt.imshow(cv2.cvtColor(imgShear, cv2.COLOR_BGR2RGB)), plt.title("imgShear")
plt.show()
