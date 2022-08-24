"""
添加文字
"""
import cv2

img1 = cv2.imread("../img/img.jpg")

text = "zstar"
fontList = [cv2.FONT_HERSHEY_SIMPLEX,
            cv2.FONT_HERSHEY_SIMPLEX,
            cv2.FONT_HERSHEY_PLAIN,
            cv2.FONT_HERSHEY_DUPLEX,
            cv2.FONT_HERSHEY_COMPLEX,
            cv2.FONT_HERSHEY_TRIPLEX,
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            cv2.FONT_ITALIC]
fontScale = 1  # 字体缩放比例
color = (0, 0, 0)  # 字体颜色
for i in range(10):
    pos = (10, 50 * (i + 1))
    imgPutText = cv2.putText(img1, text, pos, fontList[i], fontScale, color)

cv2.imshow("imgPutText", imgPutText)  # 显示叠加图像 imgAdd
key = cv2.waitKey(0)  # 等待按键命令
