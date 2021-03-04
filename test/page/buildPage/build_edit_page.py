__author__ = 'apple'
from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page


class BuildEditPage(Page,Browser):
    editButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[6]/span[3]")

    buildingName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/input")
    floorCount_loc = (By.ID,"listCmpUnitDO[0].floorCount")

    saveButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")



    def click_editButton(self):
        self.find_element(*self.editButton_loc).click()

    def input_buildingName(self,buildingName):
        self.find_element(*self.buildingName_loc).clear()
        self.find_element(*self.buildingName_loc).send_keys(buildingName)

    def input_floorCount(self,floorCount):
        self.find_element(*self.floorCount_loc).clear()
        self.find_element(*self.floorCount_loc).send_keys(floorCount)

    def click_saveButton(self):
        self.find_element(*self.saveButton_loc).click()
