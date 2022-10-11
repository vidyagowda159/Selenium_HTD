import time
from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
#
# file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\loading.html"
# driver.get(file_path)
# driver.maximize_window()
#
# # unconditional synchronization - time.sleep()
# time.sleep(15)
# firstname = driver.find_element("name", "fname")
# firstname.send_keys("steve")
#
# # conditional synchronization:
#
# # i. implicit wait - driver.implicitly_wait(time_out_value)
# driver.implicitly_wait(5)
# firstname = driver.find_element("name", "fname")
# firstname.send_keys("steve")
#
# # ii. explicit wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# element = driver.find_element("name", "fname")
#
# wait_ = WebDriverWait(driver, 5)
# wait_.until(expected_conditions.visibility_of(element), message="element is not visible")
#
# # waiting until the element is invisible
#
# element = driver.find_element("id", "loader")
# locator_ = ("id", "loader")
#
# # webdriverwait object
# wait_ = WebDriverWait(driver, 30)
# wait_.until(expected_conditions.invisibility_of_element(locator_))
#
# driver.find_element("name", "fname").send_keys("steve")
#


driver.get("https://www.myntra.com/boys-tshirts")
driver.maximize_window()
driver.implicitly_wait(10)
products = driver.find_elements("xpath", '//span[@class="product-discountedPrice"]|//span[@class="product-discountedPrice"]/../../..//h4[@class="product-product"]')

for prod in products[:10]:
    print(prod.text)


driver.close()








