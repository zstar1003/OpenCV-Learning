"""
边缘检测和角点检测
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", flags=1)
imgSign = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片格式转换：BGR(OpenCV) -> Gray
# ret, imgBin = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 边缘检测
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
imgEdge = cv2.morphologyEx(imgGray, cv2.MORPH_GRADIENT, element)  # 形态学梯度

# 构造 5×5 结构元素，十字形、菱形、方形、X 型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字型结构元
square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构元
xShape = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # X 形结构元
diamond = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 构造菱形结构元
diamond[1, 1] = diamond[3, 3] = 1
diamond[1, 3] = diamond[3, 1] = 1
print(diamond)

imgDilate1 = cv2.dilate(imgGray, cross)  # 用十字型结构元膨胀原图像
imgErode1 = cv2.erode(imgDilate1, diamond)  # 用菱形结构元腐蚀图像

imgDilate2 = cv2.dilate(imgGray, xShape)  # 使用 X 形结构元膨胀原图像
imgErode2 = cv2.erode(imgDilate2, square)  # 使用方形结构元腐蚀图像

imgDiff = cv2.absdiff(imgErode2, imgErode1)  # 将两幅闭运算的图像相减获得角点
retval, thresh = cv2.threshold(imgDiff, 40, 255, cv2.THRESH_BINARY)  # # 二值化处理

# 在原图上用半径为 5 的圆圈标记角点
for j in range(thresh.size):
    y = int(j / thresh.shape[0])
    x = int(j % thresh.shape[0])
    if (thresh[x, y] == 255):
        cv2.circle(imgSign, (y, x), 5, (255, 0, 255))

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("Origin"), plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.title("Edge"), plt.axis('off')
plt.imshow(imgEdge, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title("Corner"), plt.axis('off')
plt.imshow(cv2.cvtColor(imgSign, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
