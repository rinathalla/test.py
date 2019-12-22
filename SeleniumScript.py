# https://youtu.be/zRrubJ13I8s


#import webbrowser
#webbrowser.open('https://www.twitter.com')

from selenium import webdriver

driver = webdriver.Chrome('C:\\Python37\\chromedriver.exe')
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file('C:\\Users\\Administrator\\PycharmProjects\\Project1\\Screenshots\\Facebook1.png')
driver.find_element_by_id("email").send_keys("rina@facebook.com")
driver.find_element_by_name("pass").send_keys("*******")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file('C:\\Users\\Administrator\\PycharmProjects\\Project1\\Screenshots\\Facebook2.png')
driver.quit()
#driver.refresh()
#driver.back()
#driver.forward()