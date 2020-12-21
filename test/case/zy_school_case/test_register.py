import unittest
from test.page.zy_school.home_page import HomePage
from test.page.zy_school.register_page import RegisterPage
from utils.config import Config, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from utils.PhoneNOGenerator import PhoneNOGenerator
from selenium.webdriver.support import expected_conditions as EC


class TestRegister(unittest.TestCase):
    zhongye_net = Config().get('zhongye_net')
    #随机手机号
    telphone = PhoneNOGenerator.phoneNORandomGenerator(1)

    def setUp(self):
        logger.info("--------------------------------------------------start------------------------------------------")
        self.home_page = HomePage(browser_type='chrome').get(self.zhongye_net, maximize_window=True)
        self.register_page = RegisterPage(self.home_page)

    def tearDown(self):
        logger.info("--------------------------------------------------END--------------------------------------------")
        self.home_page.quit()

    """
    @注册用例
    description:点击去注册页面并录入信息成功注册
    """
    @unittest.skipUnless(False, "False用例则跳过")
    def test_register(self):
        try:
            self.home_page.registerBtn_click()
            self.home_page.switch_to_window()
            self.register_page.input_telphone(self.telphone)#此处应添加对已存在的手机号进行重新录入 √已解决
            self.register_page.input_password("123456")
            self.register_page.input_confirmPassword("123456")
            self.register_page.classList_click()
            self.register_page.selectClass_click()
            self.register_page.submitBtn_click()
            self.home_page.wait(3)
            if EC.alert_is_present: #判断是否有弹窗，有弹窗证明随机的手机号已存在，关闭窗口重新运行
                al = self.register_page.switch_to_alert()
                self.alertMessage = al.text
                logger.info("发生弹窗，弹窗文本：%s ，即将关闭本窗口重新开始运行！", self.alertMessage)
                al.accept()
                self.register_page.quit()
                unittest.TextTestRunner().run(TestRegister("test_register"))
            else:
                #断言
                self.assertEqual(self.home_page.title, "中业用户中心-我的课程-1", msg="登录成功标题断言失败")
                logger.info("断言通过，注册成功了诶，恭喜恭喜！")
                #截图
                self.home_page.save_screen_shot('success_home_page')
        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_register")
            logger.info("注册用例执行失败-异常信息:%s" %msg)
            raise


    """
    @注册用例
    description:注册信息提交校验
    进入注册页面直接点击提交按钮，将弹出提示窗“手机号不能为空！”
    """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_register2(self):
        try:
            self.home_page.registerBtn_click()
            self.home_page.switch_to_window()

            self.register_page.submitBtn_click()
            al = self.register_page.switch_to_alert()
            self.alertMessage = al.text
            logger.info("发生弹窗，弹窗文本：%s ", self.alertMessage)
            self.assertEqual("手机号不能为空！", self.alertMessage, msg="注册校验信息失败")
            al.accept()

        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_register2")
            logger.info("注册用例执行失败-异常信息:%s" %msg)
            raise

    """
     @注册用例
     description:注册信息提交校验
     进入注册页面录入正确手机号点击提交按钮，将弹出提示窗“请输入密码！”
     """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_register3(self):
        try:
            self.home_page.registerBtn_click()
            self.home_page.switch_to_window()

            self.register_page.input_telphone(self.telphone)
            self.register_page.submitBtn_click()
            al = self.register_page.switch_to_alert()
            self.alertMessage = al.text
            logger.info("发生弹窗，弹窗文本：%s ", self.alertMessage)
            self.assertEqual("请输入密码！", self.alertMessage, msg="注册校验信息失败")
            al.accept()

        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_register3")
            logger.info("注册用例执行失败-异常信息:%s" % msg)
            raise

    """
     @注册用例
     description:注册信息提交校验
     进入注册页面录入错误格式手机号点击提交按钮，将弹出提示窗“手机号码格式不正确！”
     ps：手机号不满足11位长度纯数字为格式错误
     """
    @unittest.skipUnless(True, "False用例则跳过")
    def test_register4(self):
        try:
            self.home_page.registerBtn_click()
            self.home_page.switch_to_window()

            self.register_page.input_telphone("00000000000000000")
            self.register_page.submitBtn_click()
            al = self.register_page.switch_to_alert()
            self.alertMessage = al.text
            logger.info("发生弹窗，弹窗文本：%s ", self.alertMessage)
            self.assertEqual("手机号码格式不正确！", self.alertMessage, msg="注册校验信息失败")
            al.accept()

        except Exception as msg:
            self.home_page.save_screen_shot("Fail_test_register3")
            logger.info("注册用例执行失败-异常信息:%s" % msg)
            raise

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()
    tests = [
        TestRegister("test_register"),
        TestRegister("test_register2"),
        TestRegister("test_register3"),
        TestRegister("test_register4")
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
