"""
图像分割之区域分离
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


def SplitMerge(src, dst, h, w, h0, w0, maxMean, minVar, cell=4):
    win = src[h0: h0 + h, w0: w0 + w]
    mean = np.mean(win)  # 窗口区域的均值
    var = np.std(win, ddof=1)  # 窗口区域的标准差，无偏样本标准差

    if (mean < maxMean) and (var > minVar) and (h < 2 * cell) and (w < 2 * cell):
        # 该区域满足谓词逻辑条件，判为目标区域，设为白色
        dst[h0:h0 + h, w0:w0 + w] = 255  # 白色
        # print("h0={}, w0={}, h={}, w={}, mean={:.2f}, var={:.2f}".
        #       format(h0, w0, h, w, mean, var))
    else:  # 该区域不满足谓词逻辑条件
        if (h > cell) and (w > cell):  # 区域能否继续分拆？继续拆
            SplitMerge(src, dst, (h + 1) // 2, (w + 1) // 2, h0, w0, maxMean, minVar, cell)
            SplitMerge(src, dst, (h + 1) // 2, (w + 1) // 2, h0, w0 + (w + 1) // 2, maxMean, minVar, cell)
            SplitMerge(src, dst, (h + 1) // 2, (w + 1) // 2, h0 + (h + 1) // 2, w0, maxMean, minVar, cell)
            SplitMerge(src, dst, (h + 1) // 2, (w + 1) // 2, h0 + (h + 1) // 2, w0 + (w + 1) // 2, maxMean, minVar,
                       cell)
        # else:  # 不能再分拆，判为非目标区域，设为黑色
        #     src[h0:h0+h, w0:w0+w] = 0  # 黑色


img = cv2.imread("../img/lena.jpg", flags=0)
hImg, wImg = img.shape
mean = np.mean(img)  # 窗口区域的均值
var = np.std(img, ddof=1)  # 窗口区域的标准差，无偏样本标准差
print("h={}, w={}, mean={:.2f}, var={:.2f}".format(hImg, wImg, mean, var))

maxMean = 80  # 均值上界
minVar = 10  # 标准差下界
src = img.copy()
dst1 = np.zeros_like(img)
dst2 = np.zeros_like(img)
dst3 = np.zeros_like(img)
SplitMerge(src, dst1, hImg, wImg, 0, 0, maxMean, minVar, cell=32)  # 最小分割区域 cell=32
SplitMerge(src, dst2, hImg, wImg, 0, 0, maxMean, minVar, cell=16)  # 最小分割区域 cell=16
SplitMerge(src, dst3, hImg, wImg, 0, 0, maxMean, minVar, cell=8)  # 最小分割区域 cell=8

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.axis('off'), plt.title("Origin")
plt.imshow(img, 'gray')
plt.subplot(222), plt.axis('off'), plt.title("Region split (c=32)")
plt.imshow(dst1, 'gray')
plt.subplot(223), plt.axis('off'), plt.title("Region split (c=16)")
plt.imshow(dst2, 'gray')
plt.subplot(224), plt.axis('off'), plt.title("Region split (c=8)")
plt.imshow(dst3, 'gray')
plt.tight_layout()
plt.show()
