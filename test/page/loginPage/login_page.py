__author__ = 'apple'
from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
sys.setrecursionlimit(100000)

class LoginPage(Page, Browser):
    userAcct_loc = (By.ID, "userName")
    userPwd_loc = (By.ID, "password")
    smsCodeButton_loc = (By.CLASS_NAME, "verificationCode")
    smsCode_loc = (By.ID, "verificationCode")
    checkbox_loc = (By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[4]")
    closeAlert_loc = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button")
    loginButton_loc = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/form/div[5]/div/div/span/button")
    def input_userAcct(self, userAcct):
        logger.info("输入账号：%s", userAcct)
        self.find_element(*self.userAcct_loc).send_keys(userAcct)

    def input_userPwd(self, userPwd):
        logger.info("输入密码：%s", userPwd)
        self.find_element(*self.userPwd_loc).send_keys(userPwd)

    def click_smsCodeButton(self):
        logger.info("点击获取验证码")
        self.find_element(*self.smsCodeButton_loc).click()

    def input_smsCode(self, smsCode):
        logger.info("输入验证码：%s", smsCode)
        self.find_element(*self.smsCode_loc).send_keys(smsCode)

    def click_checkbox(self):
        logger.info("勾选协议")
        self.find_element(*self.checkbox_loc).click()

    def click_closeAlert(self):
        logger.info("弹窗关闭")
        self.find_element(*self.closeAlert_loc).click()

    def click_loginButton(self):
        logger.info("点击登陆")
        self.find_element(*self.loginButton_loc).click()