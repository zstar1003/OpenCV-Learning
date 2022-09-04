"""
调节色彩
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/img.jpg", flags=1)

maxG = 128  # 修改颜色通道最大值，0<=maxG<=255
lutHalf = np.array([int(i * maxG / 255) for i in range(256)]).astype("uint8")
lutEqual = np.array([i for i in range(256)]).astype("uint8")

lut3HalfB = np.dstack((lutHalf, lutEqual, lutEqual))  # (1,256,3), B_half/BGR
lut3HalfG = np.dstack((lutEqual, lutHalf, lutEqual))  # (1,256,3), G_half/BGR
lut3HalfR = np.dstack((lutEqual, lutEqual, lutHalf))  # (1,256,3), R_half/BGR

blendHalfB = cv.LUT(img, lut3HalfB)  # B 通道衰减 50%
blendHalfG = cv.LUT(img, lut3HalfG)  # G 通道衰减 50%
blendHalfR = cv.LUT(img, lut3HalfR)  # R 通道衰减 50%


plt.figure(figsize=(9, 5))
plt.subplot(131), plt.axis('off'), plt.title("B half decayed")
plt.imshow(cv.cvtColor(blendHalfB, cv.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title("G half decayed")
plt.imshow(cv.cvtColor(blendHalfG, cv.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('off'), plt.title("R half decayed")
plt.imshow(cv.cvtColor(blendHalfR, cv.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
