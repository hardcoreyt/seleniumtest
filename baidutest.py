from selenium import webdriver
import time

# 打开浏览器
web = webdriver.Firefox()
web.get('https://baidu.com')

# 对元素进行定位操作
web.find_element_by_id('kw').send_keys('南京美食')
time.sleep(3)
web.find_element_by_id('su').click()
# time.sleep(3)
# web.quit()  # 浏览器退出
# close 当前窗口关闭
