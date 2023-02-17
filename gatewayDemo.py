# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/2/17
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.17.81.21/login")
driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys("Arc_MMS123")
driver.find_element(By.CLASS_NAME, "el-button").click()
time.sleep(1)
driver.get("http://172.17.81.21/sourcemanage/materialManager")
time.sleep(1)
driver.find_element(By.XPATH, "//input[starts-with(@class, 'el-input__inner')]").send_keys("123")
driver.find_element(By.XPATH, "//button[starts-with(@class, 'el-button el-button--primary el-button--mini')]").click()
time.sleep(4)

driver.close()
