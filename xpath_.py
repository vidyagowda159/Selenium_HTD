from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# driver.get("https://demo.actitime.com/login.do")
# driver.maximize_window()
#
# # xpath using attributes
# driver.find_element("xpath", '//input[@id="username"]').send_keys("admin")
# driver.find_element("xpath", '//input[@placeholder="Password"]').send_keys("manager")
#
# # xpath using text()
# driver.find_element("xpath", '//div[text()="Login "]').click()

########################################################################################

file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
driver.get(file_path)
driver.maximize_window()

# xpath using group indexing
driver.find_element("xpath", '(//input[@name="download"])[2]').click()












