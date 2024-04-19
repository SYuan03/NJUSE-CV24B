import os
import cv2
import numpy as np


# 均值滤波
def mean_filter(image, kernel_size=3):
    return cv2.blur(image, (kernel_size, kernel_size))


# 中值滤波
def median_filter(image, kernel_size=3):
    return cv2.medianBlur(image, kernel_size)


# 高斯滤波
def gaussian_filter(image, kernel_size=3, sigma=1):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)


# 双边滤波
def bilateral_filter(image, kernel_size=3, sigma=1):
    return cv2.bilateralFilter(image, kernel_size, sigma, sigma)


# 非局部均值滤波
def non_local_means_filter(image, h=10, templateWindowSize=7, searchWindowSize=21):
    return cv2.fastNlMeansDenoising(image, None, h, templateWindowSize, searchWindowSize)


# 波士顿变换
def anscombe_transform(x):
    # 波士顿变换
    return 2.0 * np.sqrt(x + 3.0 / 8.0)


def inverse_anscombe_transform(x):
    # 逆波士顿变换
    return (x / 2.0) ** 2 - 3.0 / 8.0


def anscombe_gaussian_filter(image, sigma=1):
    # 应用波士顿变换
    img_transformed = anscombe_transform(image)

    # 应用高斯滤波器
    img_filtered = gaussian_filter(img_transformed, sigma=sigma)

    # 应用逆波士顿变换
    img_restored = inverse_anscombe_transform(img_filtered)

    return img_restored


# 应用滤波器
def process_gaussian_noise():
    # 1. 对高斯噪声图像应用三种滤波器
    I1 = cv2.imread('./Q1_output/I1.jpg', cv2.IMREAD_GRAYSCALE)
    image_gaussian_noise = cv2.imread('./Q2_output/I1_gaussian.jpg', cv2.IMREAD_GRAYSCALE)
    image_gaussian_mean = mean_filter(image_gaussian_noise)
    image_gaussian_median = median_filter(image_gaussian_noise)
    image_gaussian_gaussian = gaussian_filter(image_gaussian_noise, 7, 1)
    image_gaussian_bilateral = bilateral_filter(image_gaussian_noise)
    image_gaussian_non_local_means = non_local_means_filter(image_gaussian_noise)

    print("Processing gaussian noise")
    print("PSNR of mean filter: ", cv2.PSNR(I1, image_gaussian_mean))
    print("PSNR of median filter: ", cv2.PSNR(I1, image_gaussian_median))
    print("PSNR of Gaussian filter: ", cv2.PSNR(I1, image_gaussian_gaussian))
    print("PSNR of bilateral filter: ", cv2.PSNR(I1, image_gaussian_bilateral))
    print("PSNR of non local means filter: ", cv2.PSNR(I1, image_gaussian_non_local_means))
    # 保存滤波结果
    os.makedirs("Q3_output/gaussian", exist_ok=True)
    cv2.imwrite('Q3_output/gaussian/I1_gaussian_mean.jpg', image_gaussian_mean)
    cv2.imwrite('Q3_output/gaussian/I1_gaussian_median.jpg', image_gaussian_median)
    cv2.imwrite('Q3_output/gaussian/I1_gaussian_gaussian.jpg', image_gaussian_gaussian)
    cv2.imwrite('Q3_output/gaussian/I1_gaussian_bilateral.jpg', image_gaussian_bilateral)
    cv2.imwrite('Q3_output/gaussian/I1_gaussian_non_local_means.jpg', image_gaussian_non_local_means)


def process_poission_noise():
    I1 = cv2.imread('./Q1_output/I1.jpg', cv2.IMREAD_GRAYSCALE)
    image_poisson_noise = cv2.imread('./Q2_output/I1_poisson.jpg', cv2.IMREAD_GRAYSCALE)
    image_poisson_mean = mean_filter(image_poisson_noise)
    image_poisson_median = median_filter(image_poisson_noise)
    image_poisson_gaussian = gaussian_filter(image_poisson_noise)
    image_poisson_bilateral = bilateral_filter(image_poisson_noise)
    image_poisson_non_local_means = non_local_means_filter(image_poisson_noise)
    # 波士顿变换
    image_poisson_gaussian_anscombe = anscombe_gaussian_filter(image_poisson_noise).astype(np.uint8)

    print("Processing poisson noise")
    print("PSNR of mean filter: ", cv2.PSNR(I1, image_poisson_mean))
    print("PSNR of median filter: ", cv2.PSNR(I1, image_poisson_median))
    print("PSNR of Gaussian filter: ", cv2.PSNR(I1, image_poisson_gaussian))
    print("PSNR of bilateral filter: ", cv2.PSNR(I1, image_poisson_bilateral))
    print("PSNR of non local means filter: ", cv2.PSNR(I1, image_poisson_non_local_means))
    print("PSNR of anscombe gaussian filter: ", cv2.PSNR(I1, image_poisson_gaussian_anscombe))

    # 保存滤波结果
    os.makedirs("Q3_output/poisson", exist_ok=True)
    cv2.imwrite('Q3_output/poisson/I1_poisson_mean.jpg', image_poisson_mean)
    cv2.imwrite('Q3_output/poisson/I1_poisson_median.jpg', image_poisson_median)
    cv2.imwrite('Q3_output/poisson/I1_poisson_gaussian.jpg', image_poisson_gaussian)
    cv2.imwrite('Q3_output/poisson/I1_poisson_bilateral.jpg', image_poisson_bilateral)
    cv2.imwrite('Q3_output/poisson/I1_poisson_non_local_means.jpg', image_poisson_non_local_means)
    cv2.imwrite('Q3_output/poisson/I1_poisson_gaussian_anscombe.jpg', image_poisson_gaussian_anscombe)


