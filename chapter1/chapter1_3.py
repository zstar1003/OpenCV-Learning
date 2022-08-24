"""
裁剪图像
"""
import cv2

img1 = cv2.imread("../img/img.jpg")  # flags=1 读取彩色图像(BGR)

# 方式一：自定义切片位置参数
# xmin, ymin, w, h = 180, 190, 200, 200  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w)
# imgROI = img1[ymin:ymin + h, xmin:xmin + w].copy()  # 切片获得裁剪后保留的图像区域
# 方式二：鼠标框选获得位置参数
roi = cv2.selectROI(img1, showCrosshair=True, fromCenter=False)
xmin, ymin, w, h = roi  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w) 的位置参数
imgROI = img1[ymin:ymin + h, xmin:xmin + w].copy()  # 切片获得裁剪后保留的图像区域

cv2.imshow("DemoRIO", imgROI)
cv2.waitKey(0)
