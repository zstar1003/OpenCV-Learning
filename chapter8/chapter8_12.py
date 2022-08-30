"""
凸包提取
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/img.jpg", 1)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
imgBlur = cv2.blur(imgGray, (3, 3))  # 去除噪点
ret, imgBin = cv2.threshold(imgBlur, 225, 255, cv2.THRESH_BINARY)  # 二值化处理

img2, contours, hierarchy = cv2.findContours(imgBin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 寻找所有的轮廓
hullAll = []  # 所有的凸包
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i], False)  # 计算轮廓 contours[i] 的凸包
    hullAll.append(hull)

colorContours = (0, 255, 0)  # 设置轮廓的颜色
colorConvexHull = (255, 255, 255)  # 设置凸包的颜色
imgContours = np.zeros(img.shape, np.uint8)
for i in range(len(contours)):  # 绘制轮廓线
    cv2.drawContours(imgContours, contours, i, colorContours, 2, 8, hierarchy)
imgDrawing = imgContours.copy()
for i in range(len(contours)):  # 绘制凸包线
    cv2.drawContours(imgDrawing, hullAll, i, colorConvexHull, 2, 8)

plt.figure(figsize=(9, 6))
plt.subplot(221), plt.axis('off'), plt.title("origin")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(222), plt.title("binary"), plt.axis('off')
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(223), plt.title("contours"), plt.axis('off')
plt.imshow(cv2.cvtColor(imgContours, cv2.COLOR_BGR2RGB))
plt.subplot(224), plt.title("convex hull"), plt.axis('off')
plt.imshow(cv2.cvtColor(imgDrawing, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
