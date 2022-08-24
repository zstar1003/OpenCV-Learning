"""
图像的叠加
"""
import cv2
import numpy as np

imgL = cv2.imread("../img/img.jpg")  # 读取大图
imgS = cv2.imread("../img/img.jpg")  # 读取小图 (LOGO)
imgS = cv2.resize(imgS, (300, 300))

x, y = 300, 50  # 叠放位置
W1, H1 = imgL.shape[1::-1]  # 大图尺寸
W2, H2 = imgS.shape[1::-1]  # 小图尺寸
if (x + W2) > W1: x = W1 - W2  # 调整图像叠放位置，避免溢出
if (y + H2) > H1: y = H1 - H2

imgCrop = imgL[y:y + H2, x:x + W2]  # 裁剪大图，与小图 imgS 的大小相同
alpha, beta, gamma = 0.2, 0.8, 0.0  # 加法权值
imgAddW = cv2.addWeighted(imgCrop, alpha, imgS, beta, gamma)  # 加权加法，裁剪图与小图叠加
imgAddM = np.array(imgL)
imgAddM[y:y + H2, x:x + W2] = imgAddW  # 用叠加小图替换原图 imgL 的叠放位置

cv2.imshow("imgAddM", imgAddM)
cv2.waitKey(0)
