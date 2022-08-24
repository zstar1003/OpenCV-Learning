"""
图像边界扩充
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/xdu.jpg")  # 读取彩色图像(BGR)

top = bottom = left = right = 50
imgReplicate = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
imgReflect = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)
imgReflect101 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT_101)
imgWrap = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_WRAP)
imgConstant = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(200, 200, 200))

plt.figure(figsize=(9, 6))
plt.subplot(231), plt.axis([-50, 562, -50, 562]), plt.title('ORIGINAL'), plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(232), plt.axis('off'), plt.title('REPLICATE')
plt.imshow(cv2.cvtColor(imgReplicate, cv2.COLOR_BGR2RGB))
plt.subplot(233), plt.axis('off'), plt.title('REFLECT')
plt.imshow(cv2.cvtColor(imgReflect, cv2.COLOR_BGR2RGB))
plt.subplot(234), plt.axis('off'), plt.title('REFLECT_101')
plt.imshow(cv2.cvtColor(imgReflect101, cv2.COLOR_BGR2RGB))
plt.subplot(235), plt.axis('off'), plt.title('WRAP')
plt.imshow(cv2.cvtColor(imgWrap, cv2.COLOR_BGR2RGB))
plt.subplot(236), plt.axis('off'), plt.title('CONSTANT')
plt.imshow(cv2.cvtColor(imgConstant, cv2.COLOR_BGR2RGB))
plt.show()
