from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page

__author__ = 'apple'


class BuildFindPage(Page,Browser):
    findButton_loc = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div")
    buildingName_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div[2]/div/span/input")
    submitButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/form/div/div[3]/button[2]")

    def click_findButton(self):
        self.find_element(*self.findButton_loc).click()

    def input_buildingName(self,buildingName):
        self.find_element(*self.buildingName_loc).clear()
        self.find_element(*self.buildingName_loc).send_keys(buildingName)

    def click_submitButton(self):
        self.find_element(*self.submitButton_loc).click()