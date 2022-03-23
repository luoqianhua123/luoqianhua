import time
from selenium import webdriver                                      #导包
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
web=webdriver.Chrome()
#打开网址
web.get('http://123.57.140.190/manage/')
#窗口最大化
web.maximize_window()

web.implicitly_wait(10)
time.sleep(3)
#账号
web.find_element(By.CSS_SELECTOR,'body > div > section > form > div > input:nth-child(1)').send_keys('admin')
#密码
web.find_element(By.CSS_SELECTOR,'body > div > section > form > div > input:nth-child(2)').send_keys('admin999')
#登录
web.find_element(By.CSS_SELECTOR,'body > div > section > form > div > input.btn.btn-lg.btn-login.btn-block').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#nav-accordion > li:nth-child(1) > a > span:nth-child(2)').click()
web.find_element(By.CSS_SELECTOR,'#nav-accordion > li:nth-child(1) > ul > li:nth-child(1) > a').click()
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('苹果手机')
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('pingguo13')
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('pingguo1314')
web.find_element(By.XPATH,'//*[@id="uppic"]').click()
web.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div[2]/div[1]/span/input').click()
web.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[2]/div/div[2]/div[1]/div[1]/img').click()
time.sleep(2)
web.find_element(By.CSS_SELECTOR,'body > div:nth-child(24) > div.ke-dialog-content > div.ke-dialog-body > div > div.ke-plugin-filemanager-body > div > div.ke-inline-block.ke-photo > img').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="remoteWidth"]').send_keys("100")
web.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div[2]/div[2]/input[2]').send_keys('100')
web.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div[2]/div[3]/input[2]').click()
web.find_element(By.XPATH,'//*[@id="remoteTitle"]').send_keys('就是一个图片')
web.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/span[1]/input').click()
web.switch_to.frame(0)
web.find_element(By.XPATH,'/html/body').send_keys('这是一部手机')
web.switch_to.parent_frame()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[9]/div/button').click()


web.find_element(By.XPATH,'//*[@id="nav-accordion"]/li[1]/a/span[1]').click()
web.find_element(By.XPATH,'//*[@id="nav-accordion"]/li[1]/ul/li[2]/a').click()
#查找产品名称未苹果手机
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[1]/input').send_keys('苹果手机')
#查找到后点击预览
web.find_element(By.XPATH,'//*[@id="myform"]/div/div/section/table/tbody/tr/td[7]/span').click()

#关闭预览
web.find_element(By.CSS_SELECTOR,'#layui-layer1 > span.layui-layer-setwin > a').click()
time.sleep(2)
#点击编辑
web.find_element(By.XPATH,'//*[@id="myform"]/div/div/section/table/tbody/tr[1]/td[8]/a').click()
#改名称删掉一个字符
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[1]/div[1]/input').send_keys(Keys.BACK_SPACE)
#给名称再加一个13
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[1]/div[1]/input').send_keys("13")
#全选编号
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[2]/div[1]/input').send_keys(Keys.CONTROL,'A')
#删除全选的编号
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[2]/div[1]/input').send_keys(Keys.BACK_SPACE)
#输入新的编号
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[2]/div[1]/input').send_keys('18suidepingguo')
#点击确认修改编号
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div[2]/div/section/div/form/div[9]/div/button').click()
#查找名称苹果手13
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/div[1]/input').send_keys('苹果手13')
#点击开始搜索
web.find_element(By.XPATH,'//*[@id="main-content"]/section/div/div/section/div/form/button').click()
#点击选择这个选项
web.find_element(By.XPATH,'//*[@id="chk[]"]').click()
#点击删除
web.find_element(By.XPATH,'//*[@id="myform"]/div/div/section/table/tbody/tr[1]/td[8]/span').click()

time.sleep(2)
#点击确定
web.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]').click()
#页面刷新
web.refresh()
time.sleep(4)
web.close()
web.quit()
