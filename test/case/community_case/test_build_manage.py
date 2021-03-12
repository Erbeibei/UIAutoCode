import unittest
from test.page.loginPage.login_page import LoginPage
from test.page.buildPage.build_add_page import BuildAddPage
from test.page.buildPage.build_find_page import BuildFindPage
from test.page.buildPage.build_edit_page import BuildEditPage
from test.page.buildPage.build_del_page import BuildDelPage
from utils.config import Config, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from selenium.webdriver.common.by import By


class TestBuildManage(unittest.TestCase):
    ZHSQ_URL = Config().get('ZHSQ_URL')
    userAcct = Config().get('userAcct')
    userPwd = Config().get('userPwd')
    smsCode = Config().get('smsCode')
    """
    @前置处理器
    description:登陆
    """
    def setUp(self):
        logger.info("----start---")
        self.login_page = LoginPage(browser_type='chrome').get(self.ZHSQ_URL, maximize_window=True)
        self.build_add_page = BuildAddPage(self.login_page)
        self.build_find_page = BuildFindPage(self.login_page)
        self.build_edit_page = BuildEditPage(self.login_page)
        self.build_del_page = BuildDelPage(self.login_page)
        try:
            #遗留问题，先录入账号再勾选协议找不到元素
            #原因可能是因为倒计时，导致页面有动态元素
            self.login_page.click_checkbox()
            self.login_page.click_closeAlert()
            self.login_page.input_userAcct(self.userAcct)
            self.login_page.input_userPwd(self.userPwd)
            self.login_page.click_smsCodeButton()
            self.login_page.input_smsCode(self.smsCode)
            self.login_page.click_loginButton()
            self.login_page.wait(3)
            self.build_add_page.click_chooseModTree()
            self.build_add_page.click_chooseBuildManageTree()


        except Exception as msg:
            self.login_page.save_screen_shot("test_login")
            logger.info("异常信息:%s" %msg)
            raise

    def tearDown(self):
        logger.info("----END---")
        self.login_page.quit()


    """
    @添加楼栋
    description:正常添加
    """
    buildingName = "天地社区"
    @unittest.skipUnless(True, "添加楼栋")
    def test_addBuild(self):
        try:
            #1line
            self.build_add_page.click_addButton()
            self.build_add_page.wait()

            self.build_add_page.input_buildingName(self.buildingName)
            self.build_add_page.input_buildingNo(2)
            self.build_add_page.input_unitNo(1)
            self.build_add_page.input_floorCount(8)
            self.build_add_page.input_roomCount(2)
            #2line
            self.build_add_page.click_addLine()
            self.build_add_page.input_unitNo2(2)
            self.build_add_page.input_floorCount2(8)
            self.build_add_page.input_roomCount2(2)
            #操作保存
            self.build_add_page.click_saveButton()
            self.build_add_page.wait()
            #刷新
            self.build_add_page.refresh()
            self.build_add_page.wait()

            buildingNameStr = self.build_add_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]")
            if buildingNameStr is not None:
                self.assertEqual(self.buildingName, buildingNameStr.text,msg="楼栋添加失败")
            else:
                self.assertIsNone(buildingNameStr,msg="元素定位失败")
        except Exception as msg:
            self.admin_add_page.save_screen_shot("test_addBuild")
            logger.info("异常信息:%s" %msg)
            raise

    #编辑楼栋
    buildingNameEdit = "金城社区"
    floorCountEdit = 10
    def test_editBuild(self):
        TestBuildManage.test_findBuild(self)
        try:
            buildingNameStr = self.build_edit_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[3]")
            if buildingNameStr is not None:
                self.assertEqual(self.buildingName,buildingNameStr.text,msg="查询成功")
                self.build_edit_page.click_editButton()
                self.build_edit_page.input_buildingName(self.buildingNameEdit)
                self.build_edit_page.input_floorCount(self.floorCountEdit)
                self.build_edit_page.click_saveButton()
                self.build_edit_page.wait()
                #get value be used for assert
                self.build_find_page.input_buildingName(self.buildingNameEdit)
                self.build_find_page.click_submitButton()
                buildingNameStr = self.build_edit_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[3]")

                self.build_edit_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span").click()
                floorCountStr = self.build_edit_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]")

                if buildingNameStr is not None:
                    self.assertEqual(str(self.buildingNameEdit),buildingNameStr.text,msg="断言失败")
                else:
                    self.assertIsNone(buildingNameStr,msg="元素定位失败")
                if floorCountStr is not None:
                    self.assertEqual(str(self.floorCountEdit),floorCountStr.text,msg="断言失败")
                else:
                    self.assertIsNone(floorCountStr,msg="元素定位失败")
            else:
                self.assertIsNone(buildingNameStr,msg="元素定位失败")
        except Exception as msg:
            self.build_edit_page.save_screen_shot("test_findBuild")
            logger.info("异常信息:%s" %msg)
            raise


     #删除楼栋
    def test_delBuild(self):
        try:
          self.build_del_page.click_delButton()
          self.build_del_page.click_isYesButton()
          buildingNameStr = self.build_del_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[3]")
          if buildingNameStr is not None:
            self.assertNotEqual(self.floorCountEdit,buildingNameStr.text,msg="断言失败,删除失败")
          else:
            # self.assertIsNone(buildingNameStr,msg="元素定位失败,已删除")
            return
        except Exception as msg:
            self.build_edit_page.save_screen_shot("test_findBuild")
            logger.info("异常信息:%s" %msg)
            raise

    #查询
    def test_findBuild(self):
        try:
            self.build_find_page.click_findButton()
            self.build_find_page.input_buildingName(self.buildingName)
            self.build_find_page.click_submitButton()
            self.build_find_page.wait()
        except Exception as msg:
            self.build_edit_page.save_screen_shot("test_findBuild")
            logger.info("异常信息:%s" %msg)
            raise

if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    suite = unittest.TestSuite()
    tests = [
        TestBuildManage("test_addBuild"),
        TestBuildManage("test_editBuild"),
        TestBuildManage("test_delBuild")
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
