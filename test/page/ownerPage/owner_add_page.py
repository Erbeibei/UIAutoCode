from selenium.webdriver.common.by import By
from test.common.page import Page
from test.common.browser import Browser
from utils.log import logger


__author__ = 'apple'

class OwnerAddPage(Page,Browser):
    #add
    addButton_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/button[1]")
    #选择小区信息
    belongToBuilding_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div")
    buildListBox_loc = (By.XPATH,"/html/body/div[4]/div/div/div/ul/li")

    belongToUnit_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/span/div/div")
    unitListBox_loc = (By.XPATH,"/html/body/div[5]/div/div/div/ul/li")

    belongToFloor_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/div/span/div/div")
    floorListBox_loc = (By.XPATH,"/html/body/div[6]/div/div/div/ul/li[1]")

    roomId_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[5]/div/div[2]/div/span/div/div/div/div")
    chooseRoomId_loc = (By.XPATH,"/html/body/div[7]/div/div/div/ul/li")

    def click_addButton(self):
        self.find_element(*self.addButton_loc).click()

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

    def click_roomId(self):
        self.find_element(*self.roomId_loc).click()

    def click_chooseRoomId(self):
        self.find_elements(*self.chooseRoomId_loc)[0].click()

    #业主
    customName_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/span/input")
    customType_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div")
    chooseCustomType_loc = (By.XPATH,"/html/body/div[8]/div/div/div/ul/li")
    customTel_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/div[2]/div/span/input")
    # customTel2_loc = (By.XPATH,"")
    # customIdcard_loc = (By.XPATH,"")
    imgFile_loc = (By.XPATH,'//*[@id="customs.0.prsnImgUrl"]')

    def input_customName(self, customName):
        self.find_element(*self.customName_loc).send_keys(customName)

    def click_customType(self):
        self.find_element(*self.customType_loc).click()

    def click_chooseCustomType(self):
        self.find_elements(*self.chooseCustomType_loc)[-1].click()

    def input_customTel(self,customTel):
        self.find_element(*self.customTel_loc).send_keys(customTel)

    def input_imgFile(self,imgFile):
        logger.info(self.find_element(*self.imgFile_loc))
        self.find_element(*self.imgFile_loc).send_keys(imgFile)

    #业主成员
    addMemberButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/button")
    memberName_loc = (By.ID,"customs.0.prsnName")
    memberType_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div/div/div")
    chooseMemberType_loc = (By.XPATH,"/html/body/div[8]/div/div/div/ul/li")
    memberTel_loc = (By.ID,"customs.0.prsnPhone")
    # memberTel2_loc = (By.XPATH,"")
    # memberIdcard_loc = (By.XPATH,"")


    def click_addMemberButton(self):
        self.find_element(*self.addMemberButton_loc).click()

    def input_memberName(self, memberName):
        self.find_element(*self.memberName_loc).send_keys(memberName)

    def click_memberType(self):
        self.find_element(*self.memberType_loc).click()

    def click_chooseMemberType(self):
        self.find_elements(*self.chooseMemberType_loc)[0].click()

    def input_memberTel(self,memberTel):
        self.find_element(*self.memberTel_loc).send_keys(memberTel)


    #操作
    saveButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    def click_saveButton(self):
        self.find_element(*self.saveButton_loc).click()
