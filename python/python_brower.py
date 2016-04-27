from splinter.browser import Browser
import time

url = "http://oa-center/Programs/login/login.aspx"
with Browser() as browser:
	browser.visit(url)
	browser.fill('tbUserName','2949')
	browser.fill('tbPassword','peng910206')
	browser.find_by_name('btnLogin').first.click()
	print browser.url
	time.sleep(2)

