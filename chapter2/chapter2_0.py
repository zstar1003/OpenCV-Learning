"""
图像的加法运算
"""
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)
img2 = cv2.imread("../img/img.jpg")  # 读取彩色图像(BGR)

imgAddCV = cv2.add(img1, img2)  # OpenCV 加法: 饱和运算
imgAddNP = img1 + img2  # Numpy 加法: 模运算

plt.subplot(221), plt.title("1. img1"), plt.axis('off')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # 显示 img1(RGB)
plt.subplot(222), plt.title("2. img2"), plt.axis('off')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 显示 img2(RGB)
plt.subplot(223), plt.title("3. cv2.add(img1, img2)"), plt.axis('off')
plt.imshow(cv2.cvtColor(imgAddCV, cv2.COLOR_BGR2RGB))  # 显示 imgAddCV(RGB)
plt.subplot(224), plt.title("4. img1 + img2"), plt.axis('off')
plt.imshow(cv2.cvtColor(imgAddNP, cv2.COLOR_BGR2RGB))  # 显示 imgAddNP(RGB)
plt.savefig("result3.png")
plt.show()
