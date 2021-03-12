import unittest
import time
import zipfile
import shutil
import os
from utils.config import REPORT_PATH, LOG_PATH, IMGS_PATH, LOGS_PATH, RESULT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from test.case.community_case.test_admin_manage import TestAdminManage
from test.case.community_case.test_build_manage import TestBuildManage
from test.case.community_case.test_house_manage import TestHouseManage


class RunCase(unittest.TestCase):

    def test_text(self):
        self.test_text()

    def combine_file(self):
        if os.path.exists(IMGS_PATH):
            shutil.rmtree(IMGS_PATH)
        if os.path.exists(LOGS_PATH):
            shutil.rmtree(LOGS_PATH)
        os.mkdir(LOGS_PATH)

    def zipDir(dirpath, outFullName):
        '''
        压缩指定文件夹
        :param dirpath: 目标文件夹路径
        :param outFullName:  压缩文件保存路径+XXXX.zip
        :return: 无
        '''
        zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标和路径，只对目标文件夹下边的文件及文件夹进行压缩（包括父文件夹本身）
            this_path = os.path.abspath('.')
            fpath = path.replace(this_path, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

    def clear_text(self):
        file_path = LOG_PATH + '/test.log'
        print(file_path)
        with open(file_path, "rb+") as f:
            f.read()
            f.seek(0)
            f.truncate()


if __name__ == '__main__':
            RunCase.clear_text(1)
            RunCase.combine_file(1)
            report = REPORT_PATH + '/report.html'
            suite = unittest.TestSuite()
            tests = [
                # TestAdminManage("test_addAdmin"),
                # TestAdminManage("test_editAdmin"),
                # TestAdminManage("test_delAdmin"),
                TestBuildManage("test_addBuild"),
                TestBuildManage("test_editBuild"),
                # TestBuildManage("test_delBuild"),
                TestHouseManage("test_addHouse"),
                TestHouseManage("test_editHouse")
                # TestHouseManage("test_delHouse")
            ]
            suite.addTests(tests)
            with open(report, 'wb') as f:
                runner = HTMLTestRunner(stream=f, verbosity=2, title='Website test report',
                                        description='一句话描述此报告')
                runner.run(suite)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            out_dir = RESULT_PATH + '/report%s.zip' %tm
            RunCase.zipDir(REPORT_PATH, out_dir)
            # e = Email(title='Website test report',
            #                 message='测试报告！',
            #                 receiver='',
            #                 server='smtp.qq.com',
            #                 sender='xx@qq.com',
            #                 password='',
            #                 path=out_dir
            #         )
            # e.send()