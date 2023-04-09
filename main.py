from selenium import webdriver
import random
from time import sleep
# 选择Chrome浏览器
driver = webdriver.Chrome()
# 这是我学校的打卡网页，需自行修改
driver.get("https://blog.csdn.net/xwj2633673783/article/details/119932573")

# 这两步把操作界面切换到新打开的浏览器页面
now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)

# 清除输入框内容、输入账号密码，需自行修改
driver.find_element_by_id("username").clear()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("username").send_keys("*********")	# 账号
driver.find_element_by_id("password").send_keys("***********")	# 密码
# 延时2秒
sleep(2)
# 如果过了5秒，页面还没加载完，发出error警告
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)
# error的自动处理
try:
	# 如果出现error，就试试看点击 id为passbutton 的页面元素，登录网站
	# 因为调试bug时候发现我的代码会卡在这一句
    driver.find_element_by_id("passbutton").click()
except:
	# 尝试点击失败（卡住），停止加载页面
    driver.execute_script("window.stop()")

