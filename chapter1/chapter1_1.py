"""
用 matplotlib 显示图像
"""
import cv2
import matplotlib.pyplot as plt

imgFile = "../img/img.jpg"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)

imgRGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # 图片格式转换：BGR(OpenCV) -> RGB(PyQt5)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 图片格式转换：BGR(OpenCV) -> Gray

plt.rcParams['font.sans-serif'] = ['FangSong']  # 支持中文标签
plt.subplot(221), plt.title("1. RGB 格式(mpl)"), plt.axis('off')
plt.imshow(imgRGB)  # matplotlib 显示彩色图像(RGB格式)
plt.subplot(222), plt.title("2. BGR 格式(OpenCV)"), plt.axis('off')
plt.imshow(img1)  # matplotlib 显示彩色图像(BGR格式)
plt.subplot(223), plt.title("3. 设置 Gray 参数"), plt.axis('off')
plt.imshow(img2, cmap='gray')  # matplotlib 显示灰度图像，设置 Gray 参数
plt.subplot(224), plt.title("4. 未设置 Gray 参数"), plt.axis('off')
plt.imshow(img2)  # matplotlib 显示灰度图像，未设置 Gray 参数
plt.savefig("result.png")
plt.show()

