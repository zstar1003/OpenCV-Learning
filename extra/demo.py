"""
Title:旧影浮光——基于Opencv的色彩保留滤镜
Author:ZouKeh
Link:https://www.bilibili.com/video/BV1BG4y1r7WP
"""

import numpy as np
import cv2


def color_choose():
    # 选择需要保留的颜色
    color = int(input("choose color(1.red 2.yellow 3.blue 4.green 5.white):"))
    lower = np.array([0, 0, 0])
    upper = np.array([0, 0, 0])
    if color == 1:
        lower = np.array([156, 60, 60])
        upper = np.array([180, 255, 255])
        # lower = np.array([0, 60, 60])
        # upper = np.array([10, 255, 255])
    elif color == 2:
        lower = np.array([26, 43, 46])
        upper = np.array([34, 255, 255])
    elif color == 3:
        lower = np.array([100, 43, 46])
        upper = np.array([124, 255, 255])
    elif color == 4:
        lower = np.array([35, 43, 46])
        upper = np.array([77, 255, 255])
    elif color == 5:
        lower = np.array([0, 0, 221])
        upper = np.array([180, 30, 255])
    return lower, upper, color


def choose_range(img):
    # 在图片上画区域 选择需要保留颜色的区域
    a = []
    b = []

    ##鼠标事件 左键单击
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        global num  # 界面上点的个数 0开始 偶数为起点 奇数为终点
        # global begin_xy
        if event == cv2.EVENT_LBUTTONDOWN and num % 2 == 0:  # 画选框的左上角 红色
            xy = "%d,%d" % (x, y)
            a.append(x)
            b.append(y)
            cv2.circle(img, (x, y), 2, (0, 0, 255), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
            print(x, y)
            num += 1
            begin_xy = (x, y)
        elif event == cv2.EVENT_LBUTTONDOWN and num % 2 == 1:  # 画选框的右下角 绿色
            xy = "%d,%d" % (x, y)
            a.append(x)
            b.append(y)
            cv2.circle(img, (x, y), 2, (0, 255, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            # cv2.arrowedLine(img, begin_xy, (x, y), (0, 0, 255), 2, 0, 0, 0.1)  # 画完终点后画箭头
            cv2.imshow("image", img)
            print(x, y)
            num += 1

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

    while True:
        cv2.imshow('image', img)
        key = cv2.waitKey(1)
        if key == ord('q'):  # 在键盘上按Q键退出画图
            break
    if num % 2 == 1:  # 如果num为奇数说明有一个起点多余了 去掉
        a = a[:-1]
        b = b[:-1]
    print(a, b)
    return a, b


# 将坐标点列表a,b 转换为corner_list(坐标点必须为(x,y)形式)
def get_corner_list(a, b):
    corner_list = []
    for i in range(int(len(a) / 2)):
        corner_list.append([a[2 * i], b[2 * i], a[2 * i + 1], b[2 * i + 1]])
    # print(corner_list)
    return corner_list


# 将在选区外的掩膜去除
# 判断点是否在选择区域内
def in_box(i, j, corner_list):
    # if_inbox = False
    for k in corner_list:
        if i >= k[0] and i <= k[2] and j >= k[1] and j <= k[3]:
            return True
        else:
            continue
    return False


def cut(mask_r, corner_list):
    for i in range(mask_r.shape[0]):
        for j in range(mask_r.shape[1]):
            if mask_r[i, j] == 255 and not in_box(j, i, corner_list):
                mask_r[i, j] = 0
            else:
                continue
    return mask_r


# 主函数
def main(corner_list, img_path, lower, upper, color):
    # 转为hsv颜色模式
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    if color == 1:
        lower_red2 = np.array([0, 60, 60])
        upper_red2 = np.array([10, 255, 255])  # thers is two ranges of red
        mask_2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask + mask_2
    mask = cut(mask, corner_list)
    gray_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    gray = cv2.merge([gray_image, gray_image, gray_image])
    # 将mask于原视频帧进行按位与操作，则会把mask中的白色用真实的图像替换：
    res = cv2.bitwise_and(img, img, mask=mask)
    mask_bg = cv2.bitwise_not(mask)
    gray = cv2.bitwise_and(gray, gray, mask=mask_bg)
    result = res + gray
    cv2.namedWindow('Result', 0)
    cv2.imshow('Result', result)
    cv2.imwrite('result.jpg', result)
    cv2.waitKey(0)


if __name__ == '__main__':
    img_path = '../img/img.jpg'
    lower, upper, color = color_choose()
    img = cv2.imread(img_path)
    num = 0
    a, b = choose_range(img)
    cv2.destroyAllWindows()
    corner_list = get_corner_list(a, b)
    main(corner_list, img_path, lower, upper, color)
