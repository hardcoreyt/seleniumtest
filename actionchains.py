from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# web.refresh()  # 刷新
# web.back()    # 后退
# web.forward()   # 前进

web = webdriver.Chrome()
web.maximize_window()
web.get('https://baidu.com')
time.sleep(2)
