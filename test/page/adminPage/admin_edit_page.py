__author__ = 'apple'
from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
from test.common.browser import Browser
import sys
import time
sys.setrecursionlimit(100000)


class AdminEditPage(Page, Browser):
    #编辑管理
    editAdminAcctButton_loc = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[1]")
    adminName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/input")
    adminTel_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span/input")
    adminIdCard_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/span/input")
    adminSavaButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")

    def click_editAdminAcctButton(self):
        logger.info("点击编辑管理员按钮")
        self.find_element(*self.editAdminAcctButton_loc).click()

    def input_adminName(self, adminName):
        self.find_element(*self.adminName_loc).clear()
        self.find_element(*self.adminName_loc).send_keys(adminName)

    def input_adminTel(self, adminTel):
        time.sleep(3)
        self.find_element(*self.adminTel_loc).click()
        self.find_element(*self.adminTel_loc).clear()
        self.find_element(*self.adminTel_loc).send_keys(adminTel)

    def input_adminIdCard(self, adminIdCard):
        logger.info("")
        self.find_element(*self.adminIdCard_loc).clear()
        # self.find_element(*self.adminIdCard_loc).send_keys(adminIdCard)

    def click_adminSavaButton(self):
        self.find_element(*self.adminSavaButton_loc).click()

