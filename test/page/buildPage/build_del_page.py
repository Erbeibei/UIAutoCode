from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page

__author__ = 'apple'

class BuildDelPage(Page,Browser):

    delButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/span[4]")

    isYesButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")
    closeButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/button")

    def click_delButton(self):
        self.find_element(*self.delButton_loc).click()

    def click_isYesButton(self):
        self.find_element(*self.isYesButton_loc).click()

    def click_closeButton(self):
        self.find_element(*self.closeButton_loc).click()



