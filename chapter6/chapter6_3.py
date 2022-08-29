"""
频率域巴特沃斯低通滤波器
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

imgGray = cv2.imread("../img/lena.jpg", flags=0)

imgFloat32 = np.float32(imgGray)  # 将图像转换成 float32
rows, cols = imgGray.shape[:2]  # 图片的高度和宽度

# (2) 中心化, centralized 2d array f(x,y) * (-1)^(x+y)
mask = np.ones(imgGray.shape)
mask[1::2, ::2] = -1
mask[::2, 1::2] = -1
fImage = imgFloat32 * mask  # f(x,y) * (-1)^(x+y)

# (3) 快速傅里叶变换
# dftImage = fft2Image(fImage)  # 快速傅里叶变换 (rPad, cPad, 2)
rPadded = cv2.getOptimalDFTSize(rows)  # 最优 DFT 扩充尺寸
cPadded = cv2.getOptimalDFTSize(cols)  # 用于快速傅里叶变换
dftImage = np.zeros((rPadded, cPadded, 2), np.float32)  # 对原始图像进行边缘扩充
dftImage[:rows, :cols, 0] = fImage  # 边缘扩充，下侧和右侧补0
cv2.dft(dftImage, dftImage, cv2.DFT_COMPLEX_OUTPUT)  # 快速傅里叶变换

dftAmp = cv2.magnitude(dftImage[:, :, 0], dftImage[:, :, 1])  # 傅里叶变换的幅度谱 (rPad, cPad)
dftAmpLog = np.log(1.0 + dftAmp)  # 幅度谱对数变换，以便于显示
dftAmpNorm = np.uint8(cv2.normalize(dftAmpLog, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(dftAmp)  # 找到傅里叶谱最大值的位置

plt.figure(figsize=(9, 6))
# rows, cols = imgGray.shape[:2]  # 图片的高度和宽度
u, v = np.mgrid[0:rPadded:1, 0:cPadded:1]
D = np.sqrt(np.power((u - maxLoc[1]), 2) + np.power((v - maxLoc[0]), 2))
D0 = [20, 40, 80]  # cut-off frequency
n = 2
for k in range(3):
    # (4) 构建低通滤波器 传递函数
    # 巴特沃斯低通滤波 (Butterworth low pass filter)
    epsilon = 1e-8  # 防止被 0 除
    lpFilter = 1.0 / (1.0 + np.power(D / (D0[k] + epsilon), 2 * n))

    # (5) 在频率域修改傅里叶变换: 傅里叶变换 点乘 低通滤波器
    dftLPfilter = np.zeros(dftImage.shape, dftImage.dtype)  # 快速傅里叶变换的尺寸(优化尺寸)
    for j in range(2):
        dftLPfilter[:rPadded, :cPadded, j] = dftImage[:rPadded, :cPadded, j] * lpFilter

    # (6) 对低通傅里叶变换 执行傅里叶逆变换，并只取实部
    idft = np.zeros(dftAmp.shape, np.float32)  # 快速傅里叶变换的尺寸(优化尺寸)
    cv2.dft(dftLPfilter, idft, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)

    # (7) 中心化, centralized 2d array g(x,y) * (-1)^(x+y)
    mask2 = np.ones(dftAmp.shape)
    mask2[1::2, ::2] = -1
    mask2[::2, 1::2] = -1
    idftCen = idft * mask2  # g(x,y) * (-1)^(x+y)

    # (8) 截取左上角，大小和输入图像相等
    result = np.clip(idftCen, 0, 255)  # 截断函数，将数值限制在 [0,255]
    imgBLPF = result.astype(np.uint8)
    imgBLPF = imgBLPF[:rows, :cols]

    plt.subplot(2, 3, k + 1), plt.title("BLPF mask(D0={})".format(D0[k])), plt.axis('off')
    plt.imshow(lpFilter[:, :], cmap='gray')
    plt.subplot(2, 3, k + 4), plt.title("BLPF rebuild(D0={})".format(D0[k])), plt.axis('off')
    plt.imshow(imgBLPF, cmap='gray')

plt.tight_layout()
plt.show()
