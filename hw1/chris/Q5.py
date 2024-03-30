import os

import cv2
import numpy as np

img = cv2.imread('./imgs/I0.jpg')
os.makedirs('./imgs/Q5', exist_ok=True)

# 1. 调整亮度
# 使用convertScaleAbs
# 亮度增强
img_bright = cv2.convertScaleAbs(img, alpha=1, beta=100)
cv2.imwrite('./imgs/Q5/I0_bright.jpg', img_bright)

# 2. 调整对比度
# 使用convertScaleAbs
# 对比度增强
img_contrast = cv2.convertScaleAbs(img, alpha=2, beta=0)
cv2.imwrite('./imgs/Q5/I0_contrast.jpg', img_contrast)

# 3. 调整饱和度
# 转到HSV空间，调整S通道
# 饱和度增强
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
# 为了给S通道加50，创建一个与S通道同形状的数组，所有值都是50。
s_add = np.full(s.shape, 50, dtype=np.uint8)
# 使用cv2.add来确保加法结果不会超过255的范围
s = cv2.add(s, s_add)
img_saturation = cv2.merge([h, s, v])
img_saturation = cv2.cvtColor(img_saturation, cv2.COLOR_HSV2BGR)
cv2.imwrite('./imgs/Q5/I0_saturation.jpg', img_saturation)

