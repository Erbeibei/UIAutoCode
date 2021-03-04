__author__ = 'apple'
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class TestCase(unittest.TestCase):
    driver = webdriver.Chrome("/Users/apple/PycharmProjects/UIAutoCode/drivers/chromedriver")

    @classmethod
    def setUpClass(cls):
        driver   = cls.driver
        base_url = "http://api.isccmp.isc.glb.cmos:50002/isccmp/index.html#/login"
        # anfang_url = "http://api.iscportal.isc.glb.cmos:50002/iscportal/index.html#/"
        driver.get(base_url)

    def test_login_success(self):

        #Action
        # self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div/div/form/div[1]/input").send_keys("HA30008901")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div/div/form/div[2]/input").send_keys("1qaz!QAZ")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div/div/form/div[3]/button").click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div/div/form/div[3]/input").send_keys("123456")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div/div/div/button").click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[1]/div/div/span/input").send_keys("CS000400399")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[2]/div/div/span/input").send_keys("1qaz!QAZ")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[3]/div/div/span/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[3]/div/div/span/input").send_keys("123456")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[4]/div/div/span/label/span[1]/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[5]/div/div/span/button").click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]").click()
        # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/div[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]/ul/li[1]").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/input").send_keys("2233")
        time.sleep(3)




    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()