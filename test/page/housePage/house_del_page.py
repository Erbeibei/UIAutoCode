from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page

__author__ = 'apple'

class HouseDelPage(Page, Browser):

    delButton_loc=(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td/span[5]")
    isYesButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")


    def click_delButton(self):
        self.find_element(*self.delButton_loc).click()

    def click_isYesButton(self):
        self.find_element(*self.isYesButton_loc).click()

    def click_cancel(self):
        self.find_element(*self.cancelButton_loc).click()
