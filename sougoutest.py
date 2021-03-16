from selenium import webdriver
import time

web = webdriver.Firefox()
web.maximize_window()  # 操作 窗口最大化  最小化 minimize_window()
web.get('https://www.sogou.com/')
web.find_element_by_id('query').send_keys('test')
time.sleep(3)
web.find_element_by_id('stb').click()
