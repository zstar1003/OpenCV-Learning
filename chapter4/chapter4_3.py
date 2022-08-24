"""
伽马变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/img.jpg", flags=0)  # flags=0 读取为灰度图像
gammaList = [0.125, 0.25, 0.5, 1.0, 2.0, 4.0]  # gamma 值
normImg = lambda x: 255. * (x - x.min()) / (x.max() - x.min() + 1e-6)  # 归一化为 [0,255]

plt.figure(figsize=(9, 6))
for k in range(len(gammaList)):
    imgGamma = np.power(img, gammaList[k])
    imgGamma = np.uint8(normImg(imgGamma))

    plt.subplot(2, 3, k + 1), plt.axis('off')
    plt.imshow(imgGamma, cmap='gray', vmin=0, vmax=255)
    plt.title(f"$\gamma={gammaList[k]}$")
plt.show()
