"""
反色变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 颜色转换：BGR(OpenCV) -> Gray
h, w = img.shape[:2]  # 图片的高度和宽度

imgInv = np.empty((w, h), np.uint8)  # 创建空白数组
for i in range(h):
    for j in range(w):
        imgInv[i][j] = 255 - imgGray[i][j]

plt.figure(figsize=(10, 6))
plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("imgBGR"), plt.axis('off')
plt.subplot(132), plt.imshow(imgGray, cmap='gray'), plt.title("imgGray"), plt.axis('off')
plt.subplot(133), plt.imshow(imgInv, cmap='gray'), plt.title("imgInv"), plt.axis('off')
plt.show()
