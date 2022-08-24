"""
钝化掩蔽
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)

# 对原始图像进行平滑，GaussianBlur(img, size, sigmaX)
imgGauss = cv2.GaussianBlur(img, (5, 5), sigmaX=5)
imgGaussNorm = cv2.normalize(imgGauss, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# 掩蔽模板：从原始图像中减去平滑图像
imgMask = img - imgGaussNorm

passivation1 = img + 0.6 * imgMask  # k<1 减弱钝化掩蔽
imgPas1 = cv2.normalize(passivation1, None, 0, 255, cv2.NORM_MINMAX)
passivation2 = img + imgMask  # k=1 钝化掩蔽
imgPas2 = cv2.normalize(passivation2, None, 0, 255, cv2.NORM_MINMAX)
passivation3 = img + 2 * imgMask  # k>1 高提升滤波
imgPas3 = cv2.normalize(passivation3, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(10, 7))
titleList = ["1. Original", "2. GaussSmooth", "3. MaskTemplate",
             "4. Passivation(k=0.5)", "5. Passivation(k=1.0)", "6. Passivation(k=2.0)"]
imageList = [img, imgGauss, imgMask, imgPas1, imgPas2, imgPas3]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.title(titleList[i]), plt.axis('off')
    plt.imshow(imageList[i], 'gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
