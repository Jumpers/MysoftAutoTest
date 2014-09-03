 
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# u'实例化
browser = webdriver.Ie()

# u'不一样的等待 
browser.implicitly_wait(30)
 
# u'打开网页 
browser.get("http://www.baidu.com")

# u'输入内容 
browser.find_element_by_id("kw").send_keys("selenium")

# u'点击搜索按钮
browser.find_element_by_id("su").click()

# u'获取标题 
print 'Page title is:',browser.title

# u'等待  
time.sleep(3)

# u'关闭 
browser.quit()
