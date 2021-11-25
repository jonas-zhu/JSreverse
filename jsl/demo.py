# encoding:utf-8
import copy
import re
import execjs
import requests
from urllib import parse


def get_cookie(url_info, response):
    cookie_js_text = re.findall("<script>(.*?)</script>", response.content.decode('utf-8'), flags=re.S)[0]
    js_func_text = """
    window = global;
    navigator = {};
    window.navigator = navigator;
    navigator.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36";
    document = {};
    window.document = document;
    location = {};
    location.pathname='%s'; location.search='';
    setTimeout = function (val) {if (typeof val == "function") {val()}};
    function get_cookie() {%s;return window.document.cookie}
    """ % (url_info.path, cookie_js_text)
    js_func_compile = execjs.compile(js_func_text)
    cookie = js_func_compile.call("get_cookie")
    return {i.split("=")[0]: i.split("=")[1] for i in cookie.split(";")}


session = requests.session()
session.headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8"}


url = "https://www.mps.gov.cn/n2254098/n4904352/"
url_info = parse.urlparse(url)

first_response = session.get(url)
first_cookie = get_cookie(url_info, first_response)
session.cookies.update(first_cookie)

second_response = session.get(url)
second_cookie = get_cookie(url_info, second_response)
session.cookies.update(second_cookie)

result_response = session.get(url)
print(result_response.content.decode('utf-8'))
print(result_response.status_code)

response = session.get("https://www.mps.gov.cn/n2254098/n4904352/c8097774/content.html")
print(response.content.decode('utf-8'))
print(response.status_code)


