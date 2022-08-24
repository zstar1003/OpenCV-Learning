"""
中值滤波
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../img/lena.jpg", flags=0)


imgMedianBlur1 = cv2.medianBlur(img, 3)
imgMedianBlur2 = cv2.medianBlur(img, 7)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title("cv2.medianBlur(size=3)")
plt.imshow(cv2.cvtColor(imgMedianBlur1, cv2.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('off'), plt.title("cv2.medianBlur(size=7)")
plt.imshow(cv2.cvtColor(imgMedianBlur2, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()

