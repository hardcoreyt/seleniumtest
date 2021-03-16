import unittest
from selenium import webdriver
import time
import random
from selenium.webdriver.support.select import Select

web = webdriver.Chrome()
web.implicitly_wait(5)
web.maximize_window()
web.get('https://www.runoob.com/try/try.php?filename=tryhtml_select2')

# 切换进入子页面
web.switch_to.frame('iframeResult')

# 定位下拉框原色
car_select_element = web.find_element_by_name('cars')

# 应用select方法选取元素
# 根据索引
Select(car_select_element).select_by_index(3)

# 根据value
Select(car_select_element).select_by_value('saab')

# 根据文本内容
Select(car_select_element).select_by_visible_text('Volvo')

# 返回主页面
web.switch_to.default_content()
web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/form/div/div[1]/button').click()
