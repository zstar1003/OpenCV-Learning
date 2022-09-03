"""
边缘检测(Roberts算子, Prewitt算子, Sobel算子, Laplacian算子)
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)

# 自定义卷积核
# Roberts 边缘算子
kernel_Roberts_x = np.array([[1, 0], [0, -1]])
kernel_Roberts_y = np.array([[0, -1], [1, 0]])
# Prewitt 边缘算子
kernel_Prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_Prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
# Sobel 边缘算子
kernel_Sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_Sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
# Laplacian 边缘算子
kernel_Laplacian_K1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
kernel_Laplacian_K2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# 卷积运算
imgBlur = cv2.blur(img, (3, 3))  # Blur 平滑后再做 Laplacian 变换
imgLaplacian_K1 = cv2.filter2D(imgBlur, -1, kernel_Laplacian_K1)
imgLaplacian_K2 = cv2.filter2D(imgBlur, -1, kernel_Laplacian_K2)
imgRoberts_x = cv2.filter2D(img, -1, kernel_Roberts_x)
imgRoberts_y = cv2.filter2D(img, -1, kernel_Roberts_y)
imgRoberts = np.uint8(cv2.normalize(abs(imgRoberts_x) + abs(imgRoberts_y), None, 0, 255, cv2.NORM_MINMAX))
imgPrewitt_x = cv2.filter2D(img, -1, kernel_Prewitt_x)
imgPrewitt_y = cv2.filter2D(img, -1, kernel_Prewitt_y)
imgPrewitt = np.uint8(cv2.normalize(abs(imgPrewitt_x) + abs(imgPrewitt_y), None, 0, 255, cv2.NORM_MINMAX))
imgSobel_x = cv2.filter2D(img, -1, kernel_Sobel_x)
imgSobel_y = cv2.filter2D(img, -1, kernel_Sobel_y)
imgSobel = np.uint8(cv2.normalize(abs(imgSobel_x) + abs(imgSobel_y), None, 0, 255, cv2.NORM_MINMAX))

plt.figure(figsize=(12, 8))
plt.subplot(341), plt.title('Origin'), plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(345), plt.title('Laplacian_K1'), plt.imshow(imgLaplacian_K1, cmap='gray'), plt.axis('off')
plt.subplot(349), plt.title('Laplacian_K2'), plt.imshow(imgLaplacian_K2, cmap='gray'), plt.axis('off')
plt.subplot(342), plt.title('Roberts'), plt.imshow(imgRoberts, cmap='gray'), plt.axis('off')
plt.subplot(346), plt.title('Roberts_X'), plt.imshow(imgRoberts_x, cmap='gray'), plt.axis('off')
plt.subplot(3, 4, 10), plt.title('Roberts_Y'), plt.imshow(imgRoberts_y, cmap='gray'), plt.axis('off')
plt.subplot(343), plt.title('Prewitt'), plt.imshow(imgPrewitt, cmap='gray'), plt.axis('off')
plt.subplot(347), plt.title('Prewitt_X'), plt.imshow(imgPrewitt_x, cmap='gray'), plt.axis('off')
plt.subplot(3, 4, 11), plt.title('Prewitt_Y'), plt.imshow(imgPrewitt_y, cmap='gray'), plt.axis('off')
plt.subplot(344), plt.title('Sobel'), plt.imshow(imgSobel, cmap='gray'), plt.axis('off')
plt.subplot(348), plt.title('Sobel_X'), plt.imshow(imgSobel_x, cmap='gray'), plt.axis('off')
plt.subplot(3, 4, 12), plt.title('Sobel_Y'), plt.imshow(imgSobel_y, cmap='gray'), plt.axis('off')
plt.tight_layout()
plt.show()
