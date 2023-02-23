# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/23
import requests

params = {"app_id": "saamex0100010001",
          "ticket": "0277fd382b0a4d509f371a8d534c3b40",
          "sign": "ffff4eff66ba651d24a1052ca019939c",
          "client": "EC_WECHAT_MP",
          "ECORIGINCLIENT": "EC_WECHAT"}
response = requests.get("https://saas.e-pointchina.com.cn/shop/base/serv/entry/login", params=params)
print(response.text)