def process_salt_pepper_noise():
    I1 = cv2.imread('./Q1_output/I1.jpg', cv2.IMREAD_GRAYSCALE)
    image_salt_pepper_noise = cv2.imread('./Q2_output/I1_salt_pepper.jpg', cv2.IMREAD_GRAYSCALE)
    image_salt_pepper_mean = mean_filter(image_salt_pepper_noise)
    image_salt_pepper_median = median_filter(image_salt_pepper_noise)
    image_salt_pepper_gaussian = gaussian_filter(image_salt_pepper_noise)
    image_salt_pepper_bilateral = bilateral_filter(image_salt_pepper_noise)
    image_salt_pepper_non_local_means = non_local_means_filter(image_salt_pepper_noise)
    # 6.尝试先中值再双边
    image_salt_pepper_median_bilateral = bilateral_filter(median_filter(image_salt_pepper_noise))

    print("Processing salt pepper noise")
    print("PSNR of mean filter: ", cv2.PSNR(I1, image_salt_pepper_mean))
    print("PSNR of median filter: ", cv2.PSNR(I1, image_salt_pepper_median))
    print("PSNR of Gaussian filter: ", cv2.PSNR(I1, image_salt_pepper_gaussian))
    print("PSNR of bilateral filter: ", cv2.PSNR(I1, image_salt_pepper_bilateral))
    print("PSNR of non local means filter: ", cv2.PSNR(I1, image_salt_pepper_non_local_means))
    print("PSNR of median and bilateral filter: ", cv2.PSNR(I1, image_salt_pepper_median_bilateral))

    # 保存滤波结果
    os.makedirs("Q3_output/salt_pepper", exist_ok=True)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_mean.jpg', image_salt_pepper_mean)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_median.jpg', image_salt_pepper_median)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_gaussian.jpg', image_salt_pepper_gaussian)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_bilateral.jpg', image_salt_pepper_bilateral)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_non_local_means.jpg', image_salt_pepper_non_local_means)
    cv2.imwrite('Q3_output/salt_pepper/I1_salt_pepper_median_bilateral.jpg', image_salt_pepper_median_bilateral)


# 网格搜索下，看看参数变化对高斯滤波效果的影响
def explore_gaussian_filter_parameter():
    I1 = cv2.imread('./Q1_output/I1.jpg', cv2.IMREAD_GRAYSCALE)
    image_gaussian_noise = cv2.imread('./Q2_output/I1_gaussian.jpg', cv2.IMREAD_GRAYSCALE)
    best_psnr = 0
    best_sigma = 0
    best_kernel_size = 0
    # psnrs = []
    # sigmas = []
    kernel_sizes = []
    for sigma in np.arange(0.1, 3.0, 0.1):
        for kernel_size in range(1, 20, 2):
            image_gaussian_gaussian = gaussian_filter(image_gaussian_noise, kernel_size, sigma)
            psnr_gaussian = cv2.PSNR(I1, image_gaussian_gaussian)
            # psnrs.append(psnr_gaussian)
            # sigmas.append(sigma)
            # kernel_sizes.append(kernel_size)
            if psnr_gaussian > best_psnr:
                best_psnr = psnr_gaussian
                best_sigma = sigma
                best_kernel_size = kernel_size
    print("Best PSNR of Gaussian filter: ", best_psnr)
    print("Best sigma: ", best_sigma)
    print("Best kernel size: ", best_kernel_size)

    # 绘制PSNR随着sigma和kernel size变化的图像
    # fig = plt.figure(figsize=(10, 5))
    # ax1 = fig.add_subplot(121)
    # ax2 = fig.add_subplot(122)
    # ax1.scatter(sigmas, psnrs, color='b')
    # ax1.set_xlabel('Sigma')
    # ax1.set_ylabel('PSNR')
    # ax1.set_title('PSNR vs Sigma')
    # ax2.scatter(kernel_sizes, psnrs, color='r')
    # ax2.set_xlabel('Kernel Size')
    # ax2.set_ylabel('PSNR')
    # ax2.set_title('PSNR vs Kernel Size')
    # plt.show()


if __name__ == '__main__':
    process_gaussian_noise()
    process_poission_noise()
    process_salt_pepper_noise()
    # explore_gaussian_filter_parameter() # 找到1和7，但效果没啥变化
