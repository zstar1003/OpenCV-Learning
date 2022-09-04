"""
调节饱和度和明度
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/img.jpg", flags=1)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # 色彩空间转换, BGR->HSV

# 调节通道强度
lutWeaken = np.array([int(0.6 * i) for i in range(256)]).astype("uint8")
lutEqual = np.array([i for i in range(256)]).astype("uint8")
lutRaisen = np.array([int(102 + 0.6 * i) for i in range(256)]).astype("uint8")
# 调节饱和度
lutSWeaken = np.dstack((lutEqual, lutWeaken, lutEqual))  # Saturation weaken
lutSRaisen = np.dstack((lutEqual, lutRaisen, lutEqual))  # Saturation raisen
# 调节明度
lutVWeaken = np.dstack((lutEqual, lutEqual, lutWeaken))  # Value weaken
lutVRaisen = np.dstack((lutEqual, lutEqual, lutRaisen))  # Value raisen

blendSWeaken = cv.LUT(hsv, lutSWeaken)  # 饱和度降低
blendSRaisen = cv.LUT(hsv, lutSRaisen)  # 饱和度增大
blendVWeaken = cv.LUT(hsv, lutVWeaken)  # 明度降低
blendVRaisen = cv.LUT(hsv, lutVRaisen)  # 明度升高

plt.figure(figsize=(9, 6))
plt.subplot(231), plt.axis('off'), plt.title("Saturation weaken")
plt.imshow(cv.cvtColor(blendSWeaken, cv.COLOR_HSV2RGB))
plt.subplot(232), plt.axis('off'), plt.title("Normal saturation")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(233), plt.axis('off'), plt.title("Saturation raisen")
plt.imshow(cv.cvtColor(blendSRaisen, cv.COLOR_HSV2RGB))
plt.subplot(234), plt.axis('off'), plt.title("Value weaken")
plt.imshow(cv.cvtColor(blendVWeaken, cv.COLOR_HSV2RGB))
plt.subplot(235), plt.axis('off'), plt.title("Normal value")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(236), plt.axis('off'), plt.title("Value raisen")
plt.imshow(cv.cvtColor(blendVRaisen, cv.COLOR_HSV2RGB))
plt.tight_layout()
plt.show()
