"""
伽马噪声
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", 0)

a, b = 10.0, 2.5
noiseGamma = np.random.gamma(shape=b, scale=a, size=img.shape)
imgGammaNoise = img + noiseGamma
imgGammaNoise = np.uint8(cv2.normalize(imgGammaNoise, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]

plt.figure(figsize=(9, 3))
plt.subplot(131), plt.title("Origin"), plt.axis('off')
plt.imshow(img, 'gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Gamma noise"), plt.axis('off')
plt.imshow(imgGammaNoise, 'gray')
plt.subplot(133), plt.title("Gray hist")
histNP, bins = np.histogram(imgGammaNoise.flatten(), bins=255, range=[0, 255], density=True)
plt.bar(bins[:-1], histNP[:])
plt.tight_layout()
plt.show()