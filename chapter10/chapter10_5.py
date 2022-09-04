"""
绘制直线
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

height, width, channels = 200, 120, 3
img = np.ones((height, width, channels), np.uint8) * 160  # 创建黑色图像 RGB=0

# 注意 pt1, pt2 坐标的格式是 (x,y) 而不是 (y,x)
img1 = img.copy()
cv.line(img1, (0, 0), (200, 150), (0, 0, 255), 1)  # 红色 R=255
cv.line(img1, (0, 0), (150, 200), (0, 255, 0), 1)  # 绿色 G=255
cv.line(img1, (0, 50), (200, 50), (128, 0, 0), 2)  # 深蓝色 B = 128
cv.line(img1, (0, 100), (200, 100), 128, 2)  # color=128 等效于 (128,0,0)
cv.line(img1, (0, 150), (200, 150), 255, 2)  # color=255 等效于 (255,0,0)

# img2 = img.copy()
# tipLength 指箭头部分长度与整个线段长度的比例
img2 = cv.arrowedLine(img.copy(), (10, 0), (100, 30), (0, 0, 255), tipLength=0.05)  # 从 pt1 指向 pt2
img2 = cv.arrowedLine(img2, (10, 50), (100, 80), (0, 0, 255), tipLength=0.1)
img2 = cv.arrowedLine(img2, (10, 100), (100, 130), (0, 0, 255), tipLength=0.2)  # 双向箭头
img2 = cv.arrowedLine(img2, (100, 130), (10, 100), (0, 0, 255), tipLength=0.2)  # 双向箭头
img2 = cv.arrowedLine(img2, (10, 150), (200, 200), (0, 0, 255), tipLength=0.1)  # 终点越界，箭头不显示

# 绘制直线可以用于灰度图像，参数 color 只有第一通道值有效，并被设为灰度值
gray = np.zeros((height, width), np.uint8)  # 创建灰度图像
img3 = cv.line(gray, (0, 10), (200, 10), (0, 255, 255), 2)
img3 = cv.line(gray, (0, 30), (200, 30), (64, 128, 255), 2)
img3 = cv.line(gray, (0, 60), (200, 60), (128, 64, 255), 2)
img3 = cv.line(gray, (0, 100), (200, 100), (255, 0, 255), 2)
img3 = cv.line(gray, (20, 0), (20, 200), 128, 2)
img3 = cv.line(gray, (60, 0), (60, 200), (255, 0, 0), 2)
img3 = cv.line(gray, (100, 0), (100, 200), (255, 255, 255), 2)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("img1"), plt.axis('off')
plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
plt.subplot(132), plt.title("img2"), plt.axis('off')
plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
plt.subplot(133), plt.title("img3"), plt.axis('off')
plt.imshow(img3, cmap="gray")
plt.tight_layout()
plt.show()
