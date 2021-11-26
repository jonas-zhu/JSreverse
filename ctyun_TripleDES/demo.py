# encoding:utf-8
import execjs
import requests

with open("./demo1.js", mode='r', encoding='utf-8') as fp:
    fun_text = fp.read()
    fun_compile = execjs.compile(fun_text)
email_ = "15779062300@163.com"
password_ = "zqasdxfjh."
parameter = fun_compile.call("get_parameter", email_, password_)

headers = {"Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
            "Host": "m.ctyun.cn",
            "Referer": "https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

url = f"https://m.ctyun.cn/account/login?userName={email_}&password={password_}&referrer=wap&mainVersion={parameter['mainVersion']}&comParam_curTime={parameter['mainVersion']}&comParam_seqCode={parameter['comParam_seqCode']}&comParam_signature={parameter['comParam_signature']}&isCheck=true&locale=zh-cn"

session = requests.session()

session.headers = headers

res = session.get(url)
print(res.text)




