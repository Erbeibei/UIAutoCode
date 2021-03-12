__author__ = 'apple'
from selenium.webdriver.common.by import By
from test.common.page import Page
from test.common.browser import Browser
from utils.log import logger


__author__ = 'apple'

class OwnerDelPage(Page,Browser):
    ##点击注销按钮
    delButton_loc = (By.XPATH,"/html/body/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td/span/a[2]")
    # ##操作键
    isYesButton_loc = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelButton_loc = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]")

    def click_delButton(self):
        self.find_element(*self.delButton_loc).click()

    def click_isYesButton(self):
        self.find_element(*self.isYesButton_loc).click()

    def click_cancelButton(self):
        self.find_element(*self.cancelButton_loc).click()
