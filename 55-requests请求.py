import requests

url = []
source_url = "https://get.xunfs.com/app/listapp.php"
data = {'a': 'get18', 
        'system': 'ios'}
r = requests.post(source_url, data=data)
old_url = eval(r.text)
# old_url = {"url1":"cl.98fxw7.info","url2":"cl.mhvrju.info","url3":"cl.vygvsg.info","urlprivate":"70","app":"NzEuZ2h1d3Mud2lu","app2":"NzAucGxheXN0YXRpb24taGstZ210LmNvbQ==","app3":"dXNlci5naHV3dC5zaG9w","update":"2025-03-26","note":"\u6700\u8fd1\u5730\u5740\u8b8a\u5316\u8f03\u591a\uff0c\u5982\u4e00\u6642\u7121\u6cd5\u8a2a\u554f\uff0c\u8acb\u5728\u8a2d\u7f6e\u4e2d\u6253\u958bSSL\u93c8\u63a5\u8a66\u8a66\u3002","appVer":"2.3.6"}  
# print(old_url)
url.append(old_url['url1'])
url.append(old_url['url2'])
url.append(old_url['url3'])

print(url)