"""
图像二维卷积
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)  # # flags=0 读取为灰度图像

kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])  # Gx + j*Gy

kFlip = cv2.flip(kernel, -1)  # 将卷积核旋转180度
# 使用函数filter2D算出same卷积
imgConv1 = cv2.filter2D(img, -1, kFlip,
                        anchor=(0, 0), borderType=cv2.BORDER_CONSTANT)
imgConv2 = cv2.filter2D(img, -1, kFlip,
                        anchor=(0, 0), borderType=cv2.BORDER_REFLECT)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title('Original'), plt.axis('off')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.axis('off'), plt.title('cv2.filter2D (BORDER_CONSTANT)')
plt.imshow(np.absolute(imgConv1), cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.axis('off'), plt.title('cv2.filter2D (BORDER_REFLECT)')
plt.imshow(np.absolute(imgConv2), cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()

