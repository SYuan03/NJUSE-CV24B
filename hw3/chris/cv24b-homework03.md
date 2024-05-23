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

## 45张被检索图像

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

【特征抽取代码贴这里】

【检索（特征匹配）代码贴这里】

【结果（检索请求+前3个结果）贴这里】

## Q3

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">选择SIFT特征，重复问题2。</p>
</div>

【SIFT特征抽取代码的来源及说明贴这里】

【SIFT特征匹配代码的来源及说明贴这里】

【结果（检索请求+前3个结果）贴这里】

## Q4

<div style="border: 2px solid #000; padding: 6px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 10px;">
  <span style="font-weight: bold; font-size: 12px;">要求说明</span>
  <p style="margin: 4px 0;">将问题2和问题3的结果进行比较和分析。</p>
</div>

【比较和分析结果贴这里】

