import os
import random

import numpy as np
import cv2


# 函数：添加高斯噪声
def add_gaussian_noise_on_gray(image, mean=0, var=1000):
    row, col = image.shape
    sigma = var ** 0.5  # 标准差
    # 生成一个与图像尺寸相同的高斯噪声矩阵，正态分布中取值
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_image = image + gauss
    # clip是将数组中的元素限制在a_min, a_max之间，大于a_max的就使得它等于a_max，小于a_min的就使得它等于a_min
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image


# 函数：添加椒盐噪声
def add_salt_and_pepper_noise_on_gray(image, salt_prob, pepper_prob):
    """
    向图像添加椒盐噪声

    参数:
    image: NumPy数组，代表灰度图像
    salt_prob: 添加“盐”噪声的概率
    pepper_prob: 添加“椒”噪声的概率
    """
    noisy_image = np.copy(image)
    num_rows, num_cols = image.shape

    # 添加“盐”噪声
    for i in range(num_rows):
        for j in range(num_cols):
            random_value = random.random()  # 生成一个0到1之间的随机数
            if random_value < salt_prob:
                noisy_image[i, j] = 255  # 将当前像素值设置为255（白色）

    # 添加“椒”噪声
    for i in range(num_rows):
        for j in range(num_cols):
            random_value = random.random()  # 再次生成一个0到1之间的随机数
            if random_value < pepper_prob:
                noisy_image[i, j] = 0  # 将当前像素值设置为0（黑色）

    return noisy_image


# 添加泊松噪声
def add_poisson_noise_on_gray(image):
    """
    向图像添加泊松噪声

    参数:
    image: NumPy数组，代表灰度图像
    """
    vals = 1.0  # 调整因子，具体数值可以根据需要调整
    print("current vals: ", vals)

    # 生成一个与图像尺寸相同的泊松噪声矩阵
    noisy_image = np.random.poisson(image * vals) / float(vals)
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image


if __name__ == '__main__':
    # 读取Q1转换出的灰度图像
    # 注意这里要使用cv2.IMREAD_GRAYSCALE参数读取灰度图像，否则读取的图像是三通道的
    I1 = cv2.imread('./Q1_output/I1.jpg', cv2.IMREAD_GRAYSCALE)

    image_gaussian_noise = add_gaussian_noise_on_gray(I1)
    image_salt_pepper_noise = add_salt_and_pepper_noise_on_gray(I1, 0.1, 0.1)
    image_poisson_noise = add_poisson_noise_on_gray(I1)

    # 保存噪声图像
    os.makedirs("Q2_output", exist_ok=True)
    cv2.imwrite('./Q2_output/I1_gaussian.jpg', image_gaussian_noise)
    cv2.imwrite('./Q2_output/I1_salt_pepper.jpg', image_salt_pepper_noise)
    cv2.imwrite('./Q2_output/I1_poisson.jpg', image_poisson_noise)

    # 加了噪声的图像与原图像的对比
    # 使用diff
    diff_gaussian = cv2.absdiff(I1, image_gaussian_noise)
    diff_salt_pepper = cv2.absdiff(I1, image_salt_pepper_noise)
    diff_poisson = cv2.absdiff(I1, image_poisson_noise)

    # 使用cv2.applyColorMap()函数将灰度图转换为伪彩色图
    diff_gaussian = cv2.applyColorMap(diff_gaussian, cv2.COLORMAP_JET)
    diff_salt_pepper = cv2.applyColorMap(diff_salt_pepper, cv2.COLORMAP_JET)
    diff_poisson = cv2.applyColorMap(diff_poisson, cv2.COLORMAP_JET)

    cv2.imwrite('./Q2_output/I1_gaussian_diff.jpg', diff_gaussian)
    cv2.imwrite('./Q2_output/I1_salt_pepper_diff.jpg', diff_salt_pepper)
    cv2.imwrite('./Q2_output/I1_poisson_diff.jpg', diff_poisson)