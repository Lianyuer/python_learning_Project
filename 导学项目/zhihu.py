import requests
import json
url = 'https://www.zhihu.com/question/338688699/answer/2538597933?utm_campaign=shareopn&utm_content=group1_Answer&utm_medium=social&utm_oi=948563202670379008&utm_psn=1557468984731230209&utm_source=wechat_session'
#使用工具包中的的get方法，向服务器发起请求

#User-Agent:，描述的是访问京东服务器的浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
resp = requests.get(url,headers=headers)
content = resp.text
print(content)
# #用空白替换掉多余的符号,最前和最后只保留{和}
# rest = content.replace('fetchJSON_comment98(','').replace(');','')
# json_data = json.loads(rest)
# comments = json_data['comments']
# for item in comments:
#     color = item['productColor']
#     size = item['productSize']
#     print(color)
#     print(size)


