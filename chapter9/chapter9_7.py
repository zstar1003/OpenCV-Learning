"""
图像分割之绘制轮廓
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg", flags=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Origin")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title("BinaryInv")
plt.imshow(binary, 'gray')

# 寻找二值化图中的轮廓
binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV3
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV4~
# # 绘制轮廓
contourPic = img.copy()  # OpenCV3.2 之前的早期版本，查找轮廓函数会修改原始图像
contourPic = cv2.drawContours(contourPic, contours, -1, (0, 0, 255), 2)  # OpenCV3
# contourPic = cv.drawContours(img, contours, -1, (0, 0, 255), thickness=cv.FILLED,maxLevel=1)

print("len(contours) = ", len(contours))  # 所有轮廓的列表
for i in range(len(contours)):
    print("i=", i, contours[i].shape)  # 第 i 个轮廓的边界点
print("hierarchy.shape : ", hierarchy.shape)  # 层次结构
print(hierarchy)

plt.subplot(133), plt.axis('off'), plt.title("External contour")
plt.imshow(cv2.cvtColor(contourPic, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
