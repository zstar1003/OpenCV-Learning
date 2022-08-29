"""
反谐波平均滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena_noise.jpg", 0)

img_h = img.shape[0]
img_w = img.shape[1]

m, n = 3, 3
order = m * n
kernalMean = np.ones((m, n), np.float32)  # 生成盒式核

hPad = int((m - 1) / 2)
wPad = int((n - 1) / 2)
imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")

Q = 1.5  # 反谐波平均滤波器 阶数
epsilon = 1e-8
imgHarMean = img.copy()
imgInvHarMean = img.copy()
for i in range(hPad, img_h + hPad):
    for j in range(wPad, img_w + wPad):
        # 谐波平均滤波器 (Harmonic mean filter)
        sumTemp = np.sum(1.0 / (imgPad[i - hPad:i + hPad + 1, j - wPad:j + wPad + 1] + epsilon))
        imgHarMean[i - hPad][j - wPad] = order / sumTemp

        # 反谐波平均滤波器 (Inv-harmonic mean filter)
        temp = imgPad[i - hPad:i + hPad + 1, j - wPad:j + wPad + 1] + epsilon
        imgInvHarMean[i - hPad][j - wPad] = np.sum(np.power(temp, (Q + 1))) / np.sum(np.power(temp, Q) + epsilon)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.axis('off'), plt.title("Harmonic mean filter")
plt.imshow(imgHarMean, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.axis('off'), plt.title("Invert harmonic mean")
plt.imshow(imgInvHarMean, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
