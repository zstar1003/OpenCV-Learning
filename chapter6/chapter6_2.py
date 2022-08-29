"""
频率域高斯低通滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

imgGray = cv2.imread("../img/lena.jpg", flags=0)

# （1）首先对图像进行傅里叶变换
imgFloat32 = np.float32(imgGray)  # 将图像转换成 float32
dft = cv2.dft(imgFloat32, flags=cv2.DFT_COMPLEX_OUTPUT)  # 傅里叶变换
dftShift = np.fft.fftshift(dft)  # 将低频分量移动到频域图像的中心

plt.figure(figsize=(9, 6))
rows, cols = imgGray.shape[:2]  # 图片的高度和宽度
sigma2 = [0.5, 0.09, 0.01]  # square of sigma
for i in range(3):
    # 构造高斯滤波器遮罩
    x, y = np.mgrid[-1:1:2.0 / rows, -1:1:2.0 / cols]
    z = 1 / (2 * np.pi * sigma2[i]) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma2[i]))
    zNorm = np.uint8(cv2.normalize(z, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]
    maskGauss = np.zeros((rows, cols, 2), np.uint8)
    maskGauss[:, :, 0] = zNorm
    maskGauss[:, :, 1] = zNorm
    # （2）然后在频率域修改傅里叶变换
    dftTrans = dftShift * maskGauss  # 修改傅里叶变换实现滤波
    # （3）最后通过傅里叶逆变换返回空间域
    ishift = np.fft.ifftshift(dftTrans)  # 将低频逆转换回图像四角
    idft = cv2.idft(ishift)  # 逆傅里叶变换
    imgRebuild = cv2.magnitude(idft[:, :, 0], idft[:, :, 1])  # 重建图像

    plt.subplot(2, 3, i + 1), plt.title("Mask (s^2={})".format(sigma2[i])), plt.axis('off')
    plt.imshow(maskGauss[:, :, 0], cmap='gray')
    plt.subplot(2, 3, i + 4), plt.title("DFT GLPF (s^2={})".format(sigma2[i])), plt.axis('off')
    plt.imshow(imgRebuild, cmap='gray')

plt.tight_layout()
plt.show()
