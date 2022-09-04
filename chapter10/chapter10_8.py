"""
绘制圆形
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = np.ones((400, 600, 3), np.uint8) * 192

center = (0, 0)  # 圆心坐标
cx, cy = 300, 200  # 圆心坐标
for r in range(200, 0, -20):
    color = (r, r, 255 - r)
    cv.circle(img, (cx, cy), r, color, -1)
    cv.circle(img, center, r, 255)
    cv.circle(img, (600, 400), r, color, 5)

plt.figure(figsize=(6, 4))
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
