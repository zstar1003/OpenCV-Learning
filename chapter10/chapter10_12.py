"""
添加马赛克
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/lena.jpg", 1)  # 加载原始图片
roi = cv.selectROI(img, showCrosshair=True, fromCenter=False)
x, y, wRoi, hRoi = roi  # 矩形裁剪区域的位置参数
# x, y, wRoi, hRoi = 208, 176, 155, 215  # 矩形裁剪区域
imgROI = img[y:y + hRoi, x:x + wRoi].copy()  # 切片获得矩形裁剪区域

plt.figure(figsize=(9, 6))
plt.subplot(231), plt.title("Original image"), plt.axis('off')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(232), plt.title("Region of interest"), plt.axis('off')
plt.imshow(cv.cvtColor(imgROI, cv.COLOR_BGR2RGB))

mosaic = np.zeros(imgROI.shape, np.uint8)  # ROI 区域
ksize = [5, 10, 20]  # 马赛克块的宽度
for i in range(3):
    k = ksize[i]
    for h in range(0, hRoi, k):
        for w in range(0, wRoi, k):
            color = imgROI[h, w]
            mosaic[h:h + k, w:w + k, :] = color  # 用顶点颜色覆盖马赛克块
    imgMosaic = img.copy()
    imgMosaic[y:y + hRoi, x:x + wRoi] = mosaic
    plt.subplot(2, 3, i + 4), plt.title("Coding image (size={})".format(k)), plt.axis('off')
    plt.imshow(cv.cvtColor(imgMosaic, cv.COLOR_BGR2RGB))

plt.subplot(233), plt.title("Mosaic"), plt.axis('off')
plt.imshow(cv.cvtColor(mosaic, cv.COLOR_BGR2RGB))
plt.show()
