"""
读取、保存、显示图像
"""
import cv2
import numpy as np
import urllib.request as request

# 读取本地图像
imgFile = "../img/img.jpg"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv2.imread(imgFile, flags=0)  # flags=0 读取为灰度图像
# 读取网络图像
response = request.urlopen("https://img-blog.csdnimg.cn/8992e07a6539448b94b06936c21b4a67.jpeg")
imgUrl = cv2.imdecode(np.array(bytearray(response.read()), dtype=np.uint8), -1)
# 显示图像
cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img1", 600, 600)
cv2.imshow("img1", img1)  # img1为窗口标题
cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img2", 600, 600)
cv2.imshow("img2", img2)
cv2.imshow("img3", imgUrl)
key = cv2.waitKey(0)  # 等待按键命令, 1000ms 后自动关闭
# 保存图像
saveFile = "img/imgSave.png"  # 保存文件的路径
cv2.imwrite(saveFile, img2)  # 保存图像文件
# cv2.imwrite(saveFile, img3, [int(cv2.IMWRITE_PNG_COMPRESSION), 8])  # 保存图像文件, 设置压缩比为 8

