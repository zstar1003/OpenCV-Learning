"""
Title:赛博朋克特效实现
Author:迷途小书童的Note
Link:https://mp.weixin.qq.com/s/brZSanGvqqi6AHT3wg54Lg
"""

import cv2
import numpy as np

def modify_color_temperature(img):
    # ---------------- 冷色調 ---------------- #
    # 1.计算三个通道的平均值，并依据平均值调整色调
    imgB = img[:, :, 0]
    imgG = img[:, :, 1]
    imgR = img[:, :, 2]

    # 调整色调 # 白平衡 -> 三个值变化相同
    # 冷色调(增加b分量) -> 除了b之外都增加
    # 暖色调(增加r分量) -> 除了r之外都增加
    bAve = cv2.mean(imgB)[0]
    gAve = cv2.mean(imgG)[0] + 10
    rAve = cv2.mean(imgR)[0] + 10
    aveGray = (int)(bAve + gAve + rAve) / 3

    # 2. 计算各通道增益系数，并使用此系数计算結果
    bCoef = aveGray / bAve
    gCoef = aveGray / gAve
    rCoef = aveGray / rAve
    imgB = np.floor((imgB * bCoef))  # 向下取整
    imgG = np.floor((imgG * gCoef))
    imgR = np.floor((imgR * rCoef))

    # 3. 变换后处理
    imgb = imgB
    imgb[imgb > 255] = 255

    imgg = imgG
    imgg[imgg > 255] = 255

    imgr = imgR
    imgr[imgr > 255] = 255
    cold_rgb = np.dstack((imgb, imgg, imgr)).astype(np.uint8)
    return cold_rgb


def reverse_hue(image):
    # 反转色相
    image_hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    image_hls = np.asarray(image_hls, np.float32)

    hue = image_hls[:, :, 0]
    hue[hue < 90] = 180 - hue[hue < 90] - 10
    image_hls[:, :, 0] = hue

    image_hls = np.asarray(image_hls, np.uint8)
    image = cv2.cvtColor(image_hls, cv2.COLOR_HLS2BGR)
    return image

def cyberpunk(image):
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    image_lab = np.asarray(image_lab, np.float32)
    image_lab[:,:,0] = np.clip(image_lab[:,:,0] * 1.2,0,255)


    # 提高像素亮度，让亮的地方更亮
    light_gamma_high = np.power(image_lab[:, :, 0], 0.9)
    light_gamma_high = np.asarray(light_gamma_high / np.max(light_gamma_high) * 255, np.uint)

     # 降低像素亮度，让暗的地方更暗
    light_gamma_low = np.power(image_lab[:, :, 0], 1.1)
    light_gamma_low = np.asarray(light_gamma_low / np.max(light_gamma_low) * 255, np.uint8)

    # 调色至偏紫
    dark_b = image_lab[:, :, 2] * (light_gamma_low / 255) * 0.4
    dark_a = image_lab[:, :, 2] * (1 - light_gamma_high / 255) * 0.1

    image_lab[:, :, 2] = np.clip(image_lab[:, :, 2] - dark_b, 0, 255)
    image_lab[:, :, 1] = np.clip(image_lab[:, :, 1] - dark_a, 0, 255)

    image_lab = np.asarray(image_lab, np.uint8)
    return cv2.cvtColor(image_lab, cv2.COLOR_Lab2BGR)


if __name__ == "__main__":
    # 设置窗口可缩放
    cv2.namedWindow('origin', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow('cold_style', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow('reverser_hue', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow('cyberpunk', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    image = cv2.imread("../img/img.jpg")
    cv2.imshow("origin", image)

    image = modify_color_temperature(image)
    cv2.imshow("cold_style", image)
    image = reverse_hue(image)
    cv2.imshow("reverser_hue", image)
    # cv2.waitKey()

    image = cyberpunk(image)
    cv2.imshow("cyberpunk", image)
    cv2.imwrite("result2.jpg", image)
    cv2.waitKey()