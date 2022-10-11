import time
from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# launch demo web shop
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# locating search bar using id locator
# element = driver.find_element("id", "small-searchterms")
# print(element)
# element.click()
# time.sleep(1)
# element.send_keys("mobiles")

# locating search bar using class name locator
# driver.find_element("class name", "search-box-text.ui-autocomplete-input").send_keys("books")

# driver.find_element("class name", "ico-register").click()

# driver.find_element("link text", "Register").click()
# driver.find_element("id", "gender-female").click()
# driver.find_element("id", "FirstName").send_keys("sita")
# driver.find_element("id", "LastName").send_keys("ram")
# driver.find_element("name", "Email").send_keys("sita@123")
#
# driver.find_element("id", "Password").send_keys("ram123")
# driver.find_element("id", "ConfirmPassword").send_keys("ram123")

driver.find_element("partial link text", "Reg")


register_link = driver.find_element("class name", "ico-register")
print(register_link.text)
print(register_link.location)
print(register_link.size)
print(register_link.rect)
print(register_link.get_attribute("href"))

