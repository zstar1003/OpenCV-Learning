"""
添加文字-中文
"""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


imgBGR = cv2.imread("../img/img.jpg")
if (isinstance(imgBGR, np.ndarray)):  # 判断是否 OpenCV 图片类型
    imgPIL = Image.fromarray(cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB))
text = "zstar, 中文字体"
pos = (100, 20)  # (left, top)，字符串左上角坐标
color = (0, 0, 0)  # 字体颜色
textSize = 40
drawPIL = ImageDraw.Draw(imgPIL)
fontText = ImageFont.truetype("Font/simhei.ttf", textSize, encoding="utf-8")
drawPIL.text(pos, text, color, font=fontText)
imgPutText = cv2.cvtColor(np.asarray(imgPIL), cv2.COLOR_RGB2BGR)

cv2.imshow("imgPutText", imgPutText)  # 显示叠加图像 imgAdd
key = cv2.waitKey(0)  # 等待按键命令
