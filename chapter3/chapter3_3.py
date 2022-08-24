"""
图像旋转(直角旋转)
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)

imgR90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
imgR180 = cv2.rotate(img, cv2.ROTATE_180)
imgR270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title(r"$Origin$")
plt.subplot(222), plt.imshow(cv2.cvtColor(imgR90, cv2.COLOR_BGR2RGB)), plt.title(r"$Rotation 90^{o}$")
plt.subplot(223), plt.imshow(cv2.cvtColor(imgR180, cv2.COLOR_BGR2RGB)), plt.title(r"$Rotation 180^{o}$")
plt.subplot(224), plt.imshow(cv2.cvtColor(imgR270, cv2.COLOR_BGR2RGB)), plt.title(r"$Rotation 270^{o}$")
plt.show()
