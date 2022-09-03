"""
图像分割之区域生长
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


def getGrayDiff(image, currentPoint, tmpPoint):  # 求两个像素的距离
    return abs(int(image[currentPoint[0], currentPoint[1]]) - int(image[tmpPoint[0], tmpPoint[1]]))


# 区域生长算法
def regional_growth(img, seeds, thresh=5):
    height, weight = img.shape
    seedMark = np.zeros(img.shape)
    seedList = []
    for seed in seeds:
        if (0 < seed[0] < height and 0 < seed[1] < weight): seedList.append(seed)
    label = 1  # 种子位置标记
    connects = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]  # 8 邻接连通
    while (len(seedList) > 0):  # 如果列表里还存在点
        currentPoint = seedList.pop(0)  # 将最前面的那个抛出
        seedMark[currentPoint[0], currentPoint[1]] = label  # 将对应位置的点标记为 1
        for i in range(8):  # 对这个点周围的8个点一次进行相似性判断
            tmpX = currentPoint[0] + connects[i][0]
            tmpY = currentPoint[1] + connects[i][1]
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:  # 是否超出限定阈值
                continue
            grayDiff = getGrayDiff(img, currentPoint, (tmpX, tmpY))  # 计算灰度差
            if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
                seedMark[tmpX, tmpY] = label
                seedList.append((tmpX, tmpY))
    return seedMark


img = cv2.imread("../img/lena.jpg", flags=0)
# histCV = cv2.calcHist([img], [0], None, [256], [0, 256])  # 灰度直方图
# OTSU 全局阈值处理
ret, imgOtsu = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)  # 阈值分割, thresh=T
# 自适应局部阈值处理
binaryMean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
# 区域生长图像分割
# seeds = [(10, 10), (82, 150), (20, 300)]  # 直接给定 种子点
imgBlur = cv2.blur(img, (3, 3))  # cv2.blur 方法
_, imgTop = cv2.threshold(imgBlur, 250, 255, cv2.THRESH_BINARY)  # 高百分位阈值产生种子区域
nseeds, labels, stats, centroids = cv2.connectedComponentsWithStats(imgTop)  # 过滤连通域，获得质心点 (x,y)
seeds = centroids.astype(int)  # 获得质心像素作为种子点
imgGrowth = regional_growth(img, seeds, 8)

plt.figure(figsize=(8, 6))
plt.subplot(221), plt.axis('off'), plt.title("Origin")
plt.imshow(img, 'gray')
plt.subplot(222), plt.axis('off'), plt.title("OTSU(T={})".format(ret))
plt.imshow(imgOtsu, 'gray')
plt.subplot(223), plt.axis('off'), plt.title("Adaptive threshold")
plt.imshow(binaryMean, 'gray')
plt.subplot(224), plt.axis('off'), plt.title("Region grow")
plt.imshow(255 - imgGrowth, 'gray')
plt.tight_layout()
plt.show()
