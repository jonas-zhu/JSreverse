# -*- coding:utf-8 -*-
# author:bridge
# time:2020/4/7
import json
import re
import requests
import random
from urllib.parse import quote
from lxml import etree


# 获取参数k和参数h
def get_k_h(url):
    b = int(random.random() * 100) + 1
    a = url.find("url=")
    url = url + "&k=" + str(b) + "&h=" + url[a + 4 + 21 + b: a + 4 + 21 + b + 1]
    return url

# 获取suv url的参数
def get_uigs_para(response):
    uigs_para = re.findall('var uigs_para = (.*?);', response.text, re.S)[0]
    if 'passportUserId ? "1" : "0"' in uigs_para:
        uigs_para = uigs_para.replace('passportUserId ? "1" : "0"', '0')
    uigs_para = json.loads(uigs_para)
    exp_id = re.findall('uigs_para.exp_id = "(.*?)";', response.text, re.S)[0]
    uigs_para['right'] = 'right0_0'
    uigs_para['exp_id'] = exp_id[:-1]
    return uigs_para


# 根据用户传递过来的公众号的名字-query构造搜索url
query_word = '进击的Coder'
weixinhao = 'FightingCoder'
search_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + quote(query_word)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'weixin.sogou.com',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
search_response = requests.get(url=search_url, headers=headers)

# 解析搜索的响应内容，找出匹配的公众号query。
search_html = etree.HTML(search_response.text)
news_boxs = search_html.xpath("//ul[@class='news-list2']/li")
news_url = ''
for news in news_boxs:
    try:
        weixinhao_temp = news.xpath(".//label[@name='em_weixinhao']/text()")[0]
        if weixinhao_temp == weixinhao:
            news_url = 'https://weixin.sogou.com/' + news.xpath("./dl/dd/a/@href")[0]
    except:
        pass
if news_url == '':
    print('没有这个公众号')
# 为url添加k和h参数
news_url = get_k_h(news_url)
# 请求含有k、h参数的new_url，还需要设置相应的cookie，这个时候会返回的响应体里面会含有正确的微信url。

# 处理cookie
# 1. 得到ABTEST、SNUID、IPLOC、SUID1：
SetCookie = search_response.headers['Set-Cookie']
cookie_params = {
    "ABTEST": re.findall('ABTEST=(.*?);', SetCookie, re.S)[0],
    "SNUID": re.findall('SNUID=(.*?);', SetCookie, re.S)[0],
    "IPLOC": re.findall('IPLOC=(.*?);', SetCookie, re.S)[0],
    "SUID": re.findall('SUID=(.*?);', SetCookie, re.S)[0]
}
# 2. 需要IPLOC、SNUID，得到SUID2：
getsuid_url = 'https://www.sogou.com/sug/css/m3.min.v.7.css'
getsuid_headers = {
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Cookie": "SNUID={}; IPLOC={}".format(cookie_params['SNUID'], cookie_params['IPLOC']),
    "Host": "www.sogou.com",
    "Referer": search_url,
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
getsuid_response = requests.get(getsuid_url, headers=getsuid_headers)
SetCookie = getsuid_response.headers['Set-Cookie']
cookie_params['SUID'] = re.findall('SUID=(.*?);', SetCookie, re.S)[0]

# 3. 需要ABTEST、IPLOC、SNUID、SUID，得到JSESSIONID：
getjsessionid_url = 'https://weixin.sogou.com/websearch/wexinurlenc_sogou_profile.jsp'
getjsessionid_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}".format(cookie_params['ABTEST'], cookie_params['SNUID'], cookie_params['IPLOC'],
                                                              cookie_params['SUID']),
    "Host": "weixin.sogou.com",
    "Referer": search_url,
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
getjsessionid_response = requests.get(url=getjsessionid_url, headers=getjsessionid_headers)
SetCookie = getjsessionid_response.headers['Set-Cookie']
cookie_params['JSESSIONID'] = re.findall('JSESSIONID=(.*?);', SetCookie, re.S)[0]

# 4. 需要IPLOC、SNUID、SUID，得到SUV, url链接的拼接，在search_reqponse里面
getsuv_url = "https://pb.sogou.com/pv.gif"
getsuv_headers = {
    "Accept": "image/webp,*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Cookie": "SNUID={}; IPLOC={}; SUID={}".format(cookie_params['SNUID'], cookie_params['IPLOC'], cookie_params['SUID']),
    "Host": "pb.sogou.com",
    "Referer": search_url,
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
uigs_para = get_uigs_para(response=search_response)
getsuv_response = requests.get(url=getsuv_url, headers=getsuv_headers, params=uigs_para)
SetCookie = getsuv_response.headers['Set-Cookie']
cookie_params['SUV'] = re.findall('SUV=(.*?);', SetCookie, re.S)[0]

# 利用含有k和h的文章链接获取真实的url链接
news_headers = {
    'Host': 'weixin.sogou.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Referer': search_url,
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'ABTEST={}; SNUID={}; IPLOC={}; SUID={}; JSESSIONID={}; SUID={}; SUV={}'.format(cookie_params['ABTEST'], cookie_params['SNUID'], cookie_params['IPLOC'], cookie_params['SUID'], cookie_params['JSESSIONID'], cookie_params['SUID'], cookie_params['SUV'])
}
nesw_response = requests.get(url=news_url, headers=news_headers)
fragments = re.findall("url \+= '(.*?)'", nesw_response.text, re.S)
realnews_url = ''
for fragment in fragments:
    realnews_url += fragment

realnews_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "user-agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
realnews_response = requests.get(url=realnews_url, headers=realnews_headers)
realnews_html = etree.HTML(realnews_response.text)
print(realnews_response.status_code)
print(realnews_html.xpath('//meta[@property="og:title"]/@content')[0])
print(realnews_url)
