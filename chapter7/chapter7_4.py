"""
均匀噪声
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", 0)

mean, sigma = 10, 100
a = 2 * mean - np.sqrt(12 * sigma)  # a = -14.64
b = 2 * mean + np.sqrt(12 * sigma)  # b = 54.64
noiseUniform = np.random.uniform(a, b, img.shape)
imgUniformNoise = img + noiseUniform
imgUniformNoise = np.uint8(cv2.normalize(imgUniformNoise, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]

plt.figure(figsize=(9, 3))
plt.subplot(131), plt.title("Origin"), plt.axis('off')
plt.imshow(img, 'gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Uniform noise"), plt.axis('off')
plt.imshow(imgUniformNoise, 'gray')
plt.subplot(133), plt.title("Gray hist")
histNP, bins = np.histogram(imgUniformNoise.flatten(), bins=255, range=[0, 255], density=True)
plt.bar(bins[:-1], histNP[:])
plt.tight_layout()
plt.show()