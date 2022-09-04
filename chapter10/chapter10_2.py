"""
色彩风格滤镜
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/img.jpg", flags=1)

# 伪彩色处理
pseudo1 = cv.applyColorMap(img, colormap=cv.COLORMAP_PINK)
pseudo2 = cv.applyColorMap(img, colormap=cv.COLORMAP_JET)
pseudo3 = cv.applyColorMap(img, colormap=cv.COLORMAP_WINTER)
pseudo4 = cv.applyColorMap(img, colormap=cv.COLORMAP_RAINBOW)
pseudo5 = cv.applyColorMap(img, colormap=cv.COLORMAP_HOT)

plt.figure(figsize=(9, 6))
plt.subplot(231), plt.axis('off'), plt.title("Origin")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(232), plt.axis('off'), plt.title("cv.COLORMAP_PINK")
plt.imshow(cv.cvtColor(pseudo1, cv.COLOR_BGR2RGB))
plt.subplot(233), plt.axis('off'), plt.title("cv.COLORMAP_JET")
plt.imshow(cv.cvtColor(pseudo2, cv.COLOR_BGR2RGB))
plt.subplot(234), plt.axis('off'), plt.title("cv.COLORMAP_WINTER")
plt.imshow(cv.cvtColor(pseudo3, cv.COLOR_BGR2RGB))
plt.subplot(235), plt.axis('off'), plt.title("cv.COLORMAP_RAINBOW")
plt.imshow(cv.cvtColor(pseudo4, cv.COLOR_BGR2RGB))
plt.subplot(236), plt.axis('off'), plt.title("cv.COLORMAP_HOT")
plt.imshow(cv.cvtColor(pseudo5, cv.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
