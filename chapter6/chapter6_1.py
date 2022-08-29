"""
快速傅里叶变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

imgGray = cv2.imread("../img/lena.jpg", flags=0)
rows, cols = imgGray.shape[:2]  # 图像的行(高度)/列(宽度)

# 快速傅里叶变换(要对原始图像进行矩阵扩充)
rPad = cv2.getOptimalDFTSize(rows)  # 最优 DFT 扩充尺寸
cPad = cv2.getOptimalDFTSize(cols)  # 用于快速傅里叶变换
imgEx = np.zeros((rPad, cPad, 2), np.float32)  # 对原始图像进行边缘扩充
imgEx[:rows, :cols, 0] = imgGray  # 边缘扩充，下侧和右侧补0
dftImgEx = cv2.dft(imgEx, cv2.DFT_COMPLEX_OUTPUT)  # 快速傅里叶变换

# 傅里叶逆变换
idftImg = cv2.idft(dftImgEx)  # 逆傅里叶变换
idftMag = cv2.magnitude(idftImg[:, :, 0], idftImg[:, :, 1])  # 逆傅里叶变换幅值

# 矩阵裁剪，得到恢复图像
idftMagNorm = np.uint8(cv2.normalize(idftMag, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]
imgRebuild = np.copy(idftMagNorm[:rows, :cols])


plt.figure(figsize=(9, 6))
plt.subplot(131), plt.title("Original image"), plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.subplot(132), plt.title("Log-trans of DFT amp"), plt.axis('off')
dftAmp = cv2.magnitude(dftImgEx[:, :, 0], dftImgEx[:, :, 1])  # 幅度谱，中心化
dftAmpLog = np.log(1 + dftAmp)  # 幅度谱对数变换，以便于显示
plt.imshow(cv2.normalize(dftAmpLog, None, 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(133), plt.title("Rebuild image with IDFT"), plt.axis('off')
plt.imshow(imgRebuild, cmap='gray')
plt.tight_layout()
plt.show()
