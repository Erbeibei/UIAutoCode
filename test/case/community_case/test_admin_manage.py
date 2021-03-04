import unittest
from test.page.loginPage.login_page import LoginPage
from test.page.adminPage.admin_add_page import AdminAddPage
from test.page.adminPage.admin_edit_page import AdminEditPage
from test.page.adminPage.admin_del_page import AdminDelPage
from utils.config import Config, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from selenium.webdriver.common.by import By


class TestAdminManage(unittest.TestCase):
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
        self.admin_add_page = AdminAddPage(self.login_page)
        self.admin_edit__page = AdminEditPage(self.login_page)
        self.admin_del_page = AdminDelPage(self.login_page)
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

        except Exception as msg:
            self.login_page.save_screen_shot("test_login")
            logger.info("异常信息:%s" %msg)
            raise

    def tearDown(self):
        logger.info("----END---")
        self.login_page.quit()

    adminName = "黄彬彬"
    adminTel = "17537135213"
    adminIdCard = "410102199203020032"
    """
    @添加管理员
    description:正常添加
    """
    @unittest.skipUnless(True, "添加管理员")
    def test_addAdmin(self):
        try:
            self.admin_add_page.click_addAdminAcctButton()
            self.admin_add_page.input_adminName(self.adminName)
            self.admin_add_page.input_adminTel(self.adminTel)
            self.admin_add_page.input_adminIdCard(self.adminIdCard)
            self.admin_add_page.click_adminSavaButton()
            self.admin_add_page.wait(3)
            self.admin_add_page.refresh()
            self.admin_add_page.wait(3)
            c = self.admin_add_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[2]").text
            logger.info(c)
            self.assertEqual(c,self.adminName)
            self.admin_add_page.wait(3)
        except Exception as msg:
            self.admin_add_page.save_screen_shot("test_addAdmin")
            logger.info("异常信息:%s" %msg)
            raise

    adminNameEdit = "张晓"
    adminTelEdit = "18137793748"
    adminIdCardEdit = "412822199004057639"
    @unittest.skipUnless(True, "编辑管理员")
    def test_editAdmin(self):
        try:
            self.admin_edit__page.click_editAdminAcctButton()
            self.admin_edit__page.input_adminName(self.adminNameEdit)
            self.admin_edit__page.input_adminTel(self.adminTelEdit)
            self.admin_edit__page.input_adminIdCard(self.adminIdCardEdit)
            self.admin_edit__page.click_adminSavaButton()
            self.admin_edit__page.refresh()
            self.admin_edit__page.wait(3)
            c = self.admin_edit__page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[2]").text
            logger.info(c)
            self.assertEqual(c,self.adminNameEdit)
            self.admin_edit__page.wait(3)
        except Exception as msg:
            self.admin_edit__page.save_screen_shot("test_editAdmin")
            logger.info("异常信息:%s" %msg)
            raise


    @unittest.skipUnless(True, "删除管理员")
    def test_delAdmin(self):
         try:
             c = self.admin_del_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]").text
             logger.info(c)
             self.admin_del_page.click_delButton()
             self.admin_del_page.wait(3)
             self.admin_del_page.click_isYesButton()
             self.admin_del_page.wait(3)
             self.admin_del_page.refresh()
             self.admin_del_page.wait(3)
             b = self.admin_del_page.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]")
             if b is not None:
                logger.info(b.text)
                self.assertNotEqual(c,b.text,msg="断言失败，删除失败")
             else:
                return
             self.admin_del_page.wait(3)
         except Exception as msg:
             self.admin_del_page.save_screen_shot("test_delAdmin")
             logger.info("异常信息:%s" %msg)
             raise



if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    suite = unittest.TestSuite()
    tests = [
        TestAdminManage("test_addAdmin"),
        TestAdminManage("test_editAdmin"),
        TestAdminManage("test_delAdmin")
            ]
    suite.addTests(tests)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='Website test reports', description='测试报告简介')
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
