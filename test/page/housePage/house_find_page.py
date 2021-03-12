from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page

__author__ = 'apple'

class HouseFindPage(Page, Browser):


    roomName_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/form/div/div[3]/div/div[2]/div/span/input")
    findButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/form/div/div[6]/button[2]")
    screenButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div")

    def input_roomName(self,roomName):
        self.find_element(*self.roomName_loc).clear()
        self.find_element(*self.roomName_loc).send_keys(roomName)

    def click_findButton(self):
        self.find_element(*self.findButton_loc).click()

    def click_screenButton(self):
        self.find_element(*self.screenButton_loc).click()