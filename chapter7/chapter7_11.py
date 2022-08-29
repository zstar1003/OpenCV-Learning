"""
修正阿尔法均值滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena_noise.jpg", 0)

img_h = img.shape[0]
img_w = img.shape[1]

m, n = 5, 5
kernalMean = np.ones((m, n), np.float32)  # 生成盒式核

# 边缘填充
hPad = int((m - 1) / 2)
wPad = int((n - 1) / 2)
imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")

imgAlphaFilter0 = np.zeros(img.shape)
imgAlphaFilter1 = np.zeros(img.shape)
imgAlphaFilter2 = np.zeros(img.shape)
for i in range(img_h):
    for j in range(img_w):
        # 邻域 m * n
        pad = imgPad[i:i + m, j:j + n]
        padSort = np.sort(pad.flatten())  # 对邻域像素按灰度值排序

        d = 1
        sumAlpha = np.sum(padSort[d:m * n - d - 1])  # 删除 d 个最大灰度值, d 个最小灰度值
        imgAlphaFilter0[i, j] = sumAlpha / (m * n - 2 * d)  # 对剩余像素进行算术平均

        d = 2
        sumAlpha = np.sum(padSort[d:m * n - d - 1])
        imgAlphaFilter1[i, j] = sumAlpha / (m * n - 2 * d)

        d = 4
        sumAlpha = np.sum(padSort[d:m * n - d - 1])
        imgAlphaFilter2[i, j] = sumAlpha / (m * n - 2 * d)

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(222), plt.axis('off'), plt.title("Modified alpha-mean(d=1)")
plt.imshow(imgAlphaFilter0, cmap='gray', vmin=0, vmax=255)
plt.subplot(223), plt.axis('off'), plt.title("Modified alpha-mean(d=2)")
plt.imshow(imgAlphaFilter1, cmap='gray', vmin=0, vmax=255)
plt.subplot(224), plt.axis('off'), plt.title("Modified alpha-mean(d=4)")
plt.imshow(imgAlphaFilter2, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
