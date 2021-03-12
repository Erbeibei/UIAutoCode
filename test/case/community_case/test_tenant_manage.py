import unittest
from test.page.loginPage.login_page import LoginPage
from test.page.loginPage.menu_page import MenuPage

from utils.config import Config, REPORT_PATH,SOURCEIMG_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from selenium.webdriver.common.by import By
import time


class TestTenantManage(unittest.TestCase):
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
        self.menu_page = MenuPage(self.login_page)

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
            self.menu_page.click_householdManage()
            self.menu_page.click_tenantManage()
            self.menu_page.wait()

        except Exception as msg:
            self.login_page.save_screen_shot("test_login")
            logger.info("异常信息:%s" %msg)
            raise

    def tearDown(self):
        logger.info("----END---")
        self.login_page.quit()



if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    suite = unittest.TestSuite()
    tests = [
       TestTenantManage("test_delOwner")
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
