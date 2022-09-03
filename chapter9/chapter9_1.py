"""
LoG边缘检测算子
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

img = cv2.imread("../img/lena.jpg", flags=0)


def ZeroDetect(img):  # 判断零交叉点
    h, w = img.shape[0], img.shape[1]
    zeroCrossing = np.zeros_like(img, np.uint8)
    for x in range(0, w - 1):
        for y in range(0, h - 1):
            if img[y][x] < 0:
                if (img[y][x - 1] > 0) or (img[y][x + 1] > 0) \
                        or (img[y - 1][x] > 0) or (img[y + 1][x] > 0):
                    zeroCrossing[y][x] = 255
    return zeroCrossing

imgBlur = cv2.blur(img, (3, 3))  # Blur 平滑后再做 Laplacian 变换

# 近似的 Marr-Hildreth 卷积核 (5*5)
kernel_MH5 = np.array([
    [0, 0, -1, 0, 0],
    [0, -1, -2, -1, 0],
    [-1, -2, 16, -2, -1],
    [0, -1, -2, -1, 0],
    [0, 0, -1, 0, 0]])
imgMH5 = signal.convolve2d(imgBlur, kernel_MH5, boundary='symm', mode='same')  # 卷积计算
zeroMH5 = ZeroDetect(imgMH5)  # 判断零交叉点

# 由 Gauss 标准差计算 Marr-Hildreth 卷积核
sigma = 3  # Gauss 标准差，输入参数
size = int(2 * round(3 * sigma)) + 1  # 根据标准差确定窗口大小，3*sigma 占比 99.7%
print("sigma={:d}, size={}".format(sigma, size))
x, y = np.meshgrid(np.arange(-size / 2 + 1, size / 2 + 1), np.arange(-size / 2 + 1, size / 2 + 1))  # 生成网格
norm2 = np.power(x, 2) + np.power(y, 2)
sigma2, sigma4 = np.power(sigma, 2), np.power(sigma, 4)
kernelLoG = ((norm2 - (2.0 * sigma2)) / sigma4) * np.exp(- norm2 / (2.0 * sigma2))  # 计算 LoG 卷积核
# Marr-Hildreth 卷积运算
imgLoG = signal.convolve2d(imgBlur, kernelLoG, boundary='symm', mode='same')  # 卷积计算
# 判断零交叉点
zeroCrossing = ZeroDetect(imgLoG)

plt.figure(figsize=(10, 7))
plt.subplot(221), plt.title("Marr-Hildreth (sigma=0.5)"), plt.imshow(imgMH5, cmap='gray'), plt.axis('off')
plt.subplot(222), plt.title("Marr-Hildreth (sigma=3)"), plt.imshow(imgLoG, cmap='gray'), plt.axis('off')
plt.subplot(223), plt.title("Zero crossing (size=5)"), plt.imshow(zeroMH5, cmap='gray'), plt.axis('off')
plt.subplot(224), plt.title("Zero crossing (size=19)"), plt.imshow(zeroCrossing, cmap='gray'), plt.axis('off')
plt.tight_layout()
plt.show()
