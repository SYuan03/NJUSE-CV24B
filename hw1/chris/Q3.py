import numpy as np
import cv2

# 这两个都是ndarray
# 读取灰度图像i1
img_i1_gray = cv2.imread('./imgs/I1.jpg', cv2.IMREAD_GRAYSCALE)
# 读取二值图像i2
img_i2_binary = cv2.imread('./imgs/I2.png', cv2.IMREAD_GRAYSCALE)

assert img_i1_gray.shape == img_i2_binary.shape

# 以ndarray打印i2的数值
# print(img_i2_binary)

# 一个字节为8位，所以灰度图像一个像素点的值为0-255，二值的话就是0或255
for i in range(8):
    # i << 4 = 二进制10000，即16
    # 取出img_i2_binary每个数值的Li位，从低到高L1 - L8
    # i = 0对应L1，i = 1对应L2，以此类推
    bit_i2 = img_i2_binary & (1 << i)
    # 用该值替换掉img_i2_gray的Li位
    img_i1_gray_new = img_i1_gray | bit_i2

    # 保存新的灰度图像
    cv2.imwrite(f'./imgs/I1_bit_replace/I1_gray_L{i+1}.jpg', img_i1_gray_new)
