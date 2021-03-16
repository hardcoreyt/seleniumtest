from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

web = webdriver.Chrome()
web.implicitly_wait(3)
web.maximize_window()
web.get('http://192.168.2.38/72crm/#/login')
web.find_element_by_name('username').send_keys('15189805609')

web.find_element_by_name('password').send_keys('123456')

web.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()

web.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[2]/div').click()

web.find_element_by_link_text('联系人').click()

web.find_element_by_link_text('线索').click()

web.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[1]/div[3]/button/span').click()

web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/input') \
    .send_keys('test3')

web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button[2]/span').click()
# 使用keys对某个元素进行剪切
web.find_element_by_xpath('/html/body/div/section/section/main/div/div/div[1]/div[2]/input').send_keys(Keys.CONTROL,
                                                                                                       'x')
# web.refresh()  # 刷新
# web.back()    # 后退
# web.forward()   # 前进

# 使用ActionChains进行单独刷新
