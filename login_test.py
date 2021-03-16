import unittest
from selenium import webdriver
import time
# F8 或者 ctrl+\  冻结页面

# 导入显示等待3个包
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from csvfile import getCsvData

# 使用ddt模块
from ddt import ddt, data, unpack


@ddt
# 类
class Login(unittest.TestCase):  # 继承 TestCase里一些方法
    # 初始化
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.maximize_window()
        self.web.get('http://192.168.2.38/72crm/')
        time.sleep(1)

    def tearDown(self):
        self.web.quit()
        # 收尾 用例执行完要做的动作

    def login(self, username, passwd):
        self.web.find_element_by_css_selector(
            'div.el-form-item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        ).send_keys(username)
        time.sleep(1)
        self.web.find_element_by_css_selector(
            'div.el-form-item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        ).send_keys(passwd)
        time.sleep(1)
        self.web.find_element_by_xpath(
            '/html/body/div/div/div[2]/form/div[4]/div/button'
        ).click()
        time.sleep(1)

    # 获取数据,解包，按行分配
    @data(*getCsvData('./username.csv'))
    @unpack
    # 测试用例的方法必须以test开头
    def test_login_success(self, username, passwd):
        self.login(username, passwd)
        success_text = self.web.find_element_by_xpath('/html/body/div/section/header/div/div/div/a[2]/div').text
        self.assertEqual('客户管理', success_text, '用户登录失败，用例执行失败')
        # 断言

    def test_login_incorect(self):
        self.login('15189805608', '123456')
        # 需要冻结页面获取弹窗字段的xpath
        # 相同的字符串却不相等
        # fail_text = self.web.find_element_by_xpath('/html/body/div[2]/p').text
        # self.assertIn('账号不存在', str.strip(fail_text), '登录失败')
        # 断言
        # 看是否能找到登录成功时的元素，找不到返回false
        success_element = self.web.find_element_by_xpath('/html/body/div/section/header/div/div/div/a[2]/div')
        self.assertTrue(success_element, '登录失败，用例执行失败')

        error_info = WebDriverWait(self.web, 5, 0.2).until \
            (EC.presence_of_element_located(By.XPATH, '/html/body/div/section/header/div/div/div/a[2]/div'))
        self.assertTrue('账户不存在', error_info, '登录失败，用例执行失败')

# if __name__ == '__mian__':
#     unittest.main(verbosity=2)
