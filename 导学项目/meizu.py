import requests
import json

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100014415029&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
resp = requests.get(url,headers=headers)
content = resp.text
rest = content.replace('fetchJSON_comment98(','').replace(');','')
json_data = json.loads(rest)
comments = json_data['comments']
for item in comments:
    color = item['productColor']
    size = item['productSize']
    print(color)
    print(size)
