# -*- coding: utf-8 -*-
from slide_track_config import slide_track
import sys;sys.path.append("../")
import json
import random
import re
import time
import execjs
import requests
from requests import Session
from jiyan_captcha import restore_image
from ImageHelper import SlideCrack
from pointermove import get_pointermove, get_slide_trajectory


class Jiyan(object):
    def __init__(self):
        self.base_headers = {
            'authority': 'www.geetest.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.geetest.com/demo/slide-popup.html',
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        }
        self.session = Session()
        self.session.headers = self.base_headers
        self.challenge = ''
        self.gt = ''
        with open("./demo_fullpage.js", mode='r', encoding='utf-8') as fp:
            js_fun_text = fp.read()
            self.js_fun_compile_fullpage = execjs.compile(js_fun_text)

        with open("./demo_slide.js", mode='r', encoding='utf-8') as fp:
            js_fun_text = fp.read()
            self.js_fun_compile_slide = execjs.compile(js_fun_text)

    def register_slide(self):
        register_slide_url = "https://www.geetest.com/demo/gt/register-slide?t={}".format(int(time.time()*1000))
        try:
            response = self.session.get(url=register_slide_url)
            data = json.loads(response.text)
            self.challenge = data['challenge']
            self.gt = data['gt']
        except Exception as e:
            print(e)
            return None
        return response

    def register_cookie(self):
        time_ = int(time.time()*1000)
        # 获得cookie GeeTestUser
        get_type_url = "https://apiv6.geetest.com/gettype.php?gt={}&callback=geetest_{}".format(self.gt, time_)
        print(get_type_url)
        response = self.session.get(url=get_type_url)
        print(response.text)

        data = json.loads(re.findall('\((.*)\)', response.text, flags=re.S)[0])['data']
        data["gt"] = self.gt
        data["challenge"] = self.challenge
        time_ = int(time.time() * 1000)
        w_data = self.js_fun_compile_fullpage.call("get_w", data)
        print("w_", w_data)
        get_url = "https://apiv6.geetest.com/get.php?gt={}&challenge={}&lang=zh-cn&pt=0&client_type=web&w={}&callback=geetest_{}".format(self.gt, self.challenge, w_data['w'], time_)
        print(get_url)
        response = self.session.get(url=get_url)
        print(response.text)
        data = json.loads(re.findall('\((.*?)\)', response.text, flags=re.S)[0])['data']

        # 获得cookie GeeTestAjaxUser
        button_coordinate = (random.randint(864, 878), random.randint(301, 313))
        pointermove_traces = get_pointermove(button_coordinate)
        print(pointermove_traces)
        ajax_data_ = {
            "c": data["c"],
            "s": data["s"],
            "gt": self.gt,
            "challenge": self.challenge,
        }
        print(ajax_data_)
        ajax_w_data = self.js_fun_compile_fullpage.call("get_ajax_w", pointermove_traces, ajax_data_, w_data['aeskey'], w_data['data_i'])
        print("ajax_w_ ", ajax_w_data)
        ajax_url = "https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&pt=0&client_type=web&w={}&callback=geetest_{}".format(self.gt, self.challenge, ajax_w_data['w'], time_)
        print(ajax_url)
        response = self.session.get(url=ajax_url)
        print("ajax_url ", response.text)
        print(response.status_code)

    def download_picture(self, picture_url, picture_name):
        response = self.session.get('https://static.geetest.com/{}'.format(picture_url))
        picture_path = './{}.{}'.format(picture_name, picture_url.split(".")[-1])
        with open(picture_path, mode='wb') as fp:
            fp.write(response.content)

        return picture_path

    def get_slide_info(self):
        time_ = int(time.time() * 1000)
        url = 'https://api.geetest.com/get.php?is_next=true&type=slide3&gt={}&challenge={}&lang=zh-cn&https=true&protocol=https%3A%2F%2F&offline=false&product=popup&api_server=api.geetest.com&isPC=true&autoReset=true&width=100%25&callback=geetest_{}'.format(self.gt, self.challenge, time_)
        response = self.session.get(url=url)
        data = json.loads(re.findall('\((.*?)\)', response.text, flags=re.S)[0])
        self.gt = data['gt']
        self.challenge = data['challenge']
        print("slide_info ", data)
        return data

    def verify_slide_code_(self, data):
        fg_path = self.download_picture(data['slice'], 'fg')
        bg_basepath = self.download_picture(data['bg'], 'bg_base')
        bg_path = restore_image(bg_basepath, im_show=False, save_path='bg.png')
        out_picture_path = "result.png"
        sc = SlideCrack(fg_path, bg_path, out_picture_path, out_flag=True)
        scale_ratio = 1
        slide_length = sc.discern(scale_ratio) - 5
        print(slide_length)
        # 构造滑块轨迹    // 轨迹第一条是基于滑块左上角的坐标-20， -36， 0
        client_button_x_y = [random.randint(-36, -20), random.randint(-36, -20), 0]
        print(client_button_x_y)
        data['startclickX'] = 758 - client_button_x_y[0]
        data['startclickY'] = 468 - client_button_x_y[1]

        def get_track(offset=0):
            """根据偏移量获取轨迹"""
            for track in slide_track:
                if offset == track[-1][0]:
                    return track

        slide_trajectory_ = get_track(slide_length)
        startclicktime = slide_trajectory_[-1][2]

        # slide_trajectory_, startclicktime = get_slide_trajectory((slide_length, random.randint(5, 20)))


        data['startclicktime'] = startclicktime
        data['endclickX'] = data['startclickX'] + slide_length
        data['endclickY'] = data['startclickY'] + slide_trajectory_[-1][1]
        slide_trajectory = [client_button_x_y]
        slide_trajectory.extend(slide_trajectory_)
        print(slide_trajectory)
        data['mouse_data'] = slide_trajectory
        print(data)
        js_response = self.js_fun_compile_slide.call("get_verify_slide_code_w", data)
        print(js_response)
        time_ = int(time.time() * 1000)
        verify_slide_url = "https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&%24_BBF=0&client_type=web&w={}&callback=geetest_{}".format(self.gt, self.challenge, js_response['w'], time_)
        print(verify_slide_url)
        response = self.session.get(url=verify_slide_url)
        print(response.status_code)
        print(response.text)
        data = json.loads(re.findall('\((.*?)\)', response.text, flags=re.S)[0])
        return data

    def get_track(self, offset=0):
        """根据偏移量获取轨迹"""
        for track in slide_track:
            if offset == track[-1][0]:
                return track

    def verify_slide_code(self, data):
        fg_path = self.download_picture(data['slice'], 'fg')
        bg_basepath = self.download_picture(data['bg'], 'bg_base')
        bg_path = restore_image(bg_basepath, im_show=False, save_path='bg.png')
        out_picture_path = "result.png"
        sc = SlideCrack(fg_path, bg_path, out_picture_path, out_flag=True)
        scale_ratio = 1
        slide_length = sc.discern(scale_ratio) - 5
        print(slide_length)

        slide_trajectory = self.get_track(slide_length)
        startclicktime = slide_trajectory[-1][2]
        data['startclickX'] = 758 - slide_trajectory[0][0]
        data['startclickY'] = 468 - slide_trajectory[0][1]

        data['startclicktime'] = startclicktime
        data['endclickX'] = data['startclickX'] + slide_length
        data['endclickY'] = data['startclickY'] + slide_trajectory[-1][1]

        print(slide_trajectory)
        data['mouse_data'] = slide_trajectory
        print(data)
        js_response = self.js_fun_compile_slide.call("get_verify_slide_code_w", data)
        print(js_response)
        time_ = int(time.time() * 1000)
        verify_slide_url = "https://api.geetest.com/ajax.php?gt={}&challenge={}&lang=zh-cn&%24_BBF=0&client_type=web&w={}&callback=geetest_{}".format(self.gt, self.challenge, js_response['w'], time_)
        print(verify_slide_url)
        response = self.session.get(url=verify_slide_url)
        print(response.status_code)
        print(response.text)
        data = json.loads(re.findall('\((.*?)\)', response.text, flags=re.S)[0])
        return data

    def login(self, data):
        validate = data['validate']
        print(validate)
        login_url = 'https://www.geetest.com/demo/gt/validate-slide'
        requests_data = {"geetest_challenge": self.challenge,
                         "geetest_validate": validate,
                         "geetest_seccode": "{}|jordan".format(validate)}
        print(requests_data)
        headers = {
            'authority': 'www.geetest.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.geetest.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.geetest.com/demo/slide-popup.html',
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        }
        response = requests.post(login_url, data=requests_data, headers=headers)
        print("login ", response.status_code, response.text)

    def binding_verify_code(self):
        #  register-slide  注册 获取challenge和gt
        self.register_slide()
        # Set-Cookie: GeeTestUser,GeeTestAjaxUser
        self.register_cookie()


if __name__ == '__main__':
    # https://www.geetest.com/demo/slide-popup.html
    # 与页面绑定验证码
    jiyan = Jiyan()
    jiyan.binding_verify_code()
    # 获取滑块信息
    slide_info = jiyan.get_slide_info()
    # 验证滑块
    verify_slide_info = jiyan.verify_slide_code(slide_info)
    # 登录
    jiyan.login(verify_slide_info)





















