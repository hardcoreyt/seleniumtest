import unittest
from selenium import webdriver
import time
import random


class Contacts(unittest.TestCase):
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.maximize_window()
        self.web.get('http://192.168.2.38/72crm/')
        time.sleep(1)
        self.web.find_element_by_css_selector(
            'div.el-form-item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        ).send_keys('15189805609')
        time.sleep(1)
        self.web.find_element_by_css_selector(
            'div.el-form-item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        ).send_keys('123456')
        time.sleep(1)
        self.web.find_element_by_xpath(
            '/html/body/div/div/div[2]/form/div[4]/div/button'
        ).click()
        time.sleep(1)
        self.web.find_element_by_link_text('客户管理').click()
        time.sleep(1)
        self.web.find_element_by_link_text('联系人').click()
        time.sleep(1)

    # 收尾 用例执行完要做的动作
    def tearDown(self):
        pass
        # self.web.quit()
        # self.web.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[2]/div').click()
        # time.sleep(1)
        # self.web.find_element_by_link_text('联系人').click()
        # time.sleep(3)

    # 新增联系人
    def test_create_contact(self):
        self.web.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[1]/div[3]/button').click()
        time.sleep(1)
        self.web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/form/'
                                       'div[1]/div/div[1]/input').send_keys('聚美客服')
        time.sleep(1)
        # 添加客户
        self.web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[2]'
                                       '/div/span/div[2]/div').click()
        time.sleep(1)
        # 勾选客户
        self.web.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/div/div[2]/div[4]/div[2]'
                                       '/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        time.sleep(1)
        # 添加客户 确定
        self.web.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/button[2]/span').click()
        # 点击保存
        self.web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button[2]/span').click()
        time.sleep(1)
        # 查看是否保存成功
        success_text = self.web.find_element_by_xpath('/html/body/div[2]/p').text
        self.assertTrue(success_text, '未能保存成功')

    # 高级删选
    def test_advancedscreening(self):
        # 打开场景筛选
        self.web.find_element_by_xpath('//*[@id="crm-main-container"]/'
                                       'div/div/div[2]/div[1]/div[1]/div[2]').click()
        time.sleep(1)
        # 点击筛选字段
        self.web.find_element_by_xpath('//*[@id="filter-container"]'
                                       '/div/div/div/div[1]/div/div/input').click()
        time.sleep(1)
        # 选择筛选条件‘姓名’
        self.web.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        # 点击添加框
        self.web.find_element_by_xpath('//*[@id="filter-container"]/div/div/div/div[3]/div/div/input').click()
        time.sleep(1)
        # 选择包含
        self.web.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]/span').click()
        time.sleep(1)
        # 筛选条件
        self.web.find_element_by_xpath('//*[@id="filter-container"]/div'
                                       '/div/div/div[5]/div/input').send_keys('test')
        time.sleep(1)
        # 点击确定
        self.web.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[2]'
                                       '/div[1]/div[1]/div[3]/div/div[3]/div/button[2]/span').click()
        time.sleep(1)
        # 查看筛选结果
        success_text = self.web.find_element_by_xpath('/html/body/div[1]/section/section'
                                                      '/main/div/div/div[2]/div[1]'
                                                      '/div[2]/ul/li/span').text
        time.sleep(1)
        print(success_text)
        self.assertIn('test', success_text, '未能筛选成功')

    # 添加场景
    def test_addscene(self):
        # 点击场景
        self.web.find_element_by_xpath('/html/body/div[1]'
                                       '/section/section/main'
                                       '/div/div/div[2]/div[1]/div[1]/span/div').click()
        time.sleep(1)
        # 点击添加场景
        self.web.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]').click()
        time.sleep(1)
        # 添加场景名称
        self.web.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div[2]/input') \
            .send_keys('快速test1')
        time.sleep(1)
        # 选择筛选字段
        self.web.find_element_by_xpath('//*[@id="scene-filter-container"]'
                                       '/div/div/div/div[1]/div/div/input').click()
        time.sleep(1)
        # 选择姓名字段
        self.web.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        # 选择范围
        self.web.find_element_by_xpath('/html/body/div[3]/div/div[2]'
                                       '/form/div/div/div/div[3]/div/div/input').click()
        time.sleep(1)
        # 选择包含
        self.web.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[3]').click()
        time.sleep(1)
        # 输入筛选条件
        self.web.find_element_by_xpath('/html/body/div[3]/div/div[2]/'
                                       'form/div/div/div/div[5]/div/input').send_keys('test')
        time.sleep(1)
        # 点击确定
        self.web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/button[2]/span').click()
        time.sleep(1)
