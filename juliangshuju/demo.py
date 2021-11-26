# encoding:utf-8
import json
import random
import time
import requests
from urllib import parse
import base64


# http://127.0.0.1:5620/business-demo/invoke?group=ws-group-juliang&action=clientTime
def get_signature(xhr_url, data):
    rpc_url = "http://127.0.0.1:5620/business-demo/invoke?group=ws-group-juliang&action=executeJs&xhrurl={}&param={}".format(parse.quote(xhr_url), parse.quote(json.dumps(data)))
    rpc_response = requests.get(rpc_url, verify=False)
    rpc_json = json.loads(rpc_response.text)
    return rpc_json['data']


def data_decrypt(data):
    rpc_url = "http://127.0.0.1:5620/business-demo/invoke?group=ws-group-juliang-data-decrypt&action=executeJs"
    data = {"param": base64.b64encode(data.encode()).decode()}
    rpc_response = requests.post(rpc_url, data, verify=False)
    return rpc_response.text


headers = {
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://trendinsight.oceanengine.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'Host': 'trendinsight.oceanengine.com',
}


keyword = "一加8"
start_date = "20210921"
end_date = "20211021"
keywords = ["一加8", "抖音", "罗永浩", "中国", "小米", "华为", "王者荣耀", "风景", "花园", "甘肃", "大学"]
start_time = time.time()


# 可以设置多个keyword查询
hot_trend_data = {"keyword_list": keywords, "start_date": start_date, "end_date": end_date, "app_name": "aweme"}
print(hot_trend_data)
hot_trend_xhr_url = 'https://trendinsight.oceanengine.com/api/open/index/get_multi_keyword_hot_trend'
hot_trend_url = get_signature(hot_trend_xhr_url, hot_trend_data)
print(hot_trend_url)
hot_trend_response = requests.post(hot_trend_url, headers=headers, data=json.dumps(hot_trend_data))
hot_trend_data = json.loads(hot_trend_response.text)
print(hot_trend_response.text)
result = data_decrypt(hot_trend_data['data'])
print(result)

portrait_data = {"param": {"keyword": keyword, "start_date": start_date, "end_date": end_date, "app_name": "aweme"}}
portrait_xhr_url = 'https://trendinsight.oceanengine.com/api/open/index/get_portrait'
portrait_url = get_signature(portrait_xhr_url, portrait_data)
print(portrait_url)
portrait_response = requests.post(portrait_url, headers=headers, data=json.dumps(portrait_data))
portrait_data = json.loads(portrait_response.text)
result = data_decrypt(portrait_data['data'])
print(result)

end_time = time.time()

print(end_time-start_time)

