# import time
# from selenium import webdriver
# path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
#
# # driver.get("https://www.myntra.com/boys-tshirts")
# # driver.maximize_window()
#
# # driver.implicitly_wait(10)
# # driver.find_element("xpath", '//label[text()="Pepe Jeans"]//div').click()
#
# #####################################################################################
# # name, discounted price
#
# xpath_ = '//span[@class="product-discountedPrice"]/../../..//h4[@class="product-product"]|//span[@class="product-discountedPrice"]'
#
#
# # names = driver.find_elements("xpath", xpath_)
# # for name in names:
# #     time.sleep(1)
# #     print(name.text)
# #
# # driver.close()
#
# ##############################################################################
#
# # driver.get("https://www.python.org/")
# #
# # links = driver.find_elements("xpath", '//a[contains(text(),"python")]')
# # link_text = []
# #
# # for link in links:
# #     text_ = link.text
# #     attr = link.get_attribute("href")
# #     link_text.append((text_, attr))
#
# # print(link_text)
# # driver.close()
#
# ###################################################################################
# driver.get(r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\HTML files\demo.html")
# driver.maximize_window()
#
# text_boxes = driver.find_elements("xpath", '//input[@name="fname"]')
# # [t1, t2, t3, t4, t5, t6, t7, t8, t9]
#
# words = ["hi", "hello", "welcome", "to", "python", "selenium", "hi", "python", "bye"]
#
#
# for element, text in zip(text_boxes, words):  # [(t1, "hi), (t2, "hello"), (t3, "welcome)....]
#     element.send_keys(text)
#     time.sleep(1)
#




