import time
from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
# driver.get(file_path)
# driver.maximize_window()

# find the number of link tags in demo.html

# using tagname
# link_tags = driver.find_elements("tag name", "a")
#
# # using xpath
# link_tags = driver.find_elements("xpath", "//a")
# print(link_tags)            # list of webelements matching all the link tags
# print(len(link_tags))       # 15
#
# # traversing through the list of webelements
# for link in link_tags:
#     print(link)           # web element

############################################################################################
# # select all the check boxes in demo.html
#
# check_boxes = driver.find_elements("css selector", 'input[type="checkbox"]')
# print(len(check_boxes))
#
# for check_box in check_boxes:
#     check_box.click()
#     time.sleep(1)

############################################################################################
# # printing the texts in link tags
#
# link_tags = driver.find_elements("tag name", "a")
#
# for link in link_tags:
#     print(link.text)

###########################################################################################
# # printing links of link tags
#
# links = driver.find_elements("tag name", "a")
#
# for link in links:
#     print(link.get_attribute("href"))

###########################################################################################
# # extracting only the links with "python" in it
#
# driver.get("https://www.python.org/")
# driver.maximize_window()
#
# # using xpath/ tagname
# links = driver.find_elements("xpath", "//a")        # 233
# print(len(links))
#
# for link in links:
#     if "python" in link.text:
#         print(link.text)
# print()
#
# # using partial link text
#
# links = driver.find_elements("partial link text", "python")
# print(len(links))
#
# for link in links:
#     print(link.text)
# print()
#
#
# # using contains()
# links = driver.find_elements("xpath", '//a[contains(text(),"python")]')
# print(len(links))
#
# for link in links:
#     print(link.text)
#
# driver.close()

############################################################################
# text of all the links in categories

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

links = driver.find_elements("xpath", '//div[@class="block block-category-navigation"]//a')
print(len(links))

for link in links:
    print(link.text)




















