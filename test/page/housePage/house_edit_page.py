from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page

__author__ = 'apple'

class HouseEditPage(Page,Browser):
    editButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td/span[4]")

    roomName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div/span/input")
    roomId_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/span/div/div")
    chooseRoomId_loc = (By.XPATH,"/html/body/div[4]/div/div/div/ul/li")

    #button
    saveButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelBUtton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")


    def click_editButton(self):
        self.find_element(*self.editButton_loc).click()

    def input_roomName(self,roomName):
        self.find_element(*self.roomName_loc).clear()
        self.find_element(*self.roomName_loc).send_keys(roomName)

    def click_roomId(self):
        self.find_element(*self.roomId_loc).click()

    def click_chooseRoomId(self):
        self.find_elements(*self.chooseRoomId_loc)[1].click()

    def click_saveButton(self):
        self.find_element(*self.saveButton_loc).click()

    def click_cancelButton(self):
        self.find_element(*self.cancelBUtton_loc).click()