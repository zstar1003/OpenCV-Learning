"""
图像分割之k均值聚类
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/img.jpg", flags=1)

dataPixel = np.float32(img.reshape((-1, 3)))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)  # 终止条件
flags = cv2.KMEANS_RANDOM_CENTERS  # 起始的中心选择

K = 2  # 设置聚类数
_, labels, center = cv2.kmeans(dataPixel, K, None, criteria, 10, flags)
centerUint = np.uint8(center)
classify = centerUint[labels.flatten()]  # 将像素标记为聚类中心颜色
imgKmean3 = classify.reshape((img.shape))  # 恢复为二维图像

K = 3  # 设置聚类数
_, labels, center = cv2.kmeans(dataPixel, K, None, criteria, 10, flags)
centerUint = np.uint8(center)
classify = centerUint[labels.flatten()]  # 将像素标记为聚类中心颜色
imgKmean4 = classify.reshape((img.shape))  # 恢复为二维图像

K = 5  # 设置聚类数
_, labels, center = cv2.kmeans(dataPixel, K, None, criteria, 10, flags)
centerUint = np.uint8(center)
classify = centerUint[labels.flatten()]  # 将像素标记为聚类中心颜色
imgKmean5 = classify.reshape((img.shape))  # 恢复为二维图像

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.axis('off'), plt.title("Origin")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 显示 img1(RGB)
plt.subplot(222), plt.axis('off'), plt.title("K-mean (k=2)")
plt.imshow(cv2.cvtColor(imgKmean3, cv2.COLOR_BGR2RGB))
plt.subplot(223), plt.axis('off'), plt.title("K-mean (k=3)")
plt.imshow(cv2.cvtColor(imgKmean4, cv2.COLOR_BGR2RGB))
plt.subplot(224), plt.axis('off'), plt.title("K-mean (k=5)")
plt.imshow(cv2.cvtColor(imgKmean5, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()