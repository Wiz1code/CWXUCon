# -*- coding: utf-8 -*-
# @Time    : 2022/12/4
# @Author  : Tianyu Tong
# @File    : connect.py

import time
import sys
import os
from typing import KeysView
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# 加启动配置
chrome_options = webdriver.ChromeOptions()
# 打开chrome浏览器
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])
chrome_options.add_argument('--disable-gpu')  # 上面代码就是为了将Chrome不弹出界面
chrome_options.add_argument('--start-maximized')#最大化
#chrome_options.add_argument('--headless')#无头浏览器
chrome_options.add_argument('--incognito')#无痕隐身模式
chrome_options.add_argument("disable-cache")#禁用缓存
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
web = webdriver.Chrome(options=chrome_options)

# web = webdriver.Edge() 

# web.maximize_window() 
# print("已全屏")
# 访问校园网网址
web.get("http://10.1.99.100/")

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

with open(os.path.join(BASE_DIR, "config.txt"),"r",encoding="gbk") as f:
    r = f.readlines()
    account = r[0]  # 读账号
    passwd = r[1]  # 读密码
    num = r[2] # 移动是1， 电信是2， 联通是3

try:
    print("@Author : Tianyu Tong")
    print("@School : Wuxi University\n")
    # 输入账号
    web.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[3]").send_keys(account)

    # 输入密码
    web.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[4]").send_keys(passwd)
    
    #选择运营商
    s1 = web.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/select")
    
    if num == "1" : Select(s1).select_by_value("@cmcc") # 移动
    if num == "2": Select(s1).select_by_value("@telecom") # 电信
    if num == "3": Select(s1).select_by_value("@unicom") # 联通

    # 登录按钮点击
    web.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[2]").click()
    print("\033[32mCurrent Login Account:%s\033[32m" % (account))

    print("登陆校园网中...")
    print("\033[32m登录成功（稍后窗口自动关闭）\033[0m")
    
    # 自动退出
    web.quit()
    
except:
    print("\033[31m终端IP已在线或密码错误！\033[0m")
    print("\033[93m详情访问http://10.1.99.100/\033[0m")
    web.quit()
    sys.exit()