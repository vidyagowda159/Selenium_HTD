from selenium import webdriver

# create instance of chrome browser
c_path = R"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
c_driver = webdriver.Chrome(executable_path=c_path)
print(c_driver)

# create instance of firefox browser
f_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\geckodriver.exe"
f_driver = webdriver.Firefox(executable_path=f_path)
print(f_driver)

# create instance of edge browser
e_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\msedgedriver.exe"
e_driver = webdriver.Edge(executable_path=e_path)
print(e_driver)