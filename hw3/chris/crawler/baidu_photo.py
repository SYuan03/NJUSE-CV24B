import os
import re
import requests


def get_images_from_baidu(keyword, page_num, save_dir, file_name_custom):
    """
    从百度图片搜索获取图片并保存到本地。

    参数:
    keyword (str): 搜索关键词
    page_num (int): 页数
    save_dir (str): 图片保存目录
    """
    # 设置请求头，模拟浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }

    # 请求的基础URL
    url = 'https://image.baidu.com/search/acjson?'

    number = 1;
    # 遍历每一页
    for pn in range(0, 30 * page_num, 30):
        # 请求参数
        params = {
            'tn': 'resultjson_com',
            'logid': '7603311155072595725',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': '',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': '',  # 这个参数未公开，但不可缺少
            'pn': pn,  # 分页参数
            'rn': '30',  # 每页显示30条
            'gsm': '1e',
            '1618827096642': ''
        }

        # 发送请求
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            print('Request successful.')
        else:
            print(f'Failed to fetch data: {response.status_code}')
            continue

        response.encoding = 'utf-8'

        # 使用正则表达式提取图片链接
        html = response.text
        image_url_list = re.findall('"thumbURL":"(.*?)",', html, re.S)

        # 创建保存目录（如果不存在）
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 保存图片
        for img_url in image_url_list:
            try:
                img_data = requests.get(img_url).content
                img_name = os.path.join(save_dir, f"{file_name_custom}_{number}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)
                print(f'Saved image {img_name}')
                number += 1
            except Exception as e:
                print(f'Failed to save image {img_url}: {e}')


if __name__ == '__main__':
    get_images_from_baidu('南京大学鼓楼校区北大楼', 2, './images', "BeiDalou")
