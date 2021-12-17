# -*- coding: utf-8 -*-
# @Time: 2021/12/06 10:14
# creator by jonas_zhu
import random
import time
import re
import json
import copy
import execjs
from requests.sessions import Session
from ImageHelper import SlideCrack

session = Session()
timestamp = int(time.time())
base_headers = {
        'authority': 'captcha.fengkongcloud.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://fengkongcloud.com/',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    }


def get_picture_info():
    headers = copy.deepcopy(base_headers)
    params = (
        ('appId', 'default'),
        ('data', '{}'),
        ('callback', 'sm_{}'.format(timestamp)),
        ('lang', 'zh-cn'),
        ('organization', 'RlokQwRlVjUrTUlkIqOg'),
        ('channel', 'DEFAULT'),
        ('model', 'slide'),
        ('sdkver', '1.1.3'),
        ('rversion', '1.0.3'),
    )
    response = session.get('https://captcha.fengkongcloud.cn/ca/v1/register', headers=headers, params=params)
    result = re.findall(r'sm.*?\((.*)\)', response.text, flags=re.S)[0]
    info = json.loads(result)
    return info


def download_picture(picture_url, picture_name):
    headers = copy.deepcopy(base_headers)
    headers.update({'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                    'sec-fetch-dest': 'image'})
    response = session.get('https://castatic.fengkongcloud.cn{}'.format(picture_url), headers=headers)
    picture_path = './{}.png'.format(picture_name)
    with open(picture_path, mode='wb') as fp:
        fp.write(response.content)

    return picture_path

# 数美轨迹
def get_random_ge(distance):
    """
    生成随机的轨迹
    """
    ge = []

    y = 0
    v = 0
    t = 1
    current = 0
    mid = distance * 3 / 4
    exceed = 20
    z = t

    ge.append([0, 0, 1])

    while current < (distance + exceed):
        if current < mid / 2:
            a = 15
        elif current < mid:
            a = 20
        else:
            a = -30
        a /= 2
        v0 = v
        s = v0 * t + 0.5 * a * (t * t)
        current += int(s)
        v = v0 + a * t

        y += random.randint(-5, 5)
        z += 100 + random.randint(0, 10)

        ge.append([min(current, (distance + exceed)), y, z])

    while exceed > 0:
        exceed -= random.randint(0, 5)
        y += random.randint(-5, 5)
        z += 100 + random.randint(0, 10)
        ge.append([min(current, (distance + exceed)), y, z])

    return ge


# 获取请求路径
def get_verify_url_param(js_fun_compile, mouse_data, register_data):
    url_param = js_fun_compile.call("get_url_param", mouse_data, register_data)
    return url_param

def verify_slide_code(param):
    sm_time = int(time.time()*1000)
    param['callback'] = 'sm_{}'.format(sm_time)
    params = '&'.join(['{}={}'.format(key,value) for key, value in param.items()])
    url = 'https://captcha.fengkongcloud.cn/ca/v2/fverify?' + params
    print(url)
    response = session.get(url, headers=base_headers)
    print(response.text)
    print(response.status_code)
    return response


def main():
    # 1,获取滑块信息
    picture_info = get_picture_info()
    register_data = picture_info['detail']
    # print(register_data)
    # 2,下载滑块
    bg_path = download_picture(register_data['bg'], 'bg')
    fg_path = download_picture(register_data['fg'], 'fg')

    # 3,识别滑块缺口，获取需要移动的长度
    out_picture_path = "result.png"     # 处理结果图片,用红线标注识别的缺口
    sc = SlideCrack(fg_path, bg_path, out_picture_path, out_flag=True)

    # 图片Intrinsic aspect ratio:	2∶1    所以需要对移动的长度进行调整,缩小图片获取移动距离
    scale_ratio = 1
    slide_length = sc.discern(scale_ratio)/2

    # 4,构造滑动轨迹 [mouseMoveX, mouseMoveY, (当前轨迹的13位时间戳-第一次轨迹的13位时间戳)]
    """
    mouseMoveX: 滑块位置处水平移动距离
    mouseMoveY: 滑块位置处上下移动距离
    """
    mouse_data = get_random_ge(slide_length)
    print(mouse_data)
    print(len(mouse_data))
    url_param = get_verify_url_param(js_fun_compile, mouse_data, register_data)
    # print(url_param)
    # time.sleep(2)
    result = verify_slide_code(url_param)
    print(result)

if __name__ == '__main__':
    with open("./demo.js", mode='r', encoding='utf-8') as fp:
        js_fun_text = fp.read().replace('\xa9', '')
        js_fun_compile = execjs.compile(js_fun_text)

    for i in range(20):
        time.sleep(1)
        print(i)
        main()




