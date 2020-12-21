import unittest
from test.page.zy_school.home_page import HomePage
from utils.config import Config, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
import time


class TestLogin(unittest.TestCase):
    zhongye_net = Config().get('zhongye_net')
    username = Config().get('username')
    password = Config().get('password')

    def setUp(self):
        logger.info("--------------------------------------------------start-------------------------------------------------------------")
        self.home_page = HomePage(browser_type='chrome').get(self.zhongye_net, maximize_window=True)

    def tearDown(self):
        logger.info("--------------------------------------------------END-------------------------------------------------------------")
        self.home_page.quit()

    """
    @用例0
    description:正常登录，登录成功并断言标题
    """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_login(self):
        try:
            self.home_page.input_username(self.username)
            self.home_page.input_password(self.password)
            self.home_page.loginBtn_click()
            self.home_page.wait(3)
            #断言
            self.assertEqual(self.home_page.title, "中业用户中心-我的课程-1", msg="登录成功标题断言失败")
            #截图
            self.home_page.save_screen_shot('success_home_page')
        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_login")
            logger.info("异常信息:%s" %msg)
            raise

    """
    @用例1
    description:用户账户正常，密码为空，弹窗提示“用户名或密码错误!”
    """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_login2(self):
        try:
            self.home_page.input_username("17516728152")
            self.home_page.input_password("12")
            self.home_page.loginBtn_click()
            self.home_page.wait(3)
            #断言信息块
            al = self.home_page.switch_to_alert()
            self.result = al.text
            self.exp = "用户名或密码错误!"
            logger.info("弹窗文本：%s", self.result)
            self.assertEqual(self.result, self.exp, msg='登录验证提示信息断言失败')
            # 断言成功后截图
            al.accept()
            self.home_page.save_screen_shot('success_home_page')
            self.home_page.wait(3)
        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_login2")
            logger.info("异常信息:%s" %msg)
            raise

    """
    @用例2
    description:用户账户不存在，密码随意录入，弹窗提示“用户名不存在!”
    """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_login3(self):
        try:
            self.home_page.input_username("123nn@@789")
            self.home_page.input_password("12312312")
            self.home_page.loginBtn_click()
            self.home_page.wait(3)
            # 断言信息块
            al = self.home_page.switch_to_alert()
            self.result = al.text
            self.exp = "用户名不存在!"
            logger.info("弹窗文本：%s", self.result)
            self.assertEqual(self.exp, self.result, msg='登录验证提示信息断言失败')
            # 断言成功后截图
            al.accept()
            self.home_page.save_screen_shot('success_home_page')
            self.home_page.wait(3)
        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_login3")
            logger.info("异常信息:%s" % msg)
            raise


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()
    tests = [
        TestLogin("test_login"),
        TestLogin("test_login2"),
        TestLogin("test_login3")
            ]
    suite.addTests(tests)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='Website test report', description='测试报告简介')
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
