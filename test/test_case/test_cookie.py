__author__ = 'apple'
from selenium import webdriver
import unittest
import json
import time

class TestCase(unittest.TestCase):
    # driver = webdriver.Chrome("/Users/apple/PycharmProjects/UIAutoCode/drivers/chromedriver")

    # @classmethod
    # def setUpClass(cls):
    #     driver   = cls.driver
    #     base_url = "https://qzone.qq.com/"
    #     driver.get(base_url)
    """
    获取cookie并保存
    """
    # def test_savaCookies(self):
    #     time.sleep(10)
    #     cookies = self.driver.get_cookies()
    #     print("cookies",cookies)
    #     jsonCookies = json.dumps(cookies)
    #     with open('cookies.txt','w') as f:
    #         f.write(jsonCookies)
    #     time.sleep(3)
    """
    引用cookie跳过登陆
    """
    # def test_login(self):
    #     self.driver.set_page_load_timeout(20)
    #     self.driver.set_script_timeout(20)
    #     fl = open('cookies.txt')
    #     cookies = fl.read()
    #     cookies = json.loads(cookies)
    #     for co in cookies:
    #         self.driver.add_cookie(co)
    #     self.driver.refresh()
    #     time.sleep(5)


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()