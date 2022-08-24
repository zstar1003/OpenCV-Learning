"""
局部直方图均衡化
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/lena.jpg", flags=0)  # flags=0 读取为灰度图像

imgEqu = cv2.equalizeHist(img)  # 全局直方图均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))  # 创建 CLAHE 对象
imgLocalEqu = clahe.apply(img)  # 自适应的局部直方图均衡化

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title('Original'), plt.axis('off')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.title(f'Global Equalize Hist'), plt.axis('off')
plt.imshow(imgEqu, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.title(f'Local Equalize Hist'), plt.axis('off')
plt.imshow(imgLocalEqu, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
