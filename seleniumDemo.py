# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/17
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(2)
print("网站名称：{}".format(driver.title))
driver.find_element("id", "kw").send_keys("牛蛙君")
driver.find_element("id", "su").click()
time.sleep(5)
driver.close()

