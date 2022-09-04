"""
绘制矩形
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

height, width, channels = 400, 300, 3
img = np.ones((height, width, channels), np.uint8) * 160  # 创建黑色图像 RGB=0

img1 = img.copy()
cv.rectangle(img1, (0, 20), (100, 200), (255, 255, 255))  # 白色
cv.rectangle(img1, (20, 0), (300, 100), (255, 0, 0), 2)  # 蓝色 B=255
cv.rectangle(img1, (300, 400), (250, 300), (0, 255, 0), -1)  # 绿色，填充
cv.rectangle(img1, (0, 400), (50, 300), 255, -1)  # color=255 蓝色
cv.rectangle(img1, (20, 220), (25, 225), (0, 0, 255), 4)  # 线宽的影响
cv.rectangle(img1, (60, 220), (67, 227), (0, 0, 255), 4)
cv.rectangle(img1, (100, 220), (109, 229), (0, 0, 255), 4)

img2 = img.copy()
x, y, w, h = (50, 50, 200, 100)  # 左上角坐标 (x,y), 宽度 w，高度 h
cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
text = "({},{}),{}*{}".format(x, y, w, h)
cv.putText(img2, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

# 绘制直线可以用于灰度图像，参数 color 只有第一通道值有效，并被设为灰度值
gray = np.zeros((height, width), np.uint8)  # 创建灰度图像
img3 = cv.line(gray, (0, 10), (300, 10), 64, 2)
cv.line(img3, (0, 30), (300, 30), (128, 128, 255), 2)
cv.line(img3, (0, 60), (300, 60), (192, 64, 255), 2)
cv.rectangle(img3, (0, 200), (30, 150), 128, -1)  # Gray=128
cv.rectangle(img3, (60, 200), (90, 150), (128, 0, 0), -1)  # Gray=128
cv.rectangle(img3, (120, 200), (150, 150), (128, 255, 255), -1)  # Gray=128
cv.rectangle(img3, (180, 200), (210, 150), 192, -1)  # Gray=192
cv.rectangle(img3, (240, 200), (270, 150), 255, -1)  # Gray=255

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("img1"), plt.axis('off')
plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
plt.subplot(132), plt.title("img2"), plt.axis('off')
plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
plt.subplot(133), plt.title("img3"), plt.axis('off')
plt.imshow(img3, cmap="gray")
plt.tight_layout()
plt.show()
