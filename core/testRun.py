import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
#写测试报告的开源代码
from bases.html_test_runner import HtmlTestRunner
#unittest:包含：TestCase/TestSuite/testrunner 三个类
#TestSuite（测试套件）中加入若干个TestCase，然后用testRunner去运行
#testrunner：TextTestRunner、HtmlTestRunner
class CmuopTestCases():
    def run_tests(self):
        # 创建一个测试套件
        test_suite = unittest.TestSuite()
        # 在测试套件中添加需要运行的测试用例
        # 一个测试套件中可以添加多个测试用例
        # test_suite.addTest(loginCases("test_login_batch"))
        # test_suite.addTest(ProductCases("test_productAdd_batch"))
        # 创建一个文本测试运行器，运行刚刚创建的测试套件
        #text_test_runner = unittest.TextTestRunner()
        #text_test_runner.run(test_suite)

        reportPath = os.path.join(BASE_DIR, "report", "test_result.html")
        report = open(reportPath, "wb")

        html_test_runner = HtmlTestRunner(report,
                title="招商随行PC客户端功能测试报告",
                description="测试详细结果")

        html_test_runner.run(test_suite)
        report.close()
if __name__ == "__main__":
    test_runner = CmuopTestCases()
    test_runner.run_tests()
    # send_email("XXX@51testing.com")