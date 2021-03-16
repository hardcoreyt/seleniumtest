import unittest
from selenium import webdriver
import random
from selenium.webdriver.support.select import Select

web = webdriver.Chrome()
web.implicitly_wait(3)  # 对所有元素隐式等待
web.maximize_window()
web.get('https://www.runoob.com/try/try.php?filename=tryjs_alert')

# 切换进入子页面
web.switch_to.frame('iframeResult')

web.find_element_by_xpath('/html/body/input').click()

# 定位到警告框
web.switch_to.alert.accept()  # 确定
# web.switch_to.alert.dismiss()  # 取消

web.switch_to.default_content()  # 返回主界面
