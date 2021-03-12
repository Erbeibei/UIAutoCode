from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page
from utils.log import logger


__author__ = 'apple'

class HouseAddPage(Page,Browser):
    #菜单选择
    chooseModTree_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/div[1]")
    chooseHouseManageTree_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/ul/li[2]")
    #add按钮
    addButoon_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/button[1]")
    #add页
    belongToBuilding_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/span/div/div")
    buildListBox_loc = (By.XPATH,"/html/body/div[4]/div/div/div/ul/li")

    belongToUnit_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/div/div")
    unitListBox_loc = (By.XPATH,"/html/body/div[5]/div/div/div/ul/li")

    belongToFloor_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span/div/div")
    floorListBox_loc = (By.XPATH,"/html/body/div[6]/div/div/div/ul/li[1]")

    roomName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div/span/input")
    roomId_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/span/div/div")
    chooseRoomId_loc = (By.XPATH,"/html/body/div[7]/div/div/div/ul/li[1]")

    #操作按钮
    saveButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    cancelButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")

    def click_chooseModTree(self):
        self.find_element(*self.chooseModTree_loc).click()

    def click_chooseHouseManageTree(self):
        self.find_element(*self.chooseHouseManageTree_loc).click()

    def click_addButton(self):
        self.find_element(*self.addButoon_loc).click()

    def click_belongToBuilding(self):
        self.find_element(*self.belongToBuilding_loc).click()#点开下拉框

    def click_buildListBox(self):
        self.find_elements(*self.buildListBox_loc)[-1].click()

    def click_belongTounit(self):
        self.find_element(*self.belongToUnit_loc).click()

    def click_unitListBox(self):
        self.find_elements(*self.unitListBox_loc)[0].click()

    def click_belongToFloor(self):
        self.find_element(*self.belongToFloor_loc).click()

    def click_floorListBox(self):
        self.find_elements(*self.floorListBox_loc)[0].click()

    def input_roomName(self,roomName):
        self.find_element(*self.roomName_loc).send_keys(roomName)

    def click_roomId(self):
        self.find_element(*self.roomId_loc).click()

    def click_chooseRoomId(self):
        self.find_elements(*self.chooseRoomId_loc)[0].click()

    def click_saveButton(self):
        self.find_element(*self.saveButton_loc).click()

    def click_cancelButton(self):
        self.find_element(*self.cancelButton_loc).click()
