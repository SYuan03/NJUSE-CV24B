import os

import numpy as np
import cv2
from skimage.util import random_noise
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import structural_similarity as compare_ssim


def add_noise(image, noise_type):
    if noise_type == "gaussian":
        noisy_image = random_noise(image, mode='gaussian', var=0.01)
    elif noise_type == "salt_pepper":
        noisy_image = random_noise(image, mode='s&p', amount=0.05)
    elif noise_type == "poisson":
        noisy_image = random_noise(image, mode='poisson')
    else:
        return image
    # 转换回[0, 255]区间的uint8类型
    noisy_image = (255 * noisy_image).astype(np.uint8)
    return noisy_image

def remove_noise(image, method):
    if method == "median":
        denoised_image = cv2.medianBlur(image, 5)
    elif method == "gaussian":
        denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    elif method == "bilateral":
        denoised_image = cv2.bilateralFilter(image, 9, 75, 75)
    else:
        return image
    return denoised_image

if __name__ == '__main__':
    # 读取图像
    image = cv2.imread('./I0.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    os.makedirs("Q4_output", exist_ok=True)

    # 添加噪声并保存
    noisy_images = {}
    for noise in ["gaussian", "salt_pepper", "poisson"]:
        noisy_images[noise] = add_noise(image, noise)
        cv2.imwrite(f'Q4_output/{noise}.jpg', cv2.cvtColor(noisy_images[noise], cv2.COLOR_RGB2BGR))

    # 去噪并保存
    denoised_images = {}
    for noise in noisy_images:
        denoised_images[noise] = {}
        for method in ["median", "gaussian", "bilateral"]:
            denoised_images[noise][method] = remove_noise(noisy_images[noise], method)
            cv2.imwrite(f'Q4_output/{noise}_{method}.jpg', cv2.cvtColor(denoised_images[noise][method], cv2.COLOR_RGB2BGR))

            # 计算PSNR和SSIM
            psnr = compare_psnr(image, denoised_images[noise][method])
            ssim = compare_ssim(image, denoised_images[noise][method], multichannel=True, channel_axis=-1)
            print(f'{noise}_{method} - PSNR: {psnr:.2f}, SSIM: {ssim:.4f}')

