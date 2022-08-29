"""
指数噪声
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", 0)

a = 10.0
noiseExponent = np.random.exponential(scale=a, size=img.shape)
imgExponentNoise = img + noiseExponent
imgExponentNoise = np.uint8(cv2.normalize(imgExponentNoise, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]

plt.figure(figsize=(9, 3))
plt.subplot(131), plt.title("Origin"), plt.axis('off')
plt.imshow(img, 'gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Exponential noise"), plt.axis('off')
plt.imshow(imgExponentNoise, 'gray')
plt.subplot(133), plt.title("Gray hist")
histNP, bins = np.histogram(imgExponentNoise.flatten(), bins=255, range=[0, 255], density=True)
plt.bar(bins[:-1], histNP[:])
plt.tight_layout()
plt.show()
