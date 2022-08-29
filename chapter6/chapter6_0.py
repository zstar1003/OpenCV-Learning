"""
离散傅里叶变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

imgGray = cv2.imread("../img/lena.jpg", flags=0)

# cv2.dft 实现图像的傅里叶变换
imgFloat32 = np.float32(imgGray)  # 将图像转换成 float32
dft = cv2.dft(imgFloat32, flags=cv2.DFT_COMPLEX_OUTPUT)  # 傅里叶变换
dftShift = np.fft.fftshift(dft)  # 将低频分量移动到频域图像的中心

# 相位谱
phase = np.arctan2(dftShift[:, :, 1], dftShift[:, :, 0])  # 计算相位角(弧度制)
dftPhi = phase / np.pi * 180  # 将相位角转换为 [-180, 180]

# cv2.idft 实现图像的逆傅里叶变换
invShift = np.fft.ifftshift(dftShift)  # 将低频逆转换回图像四角
imgIdft = cv2.idft(invShift)  # 逆傅里叶变换
imgRebuild = cv2.magnitude(imgIdft[:, :, 0], imgIdft[:, :, 1])  # 重建图像

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("Original image"), plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.subplot(132), plt.title("DFT Phase"), plt.axis('off')
plt.imshow(dftPhi, cmap='gray')
plt.subplot(133), plt.title("Rebuild image with IDFT"), plt.axis('off')
plt.imshow(imgRebuild, cmap='gray')
plt.tight_layout()
plt.show()
