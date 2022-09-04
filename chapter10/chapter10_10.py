"""
绘制多段线和多边形
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = np.ones((980, 400, 3), np.uint8) * 224
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()

# 多边形顶点
points1 = np.array([[200, 100], [295, 169], [259, 281], [141, 281], [105, 169]], np.int)
points2 = np.array([[200, 400], [259, 581], [105, 469], [295, 469], [141, 581]])  # (5,2)
points3 = np.array([[200, 700], [222, 769], [295, 769], [236, 812], [259, 881],
                    [200, 838], [141, 881], [164, 812], [105, 769], [178, 769]])

# 绘制多边形，闭合曲线
pts1 = [points1]  # pts1 是列表，列表元素是形状为 (m,2) 的 numpy 二维数组
cv.polylines(img1, pts1, True, (0, 0, 255))  # pts1  是列表
cv.polylines(img1, [points2, points3], 1, 255, 2)  # 可以绘制多个多边形

# 绘制多段线，曲线不闭合
cv.polylines(img2, [points1], False, (0, 0, 255))
cv.polylines(img2, [points2, points3], 0, 255, 2)  # 可以绘制多个多段线

# 绘制填充多边形，注意交叉重叠部分处理
cv.fillPoly(img3, [points1], (0, 0, 255))
cv.fillPoly(img3, [points2, points3], 255)  # 可以绘制多个填充多边形

# 绘制一个填充多边形，注意交叉重叠部分
cv.fillConvexPoly(img4, points1, (0, 0, 255))
cv.fillConvexPoly(img4, points2, 255)  # 不能绘制存在自相交的多边形
cv.fillConvexPoly(img4, points3, 255)  # 可以绘制凹多边形，但要慎用

plt.figure(figsize=(9, 6))
plt.subplot(141), plt.title("closed polygon"), plt.axis('off')
plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
plt.subplot(142), plt.title("unclosed polygo"), plt.axis('off')
plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
plt.subplot(143), plt.title("fillPoly"), plt.axis('off')
plt.imshow(cv.cvtColor(img3, cv.COLOR_BGR2RGB))
plt.subplot(144), plt.title("fillConvexPoly"), plt.axis('off')
plt.imshow(cv.cvtColor(img4, cv.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
