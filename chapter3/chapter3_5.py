"""
图像缩放
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)

height, width = img.shape[:2]  # 图片的高度和宽度
imgZoom1 = cv2.resize(img, (int(0.75 * width), int(height)))
imgZoom2 = cv2.resize(img, None, fx=0.75, fy=1.0, interpolation=cv2.INTER_AREA)

plt.figure(figsize=(8, 6))
plt.subplot(121), plt.axis('off'), plt.title("Zoom: 0.75*W,1.0*H")
plt.imshow(cv2.cvtColor(imgZoom1, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.axis('off'), plt.title("Zoom: fx=0.75,fy=1.0")
plt.imshow(cv2.cvtColor(imgZoom2, cv2.COLOR_BGR2RGB))
plt.show()
