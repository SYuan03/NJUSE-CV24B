import cv2
import numpy as np
import os


def extract_rgb_histogram(image_path, bins=8):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"无法读取图像文件: {image_path}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 计算直方图
    histogram = [cv2.calcHist([image], [i], None, [bins], [0, 256]) for i in range(3)]
    # ravel()将(3, 8)的数组变成(24,)的数组
    histogram = np.concatenate(histogram).ravel()
    # 比如q1是679*500，那么histogram.sum()=679*500*3
    histogram = histogram / histogram.sum()  # 归一化
    return histogram


# 处理文件夹中的所有图片
def process_images(folder_path):
    histograms = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                histograms[filename] = extract_rgb_histogram(file_path)
            except ValueError as e:
                print(e)
    return histograms


# 完成图片RGB直方图(24个bin总共)的提取
query_histograms = process_images('./images/query/')
database_histograms = process_images('./images/database/')

# 检索
# 计算相似度
# 每个query存储相似度最高的三个
results = {}
for query_name, query_histogram in query_histograms.items():
    similarities = []
    for database_name, database_histogram in database_histograms.items():
        # 相似度计算使用欧式距离
        similarity = np.linalg.norm(query_histogram - database_histogram)
        similarities.append((database_name, similarity))
    # 按相似度排序并取前三个
    similarities.sort(key=lambda x: x[1])
    results[query_name] = similarities[:3]
    # 后三个保存下相似度最小的三个，主要是对比下数值
    similarities.sort(key=lambda x: x[1], reverse=True)
    results[query_name] += similarities[:3]

# 打印结果
for query_name, top_matches in results.items():
    print(f"Query Image: {query_name}")
    # 前三个是相似度最高（也就是欧式距离最小）的
    print("Top 3 Matches:")
    for i, (match_name, similarity) in enumerate(top_matches[:3], start=1):
        print(f"  {i}. {match_name} - Similarity: {similarity:.2f}")
    # 后三个是相似度最低（也就是欧式距离最大）的
    print("Bottom 3 Matches:")
    for i, (match_name, similarity) in enumerate(top_matches[3:], start=1):
        print(f"  {i}. {match_name} - Similarity: {similarity:.2f}")
