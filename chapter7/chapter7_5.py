"""
椒盐噪声
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", 0)

ps, pp = 0.05, 0.02
mask = np.random.choice((0, 0.5, 1), size=img.shape[:2], p=[pp, (1 - ps - pp), ps])
imgChoiceNoise = img.copy()
imgChoiceNoise[mask == 1] = 255
imgChoiceNoise[mask == 0] = 0

plt.figure(figsize=(9, 3))
plt.subplot(131), plt.title("Origin"), plt.axis('off')
plt.imshow(img, 'gray', vmin=0, vmax=255)
plt.subplot(132), plt.title("Choice noise"), plt.axis('off')
plt.imshow(imgChoiceNoise, 'gray')
plt.subplot(133), plt.title("Gray hist")
histNP, bins = np.histogram(imgChoiceNoise.flatten(), bins=255, range=[0, 255], density=True)
plt.bar(bins[:-1], histNP[:])
plt.tight_layout()
plt.show()
