"""
灰度线性变换
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 颜色转换：BGR(OpenCV) -> Gray
h, w = img.shape[:2]  # 图片的高度和宽度
img1 = np.empty((w, h), np.uint8)  # 创建空白数组
img2 = np.empty((w, h), np.uint8)  # 创建空白数组
img3 = np.empty((w, h), np.uint8)  # 创建空白数组
img4 = np.empty((w, h), np.uint8)  # 创建空白数组
img5 = np.empty((w, h), np.uint8)  # 创建空白数组
img6 = np.empty((w, h), np.uint8)  # 创建空白数组

# Dt[i,j] = alfa*D[i,j] + beta
alfa1, beta1 = 1, 50  # alfa=1,beta>0: 灰度值上移
alfa2, beta2 = 1, -50  # alfa=1,beta<0: 灰度值下移
alfa3, beta3 = 1.5, 0  # alfa>1,beta=0: 对比度增强
alfa4, beta4 = 0.75, 0  # 0<alfa<1,beta=0: 对比度减小
alfa5, beta5 = -0.5, 0  # alfa<0,beta=0: 暗区域变亮，亮区域变暗
alfa6, beta6 = -1, 255  # alfa=-1,beta=255: 灰度值反转

for i in range(h):
    for j in range(w):
        img1[i][j] = min(255, max((imgGray[i][j] + beta1), 0))  # alfa=1,beta>0: 颜色发白
        img2[i][j] = min(255, max((imgGray[i][j] + beta2), 0))  # alfa=1,beta<0: 颜色发黑
        img3[i][j] = min(255, max(alfa3 * imgGray[i][j], 0))  # alfa>1,beta=0: 对比度增强
        img4[i][j] = min(255, max(alfa4 * imgGray[i][j], 0))  # 0<alfa<1,beta=0: 对比度减小
        img5[i][j] = alfa5 * imgGray[i][j] + beta5  # alfa<0,beta=255: 暗区域变亮，亮区域变暗
        img6[i][j] = min(255, max(alfa6 * imgGray[i][j] + beta6, 0))  # alfa=-1,beta=255: 灰度值反转

plt.figure(figsize=(10, 6))
titleList = ["1. imgGray", "2. beta=50", "3. beta=-50", "4. alfa=1.5", "5. alfa=0.75", "6. alfa=-0.5"]
imageList = [imgGray, img1, img2, img3, img4, img5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.title(titleList[i]), plt.axis('off')
    plt.imshow(imageList[i], vmin=0, vmax=255, cmap='gray')
plt.show()
