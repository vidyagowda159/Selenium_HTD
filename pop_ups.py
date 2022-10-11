import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
driver.get(file_path)
driver.maximize_window()

# simple alert
driver.find_element("id", "submit").click()
time.sleep(2)
alert_obj = driver.switch_to.alert
print(alert_obj.text)
# alert_obj.accept()
alert_obj.dismiss()

# confirmation alert
driver.find_element("id", "delete").click()
time.sleep(2)

alert_obj = driver.switch_to.alert
# alert_obj.accept()
alert_obj.dismiss()

################################################################################
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element("link text", "Facebook").click()
driver.implicitly_wait(10)
handles = driver.window_handles # returns list of all the window handles that are opened
print(handles)          # [demo web shop, facebook]
print(driver.current_window_handle)     # returns the handle of the active window
print(driver.title)     # returns the title of the active window

print()

driver.switch_to.window(handles[1])
print(driver.current_window_handle)
print(driver.title)
driver.find_element("name", "email").send_keys("abc@gmail.com")
driver.close()

time.sleep(2)
driver.switch_to.window(handles[0])
driver.find_element("link text", "Register").click()

######################################################################################
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\iframe.html"
driver.get(path)
driver.maximize_window()

# switching to a frame using ID attribute
driver.switch_to.frame("FR1")
driver.find_element("id", "small-searchterms").send_keys("mobiles")

# switching back to parent/main frame
driver.switch_to.default_content()

# switching to a frame using name attribute
driver.switch_to.frame("frame2")
driver.find_element("id", 'search_form').send_keys("abc")

# switching to a frame using webelement
frame_ = driver.find_element('xpath', '//iframe[@name="frame2"]')

driver.switch_to.frame(frame_)
driver.find_element("id", 'search_form').send_keys("abc")

######################################################################################

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element("xpath", '//span[text()="Upload Resume"]').click()
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\demo.txt"

driver.find_element("xpath", '(//input[@id="file-upload"])[1]').send_keys(path)












