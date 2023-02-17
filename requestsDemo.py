# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/17
import requests

html = requests.get("https://wwww.baidu.com")
print(html.text)
