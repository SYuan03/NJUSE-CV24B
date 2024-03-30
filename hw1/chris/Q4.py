import cv2
import os

# 将附带彩色图像（I0）的R、G、B通道中某个或某几个通道做与Q3类似的处理
# 对R通道做处理

img_I0 = cv2.imread('./imgs/I0.jpg')
img_I2_binary = cv2.imread('./imgs/I2.png', cv2.IMREAD_GRAYSCALE)

# 分割通道
b_channel, g_channel, r_channel = cv2.split(img_I0)

# 遍历R通道的每一位
# 创建文件夹
os.makedirs('./imgs/I0_bit_replace/R', exist_ok=True)
for i in range(8):
    # 获取二值图像的当前位
    bit_i_binary = img_I2_binary & (1 << i)
    # 将R通道的当前位替换为二值图像的当前位
    r_channel_new = r_channel | bit_i_binary
    # 合并
    img_I0_new = cv2.merge([b_channel, g_channel, r_channel_new])
    # 保存
    cv2.imwrite(f'./imgs/I0_bit_replace/R/I0_ChannelR_L{i+1}.jpg', img_I0_new)

# 对G通道做处理
os.makedirs('./imgs/I0_bit_replace/G', exist_ok=True)
for i in range(8):
    bit_i_binary = img_I2_binary & (1 << i)
    g_channel_new = g_channel | bit_i_binary
    img_I0_new = cv2.merge([b_channel, g_channel_new, r_channel])
    cv2.imwrite(f'./imgs/I0_bit_replace/G/I0_ChannelG_L{i+1}.jpg', img_I0_new)

# 对B通道做处理
os.makedirs('./imgs/I0_bit_replace/B', exist_ok=True)
for i in range(8):
    bit_i_binary = img_I2_binary & (1 << i)
    b_channel_new = b_channel | bit_i_binary
    img_I0_new = cv2.merge([b_channel_new, g_channel, r_channel])
    cv2.imwrite(f'./imgs/I0_bit_replace/B/I0_ChannelB_L{i+1}.jpg', img_I0_new)