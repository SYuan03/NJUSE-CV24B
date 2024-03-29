import cv2

# 以灰度读取彩色cv_yyds图像，做了下转换
img_origin = cv2.imread('./imgs/cv_yyds_origin.jpg', cv2.IMREAD_GRAYSCALE)

# 灰度图像读取
img_target = cv2.imread('./imgs/I1.jpg', cv2.IMREAD_GRAYSCALE)

# 将原始图像调整为与目标图像相同的分辨率
img_resized = cv2.resize(img_origin, (img_target.shape[1], img_target.shape[0]))

# 将调整大小后的图像转换为二值图像
# 127为阈值，大于127的像素值设为255，小于127的像素值设为0
_, img_binary = cv2.threshold(img_resized, 127, 255, cv2.THRESH_BINARY)

# 保存二值图像
cv2.imwrite('./imgs/I2.png', img_binary)
