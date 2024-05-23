import cv2
import numpy as np
import os


def extract_sift_features(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"无法读取图像文件: {image_path}")
    # 需要转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 初始化SIFT检测器
    sift = cv2.SIFT_create()
    # 检测关键点并计算描述子
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    if descriptors is None:
        descriptors = np.array([])
    return descriptors


# 处理文件夹中的所有图片
def process_images_sift(folder_path):
    sift_features = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                sift_features[filename] = extract_sift_features(file_path)
            except ValueError as e:
                print(e)
    return sift_features


# 完成图片SIFT特征的提取
query_sift_features = process_images_sift('./images/query/')
database_sift_features = process_images_sift('./images/database/')

# 检索
# 计算相似度
# 每个query存储相似度最高的三个
results = {}

# 使用暴力匹配器
bf = cv2.BFMatcher()

for query_name, query_descriptors in query_sift_features.items():
    similarities = []
    for database_name, database_descriptors in database_sift_features.items():
        if len(query_descriptors) == 0 or len(database_descriptors) == 0:
            continue
        # 使用KNN进行匹配，每个描述符找两个最近的邻居
        matches = bf.knnMatch(query_descriptors, database_descriptors, k=2)
        # 应用比值测试
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)
        # 以好的匹配数量作为相似度度量
        similarity = len(good_matches)
        similarities.append((database_name, similarity))
    # 按相似度排序并取前三个
    similarities.sort(key=lambda x: x[1], reverse=True)
    results[query_name] = similarities[:3]
    # 后三个保存下相似度最小的三个，主要是对比下数值
    similarities.sort(key=lambda x: x[1])
    results[query_name] += similarities[:3]

# 打印结果
for query_name, top_matches in results.items():
    print(f"Query Image: {query_name}")
    # 前三个是相似度最高（也就是匹配点最多）的
    print("Top 3 Matches:")
    for i, (match_name, similarity) in enumerate(top_matches[:3], start=1):
        print(f"  {i}. {match_name} - Similarity: {similarity}")
    # 后三个是相似度最低（也就是匹配点最少）的
    print("Bottom 3 Matches:")
    for i, (match_name, similarity) in enumerate(top_matches[3:], start=1):
        print(f"  {i}. {match_name} - Similarity: {similarity}")