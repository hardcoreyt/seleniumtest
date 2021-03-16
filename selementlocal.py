import time

from selenium import webdriver

web = webdriver.Chrome()
web.maximize_window()
web.get('https://www.baidu.com')
web.find_element_by_xpath('//*[@id="kw"]').send_keys('xpath')
time.sleep(3)
web.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)
web.find_element_by_name('wd').send_keys('test')
time.sleep(3)
web.find_element_by_id('su').click()
web.find_element_by_class_name('s_ipt').send_keys('test')
