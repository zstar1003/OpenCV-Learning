"""
算术平均滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena_noise.jpg", 0)

kSize = (3, 3)
kernalMean = np.ones(kSize, np.float32) / (kSize[0] * kSize[1])  # 生成归一化盒式核
imgConv1 = cv2.filter2D(img, -1, kernalMean)  # cv2.filter2D 方法

kSize = (20, 20)
imgConv3 = cv2.boxFilter(img, -1, kSize)  # cv2.boxFilter 方法 (默认normalize=True)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.axis('off'), plt.title("filter2D(kSize=[3,3])")
plt.imshow(imgConv1, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.axis('off'), plt.title("boxFilter(kSize=[20,20])")
plt.imshow(imgConv3, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
