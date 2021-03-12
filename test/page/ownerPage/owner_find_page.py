__author__ = 'apple'
from selenium.webdriver.common.by import By
from test.common.page import Page
from test.common.browser import Browser
from utils.log import logger


__author__ = 'apple'

class OwnerFindPage(Page,Browser):
    searchButton_loc = (By.XPATH,"/html/body/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div")
    prsnName_loc = (By.ID,"prsnName")
    submitButton_loc =(By.XPATH,"/html/body/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/form/div/div[7]/button[2]")

    def click_searchButton(self):
        self.find_element(*self.searchButton_loc).click()

    def input_prsnName(self,prsnName):
        self.find_element(*self.prsnName_loc).send_keys(prsnName)

    def click_submitButton(self):
        self.find_element(*self.submitButton_loc).click()