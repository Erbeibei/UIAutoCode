import unittest
from test.page.loginPage.login_page import LoginPage
from test.page.loginPage.menu_page import MenuPage
from test.page.ownerPage.owner_add_page import OwnerAddPage
from test.page.ownerPage.owner_find_page import OwnerFindPage
from test.page.ownerPage.owner_edit_page import OwnerEditPage
from test.page.ownerPage.owner_del_page import OwnerDelPage
from utils.config import Config, REPORT_PATH,SOURCEIMG_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger
from selenium.webdriver.common.by import By
import time


class TestOwnerManage(unittest.TestCase):
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
        self.owner_add_page = OwnerAddPage(self.login_page)
        self.owner_find_page = OwnerFindPage(self.login_page)
        self.owner_edit_page = OwnerEditPage(self.login_page)
        self.owner_del_page = OwnerDelPage(self.login_page)
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
            self.menu_page.click_ownerManage()
            self.menu_page.wait()

        except Exception as msg:
            self.login_page.save_screen_shot("test_login")
            logger.info("异常信息:%s" %msg)
            raise

    def tearDown(self):
        logger.info("----END---")
        self.login_page.quit()

    customName = "卢志恒"
    @unittest.skipUnless(True, "新增业主")
    def test_addOwner(self):
         try:
            self.owner_add_page.click_addButton()
            self.owner_add_page.click_belongToBuilding()
            self.owner_add_page.click_buildListBox()
            self.owner_add_page.click_belongTounit()
            self.owner_add_page.click_unitListBox()
            self.owner_add_page.click_belongToFloor()
            self.owner_add_page.click_floorListBox()
            self.owner_add_page.click_roomId()
            self.owner_add_page.click_chooseRoomId()
            # ##业主
            self.owner_add_page.input_customName(self.customName)
            self.owner_add_page.click_customType()
            self.owner_add_page.click_chooseCustomType()
            self.owner_add_page.input_customTel("15038330928")

            #滚动条滚动到某元素
            # target = self.owner_add_page.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
            # self.owner_add_page.execute("arguments[0].scrollIntoView();", target)

            js = "document.getElementById(\"customs.0.prsnImgUrl\").style.display='block';"
            # 调用js脚本
            self.owner_add_page.execute(js)
            self.owner_add_page.input_imgFile(SOURCEIMG_PATH + "/13213156600.jpg")

            # # ##业主成员
            # self.owner_add_page.click_addMemberButton()
            # self.owner_add_page.input_memberName("李杨")
            # self.owner_add_page.click_memberType()
            # self.owner_add_page.click_chooseMemberType()
            # self.owner_add_page.input_memberTel("15137161725")
            #
            # js1 = "document.getElementById(\"customs.1.prsnImgUrl\").style.display='block';"
            # self.owner_add_page.execute(js1)
            # self.owner_add_page.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[7]/div/div[2]/div/span/span/div/span/input").send_keys(SOURCEIMG_PATH + "/13213156601.jpeg")
            # ##操作
            self.owner_add_page.click_saveButton()
            msgStr = self.owner_add_page.find_element(By.XPATH,"/html/body/div[2]/span/div/div/div/span")
            if msgStr is not None:
                self.assertEqual(msgStr.text,"添加成功",msg="添加失败")
            else:
                self.assertIsNone(msgStr,msg="元素定位失败")
            self.owner_add_page.wait()
            self.owner_add_page.refresh()
         except Exception as msg:
             self.owner_add_page.save_screen_shot("test_addOwner")
             logger.info("异常信息:%s" %msg)
             raise


    ## 业主成员
    memberName = "李杨"
    def test_addMember(self):
        try:
            self.owner_add_page.click_addButton()
            self.owner_add_page.click_belongToBuilding()
            self.owner_add_page.click_buildListBox()
            self.owner_add_page.click_belongTounit()
            self.owner_add_page.click_unitListBox()
            self.owner_add_page.click_belongToFloor()
            self.owner_add_page.click_floorListBox()
            self.owner_add_page.click_roomId()
            self.owner_add_page.click_chooseRoomId()

            # ##业主成员
            self.owner_add_page.click_addMemberButton()
            self.owner_add_page.input_memberName(self.memberName)
            self.owner_add_page.click_memberType()
            self.owner_add_page.click_chooseMemberType()
            self.owner_add_page.input_memberTel("15137161725")

            js1 = "document.getElementById(\"customs.0.prsnImgUrl\").style.display='block';"
            self.owner_add_page.execute(js1)
            self.owner_add_page.find_element(By.ID,"customs.0.prsnImgUrl").send_keys(SOURCEIMG_PATH + "/13213156601.jpeg")
            ##操作
            self.owner_add_page.click_saveButton()
            msgStr = self.owner_add_page.find_element(By.XPATH,"/html/body/div[2]/span/div/div/div/span")
            if msgStr is not None:
                self.assertEqual(msgStr.text,"添加成功",msg="添加失败")
            else:
                self.assertIsNone(msgStr,msg="元素定位失败")
            self.owner_add_page.wait()
            self.owner_add_page.refresh()
        except Exception as msg:
             self.owner_add_page.save_screen_shot("test_addMember")
             logger.info("异常信息:%s" %msg)
             raise

    editCustomName = customName + "edit"
    editMemberName = memberName + "edit"
    ##编辑 查询并编辑
    def test_edit(self,oldName,newName):
        self.owner_edit_page.refresh()
        TestOwnerManage.test_findOwner(self,oldName)
        try:
            self.owner_edit_page.click_editButton()
            self.owner_edit_page.input_ownerName(newName)
            self.owner_edit_page.click_saveButton()
            msgStr = self.owner_edit_page.find_element(By.XPATH,"/html/body/div[2]/span/div/div/div/span")
            if msgStr is not None:
                self.assertEqual(msgStr.text,"操作成功",msg="添加失败")
            else:
                self.assertIsNone(msgStr,msg="元素定位失败")
            self.owner_edit_page.wait()
            self.owner_edit_page.refresh()
            TestOwnerManage.test_findOwner(self,newName)
            nameStr = self.owner_edit_page.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]")
            if nameStr is not None:
                self.assertEqual(nameStr.text,newName,msg="数据错误")
            else:
                self.assertIsNone(nameStr.text,msg="查询数据列表为空")
            self.owner_edit_page.refresh()
        except Exception as msg:
            self.owner_add_page.save_screen_shot("test_editMember")
            logger.info("异常信息:%s" %msg)
            raise

    def test_editOwner(self):
        TestOwnerManage.test_edit(self,self.customName,self.editCustomName)
        TestOwnerManage.test_edit(self,self.memberName,self.editMemberName)

    # ##删除-根据name查找并删除
    def test_del(self, name):
        self.owner_del_page.refresh()
        TestOwnerManage.test_findOwner(self,name)
        try:
            self.owner_del_page.click_delButton()
            self.owner_del_page.click_isYesButton()
            msgStr = self.owner_del_page.find_element(By.XPATH,"/html/body/div[2]/span/div/div/div/span")
            if msgStr is not None:
                self.assertEqual(msgStr.text,"注销业主成功",msg="注销业主失败")
            else:
                self.assertIsNone(msgStr.text,msg="元素定位失败")
        except Exception as msg:
            self.owner_add_page.save_screen_shot("test_delOwner")
            logger.info("异常信息:%s" %msg)
            raise

    def test_delOwner(self):
        TestOwnerManage.test_del(self,self.editCustomName)
        TestOwnerManage.test_del(self,self.editMemberName)

    def test_findOwner(self,prsnName):
        try:
            self.owner_find_page.click_searchButton()
            self.owner_find_page.input_prsnName(prsnName)
            self.owner_find_page.click_submitButton()
        except Exception as msg:
            self.owner_add_page.save_screen_shot("test_findOwner")
            logger.info("异常信息:%s" %msg)
            raise

if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    suite = unittest.TestSuite()
    tests = [
       # TestOwnerManage("test_addOwner"),
       # TestOwnerManage("test_addMember"),
       # TestOwnerManage("test_editOwner"),
       TestOwnerManage("test_delOwner")
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
