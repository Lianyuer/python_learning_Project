import requests
import json
url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D4%AD%C9%F1%B1%DA%D6%BD%B3%AC%C7%E5%20%CA%D6%BB%FA%B1%DA%D6%BD&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDQsMSw2LDgsNywyLDUsOQ%3D%3D'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
resp = requests.get(url,headers=headers)
print(resp.text)