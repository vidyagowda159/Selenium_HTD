import time
from selenium import webdriver

path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# launching the url
url = "https://demowebshop.tricentis.com/"
driver.get(url)

# # minimize, maximize, full_screen
# driver.maximize_window()
# time.sleep(1)
# driver.minimize_window()
# time.sleep(1)
# driver.fullscreen_window()

# position and size
print(driver.get_window_position())        # {x:, y: }
print(driver.get_window_size())     # {width: , height:}
print(driver.get_window_rect())     # {x, y, width, height}

# refresh, back, forward
driver.refresh()
driver.back()
time.sleep(2)
driver.forward()

# name
print(driver.title)
print(driver.current_url)
print(driver.name)

# close and quit
# driver.close()
# driver.quit()