from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
sys.setrecursionlimit(100000)
"""
注册页元素定位
url:http://www.zhongye.net/reg.aspx
封装注册页所有页面元素用于case统一调用
"""


class RegisterPage(Page, Browser):
    #   元素定位及实现
    telphone_loc = (By.ID, 'Telephone_TextBox1')#手机号码
    password_loc = (By.ID, 'Password_TextBox1')#密码
    confirmPassword_loc = (By.ID, 'Confirm_TextBox1')#确认密码
    classList_loc = (By.ID, 'DDL_ClassList')#感兴趣的课程
    selectClass_loc = (By.XPATH, '//*[@id="DDL_ClassList"]/option[21]')
    agreeArticle_loc = (By.ID, 'agreeArticle')#协议选取-我已阅读并同意
    submitBtn_loc = (By.ID, 'Submit')#注册按钮

    def input_telphone(self, telphone):
        logger.info("请输入手机号：%s", telphone)
        self.find_element(*self.telphone_loc).send_keys(telphone)

    def input_password(self, password):
        logger.info("请输入密码：%s", password)
        self.find_element(*self.password_loc).send_keys(password)

    def input_confirmPassword(self, confirmPassword):
        logger.info("请输入重复密码：%s", confirmPassword)
        self.find_element(*self.confirmPassword_loc).send_keys(confirmPassword)

    def classList_click(self):
        logger.info("点击课程打开课程列表")
        self.find_element(*self.classList_loc).click()

    def selectClass_click(self):
        logger.info("选择心爱的课程-日语")
        self.find_element(*self.selectClass_loc).click()

    def agreeArticle_click(self):
        logger.info("点击了一下协议按钮，当前状态...の")
        self.find_element(*self.agreeArticle_loc).click()

    def submitBtn_click(self):
        logger.info("点击了一下注册按钮...注册会成功嘛")
        self.find_element(*self.submitBtn_loc).click()