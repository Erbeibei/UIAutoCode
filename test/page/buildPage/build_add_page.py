from selenium.webdriver.common.by import By
from test.common.browser import Browser
from test.common.page import Page


__author__ = 'apple'
class BuildAddPage(Page, Browser):
    #菜单-选择
    chooseModTree_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/div[1]")
    chooseBuildManageTree_loc = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/ul/li[1]")
    addButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/button")
    #楼栋
    buildingName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/input")
    buildingNo_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span/input")
    #1行
    unitNo_loc = (By.ID,"listCmpUnitDO[0].unitNo")
    floorCount_loc = (By.ID,"listCmpUnitDO[0].floorCount")
    roomCount_loc = (By.ID,"listCmpUnitDO[0].roomCount")
    #2行
    addLine_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div[4]/button")
    unitNo2_loc = (By.ID,"listCmpUnitDO[1].unitNo")
    floorCount2_loc = (By.ID,"listCmpUnitDO[1].floorCount")
    roomCount2_loc = (By.ID,"listCmpUnitDO[1].roomCount")
    #操作键
    cancelButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]")
    saveButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    closeButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/button/span")


    def click_chooseModTree(self):
        """
        选择楼栋管理
        """
        self.find_element(*self.chooseModTree_loc).click()

    def click_chooseBuildManageTree(self):
        self.find_element(*self.chooseBuildManageTree_loc).click()

    def click_addButton(self):
        self.find_element(*self.addButton_loc).click()

    def input_buildingName(self,buildingName):
        self.find_element(*self.buildingName_loc).send_keys(buildingName)

    def input_buildingNo(self,buildingNo):
        self.find_element(*self.buildingNo_loc).send_keys(buildingNo)

    def input_unitNo(self,unitNo):
        self.find_element(*self.unitNo_loc).send_keys(unitNo)

    def input_floorCount(self,floorCount):
        self.find_element(*self.floorCount_loc).send_keys(floorCount)

    def input_roomCount(self,roomCount):
        self.find_element(*self.roomCount_loc).send_keys(roomCount)

    def click_addLine(self):
        self.find_element(*self.addLine_loc).click()

    def input_unitNo2(self,unitNo2):
        self.find_element(*self.unitNo2_loc).send_keys(unitNo2)

    def input_floorCount2(self,floorCount2):
        self.find_element(*self.floorCount2_loc).send_keys(floorCount2)

    def input_roomCount2(self,roomCount2):
        self.find_element(*self.roomCount2_loc).send_keys(roomCount2)

    def click_cancelButton(self):
        self.find_element(*self.cancelButton_loc).click()

    def click_saveButton(self):
        self.find_element(*self.saveButton_loc).click()

    def click_closeButton(self):
        self.find_element(*self.closeButton_loc).click()