__author__ = 'apple'
from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
sys.setrecursionlimit(100000)


class AdminAddPage(Page, Browser):
    #添加管理
    addAdminAcctButton_loc = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/button")
    adminName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span/span/input")
    adminTel_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/span/span/input")
    adminIdCard_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/span/span/input")
    adminSavaButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")

    def click_addAdminAcctButton(self):
        logger.info("点击添加管理员按钮")
        self.find_element(*self.addAdminAcctButton_loc).click()

    def input_adminName(self, adminName):
        logger.info("")
        self.find_element(*self.adminName_loc).send_keys(adminName)

    def input_adminTel(self, adminTel):
        logger.info("")
        self.find_element(*self.adminTel_loc).send_keys(adminTel)

    def input_adminIdCard(self, adminIdCard):
        logger.info("")
        self.find_element(*self.adminIdCard_loc).send_keys(adminIdCard)

    def click_adminSavaButton(self):
        self.find_element(*self.adminSavaButton_loc).click()

