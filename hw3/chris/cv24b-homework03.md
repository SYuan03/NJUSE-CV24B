# 《计算机视觉》（本科，2024）作业3

<table style="border-collapse: separate; border-spacing: 5px; border: none;">
  <tr>
    <td style="border: none; font-size: 15px;" align="center">丁晟元</td>
    <td style="border: none; font-size: 15px;" align="center">杜凌霄</td>
  </tr>
  <tr>
    <td style="border: none; font-size: 15px;" align="center">211250097</td>
    <td style="border: none; font-size: 15px;" align="center">211250066</td>
  </tr>
</table>
## Q1

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">在搜索引擎上按照某一关键词，搜索50张不同的图像，从中选出5张作为检索请求，另45张作为被检索图像。</p>
</div>

使用爬虫，在**百度图片**进行搜索，关键词为**“南京大学鼓楼校区北大楼”**，先爬取了90张图片（以防有不相关的，因此先多爬取了点，例如结果中有爬到了紫峰大厦），经过筛选后留下的5+45如下所示：

这5张图像虽然都是北大楼，但是差异较为明显，也算是选了比较清晰的不同时间和视角的北大楼

### 5张检索请求图像

| ![q1](cv24b-homework03/q1.jpg) | ![q2](cv24b-homework03/q2.jpg) | ![q3](cv24b-homework03/q3.jpg) | ![q4](cv24b-homework03/q4.jpg) | ![q5](cv24b-homework03/q5.jpg) |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |

### 45张被检索图像

| ![s_1](cv24b-homework03/s_1.jpg) | ![s_2](cv24b-homework03/s_2.jpg) | ![s_3](cv24b-homework03/s_3.jpg) | ![s_4](cv24b-homework03/s_4.jpg) | ![s_5](cv24b-homework03/s_5.jpg) |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| ![s_6](cv24b-homework03/s_6.jpg) | ![s_7](cv24b-homework03/s_7.jpg) | ![s_8](cv24b-homework03/s_8.jpg) | ![s_9](cv24b-homework03/s_9.jpg) | ![s_10](cv24b-homework03/s_10.jpg) |
| ![s_11](cv24b-homework03/s_11.jpg) | ![s_12](cv24b-homework03/s_12.jpg) | ![s_13](cv24b-homework03/s_13.jpg) | ![s_14](cv24b-homework03/s_14.jpg) | ![s_15](cv24b-homework03/s_15.jpg) |
| ![s_16](cv24b-homework03/s_16.jpg) | ![s_17](cv24b-homework03/s_17.jpg) | ![s_18](cv24b-homework03/s_18.jpg) | ![s_19](cv24b-homework03/s_19.jpg) | ![s_20](cv24b-homework03/s_20.jpg) |
| ![s_21](cv24b-homework03/s_21.jpg) | ![s_22](cv24b-homework03/s_22.jpg) | ![s_23](cv24b-homework03/s_23.jpg) | ![s_24](cv24b-homework03/s_24.jpg) | ![s_25](cv24b-homework03/s_25.jpg) |
| ![s_26](cv24b-homework03/s_26.jpg) | ![s_27](cv24b-homework03/s_27.jpg) | ![s_28](cv24b-homework03/s_28.jpg) | ![s_29](cv24b-homework03/s_29.jpg) | ![s_30](cv24b-homework03/s_30.jpg) |
| ![s_31](cv24b-homework03/s_31.jpg) | ![s_32](cv24b-homework03/s_32.jpg) | ![s_33](cv24b-homework03/s_33.jpg) | ![s_34](cv24b-homework03/s_34.jpg) | ![s_35](cv24b-homework03/s_35.jpg) |
| ![s_36](cv24b-homework03/s_36.jpg) | ![s_37](cv24b-homework03/s_37.jpg) | ![s_38](cv24b-homework03/s_38.jpg) | ![s_39](cv24b-homework03/s_39.jpg) | ![s_40](cv24b-homework03/s_40.jpg) |
| ![s_41](cv24b-homework03/s_41.jpg) | ![s_42](cv24b-homework03/s_42.jpg) | ![s_43](cv24b-homework03/s_43.jpg) | ![s_44](cv24b-homework03/s_44.jpg) | ![s_45](cv24b-homework03/s_45.jpg) |

## Q2

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">以全局RGB颜色直方图（每通道bin的数量为8）作为特征，进行图像检索。展示每个检索请求及对应前3个结果。</p>
</div>
### 特征抽取代码（全局RGB颜色直方图）

```python
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
```

### 检索（特征匹配）代码

```python
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
```

### 结果

程序运行结果如下

| <img src="cv24b-homework03/image-20240524001506089.png" alt="image-20240524001506089" style="zoom:50%;" /> | <img src="cv24b-homework03/image-20240524001546272.png" alt="image-20240524001546272" style="zoom:50%;" /> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

