"""
频率域高通滤波器-图片
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


def dft2Image(image):  # 最优扩充的快速傅立叶变换
    # 中心化, centralized 2d array f(x,y) * (-1)^(x+y)
    mask = np.ones(image.shape)
    mask[1::2, ::2] = -1
    mask[::2, 1::2] = -1
    fImage = image * mask  # f(x,y) * (-1)^(x+y)

    # 最优 DFT 扩充尺寸
    rows, cols = image.shape[:2]  # 原始图片的高度和宽度
    rPadded = cv2.getOptimalDFTSize(rows)  # 最优 DFT 扩充尺寸
    cPadded = cv2.getOptimalDFTSize(cols)  # 用于快速傅里叶变换

    # 边缘扩充(补0), 快速傅里叶变换
    dftImage = np.zeros((rPadded, cPadded, 2), np.float32)  # 对原始图像进行边缘扩充
    dftImage[:rows, :cols, 0] = fImage  # 边缘扩充，下侧和右侧补0
    cv2.dft(dftImage, dftImage, cv2.DFT_COMPLEX_OUTPUT)  # 快速傅里叶变换
    return dftImage


# (1) 读取原始图像
imgGray = cv2.imread("../img/lena.jpg", flags=0)
rows, cols = imgGray.shape[:2]  # 图片的高度和宽度

plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1), plt.title("Original"), plt.axis('off'), plt.imshow(imgGray, cmap='gray')

# (2) 快速傅里叶变换
dftImage = dft2Image(imgGray)  # 快速傅里叶变换 (rPad, cPad, 2)
rPadded, cPadded = dftImage.shape[:2]  # 快速傅里叶变换的尺寸, 原始图像尺寸优化

D0 = [20, 40, 80, 120, 160]  # radius
for k in range(5):
    # (3) 构建高通滤波器
    # hpFilter = ideaHighPassFilter((rPadded, cPadded), radius=D0[k])  # 理想高通滤波器
    # hpFilter = gaussHighPassFilter((rPadded, cPadded), radius=D0[k])  # 高斯高通滤波器
    hpFilter = butterworthHighPassFilter((rPadded, cPadded), radius=D0[k])  # 巴特沃斯高通滤波器

    # (5) 在频率域修改傅里叶变换: 傅里叶变换 点乘 低通滤波器
    dftHPfilter = np.zeros(dftImage.shape, dftImage.dtype)  # 快速傅里叶变换的尺寸(优化尺寸)
    for j in range(2):
        dftHPfilter[:rPadded, :cPadded, j] = dftImage[:rPadded, :cPadded, j] * hpFilter

    # (6) 对高通傅里叶变换 执行傅里叶逆变换，并只取实部
    idft = np.zeros(dftImage.shape[:2], np.float32)  # 快速傅里叶变换的尺寸(优化尺寸)
    cv2.dft(dftHPfilter, idft, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)

    # (7) 中心化, centralized 2d array g(x,y) * (-1)^(x+y)
    mask2 = np.ones(dftImage.shape[:2])
    mask2[1::2, ::2] = -1
    mask2[::2, 1::2] = -1
    idftCen = idft * mask2  # g(x,y) * (-1)^(x+y)

    # (8) 截取左上角，大小和输入图像相等
    result = np.clip(idftCen, 0, 255)  # 截断函数，将数值限制在 [0,255]
    imgHPF = result.astype(np.uint8)
    imgHPF = imgHPF[:rows, :cols]

    plt.subplot(2, 3, k + 2), plt.title("HPFilter rebuild(n={})".format(D0[k])), plt.axis('off')
    plt.imshow(imgHPF, cmap='gray')

plt.tight_layout()
plt.show()
