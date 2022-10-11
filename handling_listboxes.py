import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
driver.get(file_path)
driver.maximize_window()

listbox = driver.find_element("xpath", '//select[@id="standard_cars"]')
obj = Select(listbox)

# selecting the option by value attribute
obj.select_by_value("hda")
time.sleep(1)

# selecting the option by visible text
obj.select_by_visible_text("Mini")
time.sleep(1)

# selecting the option by index(starts from 0)
obj.select_by_index(1)

# returns list of webelements of all the options
all_options = obj.options
print(all_options)      # list of webelements

# for option in all_options:
#     print(option.text)


# selecting all the options using index
all_options = obj.options

# for index in range(len(all_options)):      # 12
#     obj.select_by_index(index)
#     time.sleep(1)

for index in range(len(all_options)-1, -1, -1):
    obj.select_by_index(index)
    time.sleep(1)

# selecting all the options using visible_text
# all_options = obj.options
#
# for option in all_options:
#     obj.select_by_visible_text(option.text)
#     time.sleep(1)

# selecting all the options using value
# all_options = obj.options
#
# for option in all_options:
#     val = option.get_attribute("value")
#     obj.select_by_value(val)
#     time.sleep(1)

# print(obj.is_multiple)

######################################################################
# listbox = driver.find_element("id", "multiple_cars")
#
# # create an object of Select class
# s_obj = Select(listbox)
#
# # selecting options
# s_obj.select_by_value("for")
# time.sleep(1)
# s_obj.select_by_index(1)
# time.sleep(1)
# s_obj.select_by_visible_text("BMW")
#
# # selecting all options using index
# # all_options = s_obj.options
# #
# # for index in range(len(all_options)):
# #     s_obj.select_by_index(index)
# #     time.sleep(1)
#
# # deselecting options
# s_obj.deselect_by_visible_text("Ford")
# time.sleep(1)
# s_obj.deselect_by_index(2)
# time.sleep(1)
# s_obj.deselect_by_value("aud")
#
# # s_obj.deselect_all()
#
# # returns list of webelement of selected options
# selected_options = s_obj.all_selected_options
#
# # for option in selected_options:
# #     print(option.text)
#
#
# # first_selected_option --> one element
#
# print(s_obj.first_selected_option.text)
#
# print(s_obj.is_multiple)