|              query               |                        top1                         |                        top2                         |                        top3                         |
| :------------------------------: | :-------------------------------------------------: | :-------------------------------------------------: | :-------------------------------------------------: |
|                q1                |                         32                          |                         10                          |                         40                          |
| ![q_1](cv24b-homework03/q_1.jpg) | ![s_32](cv24b-homework03/s_32-1716481408687-6.jpg)  | ![s_10](cv24b-homework03/s_10-1716481417409-8.jpg)  | ![s_40](cv24b-homework03/s_40-1716481422716-10.jpg) |
|                q2                |                         14                          |                         16                          |                          8                          |
| ![q_2](cv24b-homework03/q_2.jpg) | ![s_14](cv24b-homework03/s_14-1716481618764-21.jpg) | ![s_16](cv24b-homework03/s_16-1716481623052-23.jpg) |  ![s_8](cv24b-homework03/s_8-1716481629050-25.jpg)  |
|                q3                |                         30                          |                         15                          |                          3                          |
| ![q_3](cv24b-homework03/q_3.jpg) | ![s_30](cv24b-homework03/s_30-1716481667138-27.jpg) | ![s_15](cv24b-homework03/s_15-1716481673960-29.jpg) |  ![s_3](cv24b-homework03/s_3-1716481676652-31.jpg)  |
|                q4                |                         32                          |                         40                          |                         36                          |
| ![q_4](cv24b-homework03/q_4.jpg) | ![s_32](cv24b-homework03/s_32-1716481697485-33.jpg) | ![s_40](cv24b-homework03/s_40-1716481704022-35.jpg) | ![s_36](cv24b-homework03/s_36-1716481708437-37.jpg) |
|                q5                |                         43                          |                         13                          |                          9                          |
| ![q_5](cv24b-homework03/q_5.jpg) | ![s_43](cv24b-homework03/s_43-1716481734603-39.jpg) | ![s_13](cv24b-homework03/s_13-1716481740942-41.jpg) |  ![s_9](cv24b-homework03/s_9-1716481749808-43.jpg)  |



## Q3

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">选择SIFT特征，重复问题2。</p>
</div>
### SIFT特征抽取代码的来源及说明

### SIFT特征匹配代码的来源及说明

（检索请求+前3个结果）

### 结果

程序执行结果如下

| <img src="cv24b-homework03/image-20240524010558760.png" alt="image-20240524010558760" style="zoom: 67%;" /> | <img src="cv24b-homework03/image-20240524010619470.png" alt="image-20240524010619470" style="zoom: 67%;" /> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

> 注，topk列如 29(170)代表s_29.jpg，与相对应query相似度计算是170

|                       query                       |                        top1                         |                        top2                         |                        top3                         |
| :-----------------------------------------------: | :-------------------------------------------------: | :-------------------------------------------------: | :-------------------------------------------------: |
|                        q1                         |                       29(170)                       |                       28(158)                       |                       37(81)                        |
| ![q_1](cv24b-homework03/q_1-1716484312602-45.jpg) | ![s_29](cv24b-homework03/s_29-1716484338914-55.jpg) | ![s_28](cv24b-homework03/s_28-1716484349509-57.jpg) | ![s_37](cv24b-homework03/s_37-1716484355775-59.jpg) |
|                        q2                         |                       20(39)                        |                       29(24)                        |                       12(23)                        |
| ![q_2](cv24b-homework03/q_2-1716484316244-47.jpg) | ![s_20](cv24b-homework03/s_20-1716484366951-61.jpg) | ![s_29](cv24b-homework03/s_29-1716484374257-63.jpg) | ![s_12](cv24b-homework03/s_12-1716484379709-65.jpg) |
|                        q3                         |                        6(75)                        |                       37(56)                        |                       24(53)                        |
| ![q_3](cv24b-homework03/q_3-1716484319550-49.jpg) |  ![s_6](cv24b-homework03/s_6-1716484385513-67.jpg)  | ![s_37](cv24b-homework03/s_37-1716484390449-69.jpg) | ![s_24](cv24b-homework03/s_24-1716484397832-71.jpg) |
|                        q4                         |                       29(59)                        |                       44(52)                        |                       42(46)                        |
| ![q_4](cv24b-homework03/q_4-1716484322213-51.jpg) | ![s_29](cv24b-homework03/s_29-1716484405247-73.jpg) | ![s_44](cv24b-homework03/s_44-1716484410356-75.jpg) | ![s_42](cv24b-homework03/s_42-1716484413736-77.jpg) |
|                        q5                         |                        5(44)                        |                       33(38)                        |                        4(34)                        |
| ![q_5](cv24b-homework03/q_5-1716484324931-53.jpg) |  ![s_5](cv24b-homework03/s_5-1716484421315-79.jpg)  | ![s_33](cv24b-homework03/s_33-1716484426706-81.jpg) |  ![s_4](cv24b-homework03/s_4-1716484430909-83.jpg)  |



## Q4

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">将问题2和问题3的结果进行比较和分析。</p>
</div>
## 比较和分析

感觉RGB颜色直方图在我的这个实验环境下很容易受比如“天空”“草地”颜色的干扰，导致我认为是主体的“北大楼”并不一定被很好匹配

