from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
sys.setrecursionlimit(100000)
"""
首页元素定位
url:http://api.iscportal.isc.glb.cmos:50002/iscportal/index.html#/
封装登录页所有页面元素用于case统一调用
"""


class HomePage(Page, Browser):
    #   元素定位及实现
    username_loc = (By.CLASS_NAME, 'login_ipt_user')
    password_loc = (By.CLASS_NAME, 'txtpass')
    sendCode_loc = (By.CLASS_NAME, 'send-code')
    inputCode_loc = (By.CLASS_NAME, 'item-inp-lo phone-code')
    loginBtn_loc = (By.CLASS_NAME, 'btn-box')

    ##登录账号
    def input_username(self, username):
        logger.info("输入账号：%s", username)
        self.find_element(*self.username_loc).send_keys(username)

    ##登录密码
    def input_password(self, password):
        logger.info("输入密码：%s", password)
        self.find_element(*self.password_loc).send_keys(password)

    ##获取验证码按钮
    def sendCode_clike(self):
        logger.info("点击获取验证码按钮")
        self.find_element(*self.sendCode_loc).click()

    ##验证码录入，测试环境默认123456
    def input_sendCode(self):
        logger.info("验证码录入")
        self.find_element(*self.inputCode_loc).send_keys('123456')

    ##登录按钮
    def loginBtn_click(self):
        logger.info("登录按钮点击")
        self.find_element(*self.loginBtn_loc).click()


