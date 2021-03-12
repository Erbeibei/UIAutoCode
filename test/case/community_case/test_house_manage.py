import unittest
from test.page.loginPage.login_page import LoginPage
from utils.config import Config, REPORT_PATH
from test.page.housePage.house_add_page import HouseAddPage
from test.page.housePage.house_find_page import HouseFindPage
from test.page.housePage.house_del_page import HouseDelPage
from test.page.housePage.house_edit_page import HouseEditPage
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from selenium.webdriver.common.by import By


class TestHouseManage(unittest.TestCase):
    ZHSQ_URL = Config().get('ZHSQ_URL')
    userAcct = Config().get('userAcct')
    userPwd = Config().get('userPwd')
    smsCode = Config().get('smsCode')
    """
    @前置
    description:登陆
    """
    def setUp(self):
        logger.info("----start---")
        self.login_page = LoginPage(browser_type='chrome').get(self.ZHSQ_URL, maximize_window=True)
        self.house_add_page = HouseAddPage(self.login_page)
        self.house_find_page = HouseFindPage(self.login_page)
        self.house_del_page = HouseDelPage(self.login_page)
        self.house_edit_page = HouseEditPage(self.login_page)

        try:

            self.login_page.click_checkbox()
            self.login_page.click_closeAlert()
            self.login_page.input_userAcct(self.userAcct)
            self.login_page.input_userPwd(self.userPwd)
            self.login_page.click_smsCodeButton()
            self.login_page.input_smsCode(self.smsCode)
            self.login_page.click_loginButton()
            self.login_page.wait()
            self.house_add_page.click_chooseModTree()
            self.house_add_page.click_chooseHouseManageTree()
            self.house_add_page.wait()
        except Exception as msg:
            self.login_page.save_screen_shot("test_login")
            logger.info("异常信息:%s" %msg)
            raise

    roomName = "101"
    def test_addHouse(self):
        try:
            self.house_add_page.click_addButton()
            self.house_add_page.wait()
            self.house_add_page.click_belongToBuilding()
            self.house_add_page.click_buildListBox()

            self.house_add_page.click_belongTounit()
            self.house_add_page.click_unitListBox()

            self.house_add_page.click_belongToFloor()
            self.house_add_page.click_floorListBox()

            self.house_add_page.input_roomName(self.roomName)

            self.house_add_page.click_roomId()
            self.house_add_page.click_chooseRoomId()

            self.house_add_page.click_saveButton()

            tipsStr = self.house_add_page.find_element(By.XPATH,"/html/body/div[2]/span/div[1]/div/div/span")
            if tipsStr is not None:
                self.assertEqual("新增房屋,成功",tipsStr.text,msg="新增房屋失败")
            else:
                self.assertIsNone(tipsStr,msg="元素定位失败")

            roomNameStr = self.house_add_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]")
            if roomNameStr is not None:
                self.assertEqual(self.roomName,roomNameStr.text,msg="断言失败")
            else:
                self.assertIsNone(roomNameStr,msg="元素定位失败")
        except Exception as msg:
            self.login_page.save_screen_shot("test_addHouse")
            logger.info("异常信息:%s" %msg)
            raise


    def test_delHouse(self):
        self.test_serchHouse(self.editRoomName)
        try:
            buildStr = self.house_del_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]")
            if buildStr is not None:
                self.house_del_page.click_delButton()
                self.house_del_page.click_isYesButton()
                tipsStr = self.house_del_page.find_element(By.XPATH,"/div/div/div/span")
                if tipsStr is not None:
                    self.assertEqual("删除房屋成功",tipsStr.text,msg="删除失败")
                else:
                    self.assertIsNone(tipsStr,msg="元素定位失败")
            else:
                self.assertIsNone(buildStr,msg="元素定位失败")

        except Exception as msg:
            self.login_page.save_screen_shot("test_addHouse")
            logger.info("异常信息:%s" %msg)
            raise

    editRoomName = "102"
    def test_editHouse(self):
        self.test_serchHouse(self.roomName)
        self.house_edit_page.click_editButton()
        try:
            self.house_edit_page.input_roomName(self.editRoomName)
            self.house_edit_page.click_roomId()
            self.house_edit_page.click_chooseRoomId()
            self.house_edit_page.click_saveButton()
            self.test_serchHouse(self.editRoomName)
            roomNameStr = self.house_edit_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]")
            if roomNameStr is not None:
                self.assertEqual(roomNameStr.text,self.editRoomName,msg="断言失败")
            else:
                self.assertIsNone(roomNameStr,msg="元素定位失败")
        except Exception as msg:
            self.login_page.save_screen_shot("test_editHouse")
            logger.info("异常信息:%s" %msg)
            raise

    def test_serchHouse(self,roomName):
        self.house_find_page.refresh()
        self.house_find_page.click_screenButton()
        self.house_find_page.input_roomName(roomName)
        self.house_find_page.click_findButton()

    def tearDown(self):
        logger.info("----END---")
        self.login_page.quit()



if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    suite = unittest.TestSuite()
    tests = [
        TestHouseManage("test_addHouse"),
        TestHouseManage("test_editHouse"),
        TestHouseManage("test_delHouse")
            ]
    suite.addTests(tests)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='智慧社区UI自动化测试报告', description='This is a test report')
        runner.run(suite)
    # e = Email(title='测试报告',
    #                 message='测试报告！',
    #                 receiver='',
    #                 server='smtp.qq.com',
    #                 sender='xx@qq.com',
    #                 password='',
    #                 path=report
    #         )
    # e.send()
