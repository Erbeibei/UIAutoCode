
import os, time, unittest
from selenium import webdriver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '6.0'  # 设备系统版本
desired_caps['deviceName'] = 'BYFNW17307012472'  # 设备名称
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"

# desired_caps['app'] = PATH(r"E:\tests\GuoYuB2B_2.1.apk")
desired_caps['appPackage'] = 'com.zhongyewx'
desired_caps['appActivity'] = '.activity.ZYWelcomeActivity'
desired_caps['appWaitActivity'] = '.activity.ZYWelcomeActivity'


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(5)

driver.find_element_by_id("com.zhongyewx:id/edit_user").send_keys("xx")
driver.find_element_by_id("com.zhongyewx:id/edit_password").send_keys("xx")
driver.find_element_by_id("com.zhongyewx:id/login_button").click()

time.sleep(5)

#获取参数appPackage/appActivity dos命令：adb shell dumpsys activity activities >C:\Users\Administrator\Desktop\aa.txt
#com.zhongyewx/.activity.ZYWelcomeActivity