"""
统计排序滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena_noise.jpg", 0)

img_h = img.shape[0]
img_w = img.shape[1]

m, n = 3, 3
kernalMean = np.ones((m, n), np.float32)  # 生成盒式核

# 边缘填充
hPad = int((m - 1) / 2)
wPad = int((n - 1) / 2)
imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")

imgMedianFilter = np.zeros(img.shape)  # 中值滤波器
imgMaxFilter = np.zeros(img.shape)  # 最大值滤波器
imgMinFilter = np.zeros(img.shape)  # 最小值滤波器
imgMiddleFilter = np.zeros(img.shape)  # 中点滤波器
for i in range(img_h):
    for j in range(img_w):
        # # 1. 中值滤波器 (median filter)
        pad = imgPad[i:i + m, j:j + n]
        imgMedianFilter[i, j] = np.median(pad)

        # # 2. 最大值滤波器 (maximum filter)
        pad = imgPad[i:i + m, j:j + n]
        imgMaxFilter[i, j] = np.max(pad)

        # # 3. 最小值滤波器 (minimum filter)
        pad = imgPad[i:i + m, j:j + n]
        imgMinFilter[i, j] = np.min(pad)

        # # 4. 中点滤波器 (middle filter)
        pad = imgPad[i:i + m, j:j + n]
        imgMiddleFilter[i, j] = int(pad.max() / 2 + pad.min() / 2)

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.axis('off'), plt.title("median filter")
plt.imshow(imgMedianFilter, cmap='gray', vmin=0, vmax=255)
plt.subplot(222), plt.axis('off'), plt.title("maximum filter")
plt.imshow(imgMaxFilter, cmap='gray', vmin=0, vmax=255)
plt.subplot(223), plt.axis('off'), plt.title("minimum filter")
plt.imshow(imgMinFilter, cmap='gray', vmin=0, vmax=255)
plt.subplot(224), plt.axis('off'), plt.title("middle filter")
plt.imshow(imgMiddleFilter, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
