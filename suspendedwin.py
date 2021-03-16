# 鼠标停留弹出的悬浮框内容进行操作
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

web = webdriver.Chrome()
web.implicitly_wait(3)
web.maximize_window()
web.get('https://www.baidu.com')
# 鼠标停留在上面
el = web.find_element_by_name('tj_briicon')
ActionChains(web).move_to_element(el).perform()
time.sleep(2)
# 鼠标点击
web.find_element_by_name('tj_img').click()
