import cv2

img = cv2.imread('./imgs/I0.jpg')
# 转换为灰度图像
# 将R G B三个通道的像素值取加权平均值，得到一个灰度值
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 保存图像
cv2.imwrite('./imgs/I1.jpg', img_gray)
