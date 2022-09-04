"""
添加水印
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/lena.jpg", 1)  # 加载原始图片
h, w = img.shape[0], img.shape[1]

# 生成水印图案
logo = cv.imread("../img/img.jpg", 0)  # 加载 Logo
logoResize = cv.resize(logo, (200, 200))  # 调整图片尺寸
grayMark = np.zeros(img.shape[:2], np.uint8)  # 水印黑色背景
grayMark[10:210, 10:210] = logoResize  # 生成水印图案

# 生成文字水印
mark = np.zeros(img.shape[:2], np.uint8)  # 黑色背景
for i in range(h // 100):
    cv.putText(mark, "zstar", (50, 70 + 100 * i), cv.FONT_HERSHEY_SIMPLEX, 1.5, 255, 2)
MAR = cv.getRotationMatrix2D((w // 2, h // 2), 45, 1.0)  # 旋转 45 度
grayMark2 = cv.warpAffine(mark, MAR, (w, h))  # 旋转变换，默认为黑色填充

# 添加图片水印
markC3 = cv.merge([grayMark, grayMark, grayMark])
imgMark1 = cv.addWeighted(img, 1, markC3, 0.25, 0)  # 加权加法图像融合

# 添加文字水印
markC32 = cv.merge([grayMark2, grayMark2, grayMark2])
imgMark2 = cv.addWeighted(img, 1, markC32, 0.25, 0)  # 加权加法图像融合


plt.figure(figsize=(9, 6))
plt.subplot(221), plt.title("original"), plt.axis('off')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(222), plt.title("watermark"), plt.axis('off')
plt.imshow(cv.cvtColor(markC3, cv.COLOR_BGR2RGB))
plt.subplot(223), plt.title("watermark embedded"), plt.axis('off')
plt.imshow(cv.cvtColor(imgMark1, cv.COLOR_BGR2RGB))
plt.subplot(224), plt.title("watermark embedded"), plt.axis('off')
plt.imshow(cv.cvtColor(imgMark2, cv.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
