import requests
import json
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8240108&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
#使用工具包中的的get方法，向服务器发起请求
"""
   京东服务器发现你使用python程序访问他的服务器时会对你的请求进行拦截
   让puthon程序添加请求头去伪装成浏览器去访问京东服务器
"""
#User-Agent:，描述的是访问京东服务器的浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
resp = requests.get(url,headers=headers)
content = resp.text
#用空白替换掉多余的符号,最前和最后只保留{和}
rest = content.replace('fetchJSON_comment98(','').replace(');','')
json_data = json.loads(rest)
comments = json_data['comments']
for item in comments:
    color = item['productColor']
    size = item['productSize']
    print(color)
    print(size)


