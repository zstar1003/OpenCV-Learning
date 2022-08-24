"""
拼接图像
"""
import cv2
import numpy as np

img1 = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
img2 = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (300, 400))
img3 = cv2.resize(img2, (400, 300))
imgStackH = np.hstack((img1, img2))  # 高度相同图像可以横向水平拼接
imgStackV = np.vstack((img1, img3))  # 宽度相同图像可以纵向垂直拼接


cv2.imshow("DemoStackH", imgStackH)  # 在窗口显示图像 imgStackH
cv2.imshow("DemoStackV", imgStackV)  # 在窗口显示图像 imgStackV
key = cv2.waitKey(0)  # 等待按键命令
