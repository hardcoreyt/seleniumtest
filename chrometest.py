from selenium import webdriver
import time

web = webdriver.Chrome()
web.maximize_window()
web.get('https://baidu.com')

# 对元素进行定位操作
web.find_element_by_link_text('新闻').click()
time.sleep(3)
hands = web.window_handles  # 获取窗口句柄
print(hands)
web.switch_to.window(hands[1])  # 切换到第二个窗口
web.find_element_by_id('ww').send_keys('军队')
time.sleep(1)
web.find_element_by_id('s_btn_wr').click()
