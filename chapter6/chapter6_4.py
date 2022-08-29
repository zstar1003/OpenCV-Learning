"""
频率域高通滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


def ideaHighPassFilter(shape, radius=10):  # 理想高通滤波器
    u, v = np.mgrid[-1:1:2.0 / shape[0], -1:1:2.0 / shape[1]]
    D = np.sqrt(u ** 2 + v ** 2)
    D0 = radius / shape[0]
    kernel = np.ones(shape)
    kernel[D <= D0] = 0  # 理想低通滤波 (Idea low pass filter)
    return kernel


def gaussHighPassFilter(shape, radius=10):  # 高斯高通滤波器
    # 高斯滤波器：# Gauss = 1/(2*pi*s2) * exp(-(x**2+y**2)/(2*s2))
    u, v = np.mgrid[-1:1:2.0 / shape[0], -1:1:2.0 / shape[1]]
    D = np.sqrt(u ** 2 + v ** 2)
    D0 = radius / shape[0]
    kernel = 1 - np.exp(- (D ** 2) / (2 * D0 ** 2))
    return kernel


def butterworthHighPassFilter(shape, radius=10, n=2):  # 巴特沃斯高通滤波
    u, v = np.mgrid[-1:1:2.0 / shape[0], -1:1:2.0 / shape[1]]
    epsilon = 1e-8
    D = np.sqrt(u ** 2 + v ** 2)
    D0 = radius / shape[0]
    kernel = 1.0 / (1.0 + np.power(D0 / (D + epsilon), 2 * n))

    return kernel


# 理想、高斯、巴特沃斯高通传递函数
shape = [128, 128]
radius = 32
IHPF = ideaHighPassFilter(shape, radius=radius)
GHPF = gaussHighPassFilter(shape, radius=radius)
BHPF = butterworthHighPassFilter(shape, radius=radius)

filters = ['IHPF', 'GHPF', 'BHPF']
u, v = np.mgrid[-1:1:2.0 / shape[0], -1:1:2.0 / shape[1]]
fig = plt.figure(figsize=(10, 8))
for i in range(3):
    hpFilter = eval(filters[i]).copy()

    ax1 = fig.add_subplot(3, 3, 3 * i + 1)
    ax1.imshow(hpFilter, 'gray')
    ax1.set_title(filters[i]), ax1.set_xticks([]), ax1.set_yticks([])

    ax2 = plt.subplot(3, 3, 3 * i + 2, projection='3d')
    ax2.set_title("transfer function")
    ax2.plot_wireframe(u, v, hpFilter, rstride=2, linewidth=0.5, color='c')
    ax2.set_xticks([]), ax2.set_yticks([]), ax2.set_zticks([])

    ax3 = plt.subplot(3, 3, 3 * i + 3)
    profile = hpFilter[shape[0] // 2:, shape[1] // 2]
    ax3.plot(profile), ax3.set_title("profile"), ax3.set_xticks([]), ax3.set_yticks([])

plt.show()
