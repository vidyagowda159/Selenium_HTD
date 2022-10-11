import time
from selenium import webdriver
path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

file_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html"
driver.get(file_path)
driver.maximize_window()

"""
1. identify dependent and independent elements
2. write locator expression for independent element
3. traverse backward until the common parent of both dep and indep elements is obtained.
4. locate the dependent element
"""

languages = ["JavaScript", "Java", "Ruby", "Perl", "C#", "Python"]

for language in languages:
    driver.find_element("xpath", f'//td[text()="{language}"]/..//input[@name="download"]').click()
    time.sleep(1)



