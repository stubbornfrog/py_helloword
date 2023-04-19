# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/17
import time

import requests
from xml.dom.minidom import parse
import xml.dom.minidom

# authTicket=ssmall_shop_base_web0000018681351db30000a5e4aea0795634bbd753b8c3ef878d9445f2; authTicket.saamex0100010001=ssmall_shop_base_web0000018681351db30000a5e4aea0795634bbd753b8c3ef878d9445f2; JSESSIONID=1396EA21F3CA0605391EC40754118560; Hm_lvt_8a03b96c3de5e79bee6bb392c8eb4863=1677202142; Hm_lpvt_8a03b96c3de5e79bee6bb392c8eb4863=1677205010

temp_cookie = 'authTicket=ssmall_shop_base_web0000018695bc7fa60001695fee56c50908542f063c57ecd19091d9f8'

params = {"app_id": "saamex0100010001", "rack_parent_id": "16Y4L5Fb001300b8", "rack_id": "16Y4L7DQ00070000"}
response = requests.get("https://saas.e-pointchina.com.cn/shop/base/serv/rack/rack_for_single", params=params)
# print(response.text)

DOMTree = xml.dom.minidom.parseString(response.text)
root = DOMTree.documentElement
dataEle = root.getElementsByTagName("data")[0]
sectionEle = \
dataEle.getElementsByTagName("rack_goods_items")[0].getElementsByTagName("Map")[0].getElementsByTagName("section_id")[0]
goodsEle = \
dataEle.getElementsByTagName("rack_goods_items")[0].getElementsByTagName("Map")[0].getElementsByTagName("goods_id")[0]
sectionId = sectionEle.childNodes[0].nodeValue
goodId = goodsEle.childNodes[0].nodeValue

params2 = {"app_id": "saamex0100010001", "rack_id": "16Y4L7DQ00070000", "section_id": sectionId,
           "goods_id": goodId, "platform": "WAP"}
response2 = requests.get("https://saas.e-pointchina.com.cn/shop/base/serv/rack/price_list_new", params=params2)

DOMTree = xml.dom.minidom.parseString(response2.text)
root = DOMTree.documentElement
dataEle = root.getElementsByTagName("datas")[0]
sectionEle = dataEle.getElementsByTagName("Map")[0].getElementsByTagName("price_item_id")[0]
priceItemId = sectionEle.childNodes[0].nodeValue

data = {'app_id': 'saamex0100010001',
        'rack_id': '16Y4L7DQ00070000',
        'section_id': sectionId,
        'goods_id': goodId,
        'price_item_id': priceItemId,
        'goods_count': 1,
        'random_open_flag': 0,
        'ew_open_flag': 0,
        'point_open_flag': 0,
        'voucher_open_flag': 0,
        'o2o_voucher_open_flag': 0,
        'ticket_open_flag': 0,
        'gtquery_flag': 1, }

cookies_dict = {}
for i in temp_cookie.split(';'):
    v = i.split("=")
    cookies_dict[v[0]] = v[1]

for i in range(10):
    requests_post = requests.post("https://saas.e-pointchina.com.cn/shop/base/serv/order/prepare_pay", data,
                              cookies=cookies_dict)
    print(requests_post.text)
    time.sleep(0.6)

