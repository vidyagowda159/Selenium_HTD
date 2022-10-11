from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\css_selector.html"
# driver.get(file_path)
# driver.maximize_window()
#
# driver.find_element("css selector", 'input[type="text"]').send_keys("user1")
# driver.find_element("css selector", 'input[type="password"]').send_keys("pwd")

##################################################################################

driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

driver.find_element("css selector", 'input[placeholder="Username"]').send_keys("admin")
driver.find_element("css selector", 'input[placeholder="Password"]').send_keys("manager")
driver.find_element("css selector", 'a[id="loginButton"]>div').click()











