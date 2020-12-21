from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
sys.setrecursionlimit(100000)
"""
首页元素定位
url:http://www.zhongye.net/###
封装登录页所有页面元素用于case统一调用
"""


class HomePage(Page, Browser):
    #   元素定位及实现
    username_loc = (By.ID, 'txtname')
    password_loc = (By.ID, 'txtpass')
    loginBtn_loc = (By.ID, 'loginBtn')
    registerBtn_loc = (By.CLASS_NAME, 'regist')

    ##登录账号
    def input_username(self, username):
        logger.info("输入账号：%s", username)
        self.find_element(*self.username_loc).send_keys(username)

    ##登录密码
    def input_password(self, password):
        logger.info("输入密码：%s", password)
        self.find_element(*self.password_loc).send_keys(password)

    ##登录按钮
    def loginBtn_click(self):
        logger.info("登录按钮点击")
        self.find_element(*self.loginBtn_loc).click()

    ##免费注册按钮
    def registerBtn_click(self):
        logger.info("免费注册按钮点击")
        self.find_element(*self.registerBtn_loc).click()
