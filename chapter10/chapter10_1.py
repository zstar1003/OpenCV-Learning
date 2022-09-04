"""
图像颜色反转
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/img.jpg", flags=1)
h, w, ch = img.shape  # 图片的高度, 宽度 和通道数

timeBegin = cv.getTickCount()
imgInv = np.empty((w, h, ch), np.uint8)  # 创建空白数组
for i in range(h):
    for j in range(w):
        for k in range(ch):
            imgInv[i][j][k] = 255 - img[i][j][k]
timeEnd = cv.getTickCount()
time = (timeEnd - timeBegin) / cv.getTickFrequency()
print("图像反转(for 循环实现): {} s".format(round(time, 4)))

timeBegin = cv.getTickCount()
transTable = np.array([(255 - i) for i in range(256)]).astype("uint8")
invLUT = cv.LUT(img, transTable)
timeEnd = cv.getTickCount()
time = (timeEnd - timeBegin) / cv.getTickFrequency()
print("图像反转(LUT 查表实现): {} s".format(round(time, 4)))

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("img"), plt.axis('off')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(132), plt.title("imgInv"), plt.axis('off')
plt.imshow(cv.cvtColor(imgInv, cv.COLOR_BGR2RGB))
plt.subplot(133), plt.title("invLUT"), plt.axis('off')
plt.imshow(cv.cvtColor(invLUT, cv.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()