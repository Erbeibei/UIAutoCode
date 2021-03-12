from selenium.webdriver.common.by import By
from test.common.page import Page
from test.common.browser import Browser

__author__ = 'apple'

class MenuPage(Page,Browser):
    #系统管理
    systemManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[1]")
    adminManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[1]/ul/li")
    #区域管理
    regionManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]")
    buildingManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/ul/li[1]")
    houseManage_loc =(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/ul/li[2]")
    #住户管理
    householdManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]")
    ownerManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[1]")
    tenantManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[2]")
    keyAudit_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[3]")
    doorcardManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[4]")
    #设备管理
    deviceManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[4]")
    accessContro_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[4]/ul/li[1]")
    guardWarning_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[4]/ul/li[2]")
    #记录报表
    recordReport_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[5]")
    #物业管理
    estateManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[6]")
    noticeManage_loc = (By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[6]/ul/li")



    #
    def click_systemManage(self):
        self.find_element(*self.systemManage_loc).click()

    def click_adminManage(self):
        self.find_element(*self.adminManage_loc).click()

    def click_regionManage(self):
        self.find_element(*self.regionManage_loc).click()

    def click_buildingManage(self):
        self.find_element(*self.buildingManage_loc).click()

    def click_houseManage(self):
        self.find_element(*self.houseManage_loc).click()

    def click_householdManage(self):
        self.find_element(*self.householdManage_loc).click()

    def click_ownerManage(self):
        self.find_element(*self.ownerManage_loc).click()

    def click_tenantManage(self):
        self.find_element(*self.tenantManage_loc).click()

    def click_keyAudit(self):
        self.find_element(*self.keyAudit_loc).click()

    def click_doorcardManage(self):
        self.find_element(*self.doorcardManage_loc).click()

    def click_deviceManage(self):
        self.find_element(*self.deviceManage_loc).click()

    def click_accessContro(self):
        self.find_element(*self.doorcardManage_loc).click()

    def click_guardWarning(self):
        self.find_element(*self.guardWarning_loc).click()

    def click_recordReport(self):
        self.find_element(*self.recordReport_loc).click()

    def click_estateManage(self):
        self.find_element(*self.estateManage_loc).click()

    def click_noticeManage(self):
        self.find_element(*self.noticeManage_loc).click()