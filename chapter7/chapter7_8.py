"""
谐波平均滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena_noise.jpg", 0)

img_h = img.shape[0]
img_w = img.shape[1]

# 算术平均滤波 (Arithmentic mean filter)
kSize = (3, 3)
kernalMean = np.ones(kSize, np.float32) / (kSize[0] * kSize[1])  # 生成归一化盒式核
imgAriMean = cv2.filter2D(img, -1, kernalMean)

# 谐波平均滤波器 (Harmonic mean filter)
m, n = 3, 3
order = m * n
kernalMean = np.ones((m, n), np.float32)  # 生成盒式核

hPad = int((m - 1) / 2)
wPad = int((n - 1) / 2)
imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")

epsilon = 1e-8
imgHarMean = img.copy()
for i in range(hPad, img_h + hPad):
    for j in range(wPad, img_w + wPad):
        sumTemp = np.sum(1.0 / (imgPad[i - hPad:i + hPad + 1, j - wPad:j + wPad + 1] + epsilon))
        imgHarMean[i - hPad][j - wPad] = order / sumTemp

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.axis('off'), plt.title("Arithmentic mean filter")
plt.imshow(imgAriMean, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.axis('off'), plt.title("Harmonic mean filter")
plt.imshow(imgHarMean, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
