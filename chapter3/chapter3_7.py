"""
投影变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
h, w = img.shape[:2]  # 图片的高度和宽度

pointSrc = np.float32([[0, 0], [w - 1, 0], [0, h - 100], [w - 1, h - 100]])  # 原始图像中 4点坐标
pointDst = np.float32([[180, 50], [w - 180, 50], [0, h - 100], [w - 1, h - 100]])  # 变换图像中 4点坐标
MP = cv2.getPerspectiveTransform(pointSrc, pointDst)  # 计算投影变换矩阵 M
imgP = cv2.warpPerspective(img, MP, (512, 512))  # 用变换矩阵 M 进行投影变换

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(122), plt.imshow(cv2.cvtColor(imgP, cv2.COLOR_BGR2RGB)), plt.title("Projective")
plt.show()

