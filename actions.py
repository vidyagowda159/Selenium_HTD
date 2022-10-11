import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

action_obj = ActionChains(driver)

# driver.get("https://www.myntra.com/")
# driver.maximize_window()
#
# element = driver.find_element("xpath", '//a[@data-group="men"]')
# action_obj.move_to_element(element).perform()

#####################################################################################
# path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
# driver.get(path)
# driver.maximize_window()
#
# webelement_ = driver.find_element("id", "double-click")
# action_obj.double_click(webelement_).perform()
#
# ######################################################################################
# path = r"https://crossbrowsertesting.github.io/drag-and-drop.html"
#
# driver.get(path)
# driver.maximize_window()
#
# source = driver.find_element("id", 'draggable')
# destination = driver.find_element("id", "droppable")
#
# action_obj.drag_and_drop(source, destination).perform()

#####################################################################################
# from selenium.webdriver.common.keys import Keys
#
# path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
#
# driver.get(path)
# driver.maximize_window()
#
# action_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#########################################################################################

path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"

driver.get(path)
driver.maximize_window()

element = driver.find_element("id", "first_name")
print(element.is_displayed())
time.sleep(2)
print(element.is_enabled())

driver.close()
