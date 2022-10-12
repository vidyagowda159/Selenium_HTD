import re
import pytest
from selenium import webdriver


@pytest.fixture()
def init_driver():
    chrome_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        self.driver.find_element("link text", "Register").click()

    def select_female_radio_btn(self):
        self.driver.find_element("id", "gender-female").click()

    def select_male_radio_btn(self):
        self.driver.find_element("id", "gender-male").click()

    def enter_firstname(self, f_name):
        self.driver.find_element("id", "FirstName").send_keys(f_name)

    def enter_lastname(self, l_name):
        self.driver.find_element("name", "LastName").send_keys(l_name)

    def enter_email(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"
        self.driver.find_element("id", "Email").send_keys(email)

    def enter_password(self, pwd):
        assert len(pwd) >= 6, "password should have atleast 6 characters"
        self.driver.find_element("name", "Password").send_keys(pwd)
        return pwd

    def confirm_password(self, c_pwd, actual_pwd):
        assert actual_pwd == c_pwd, "passwords are different"
        self.driver.find_element("name", "ConfirmPassword").send_keys(c_pwd)

data = [
    ("Tata", "Birla", "tatabirla@gmail.com", "123456", "123456"),
    ("Tata", "Birla", "tatabirla@", "123456", "123456"),
    ("Tata", "Birla", "tatabirla@gmail.com", "123456", "123456"),
    ("Tata", "Birla", "tatabirla@gmail.com", "12345", "123456"),
    ("Tata", "Birla", "tatabirla@gmail.com", "123456", "1234567"),
    ("Tata", "Birla", "tatabirla@gmail.com", "123456", "123456")
    ]

class TestRegisterPage:

    @pytest.mark.parametrize("f_name, l_name, email, pwd, c_pwd", data)
    def test_registration(self, f_name, l_name, email, pwd, c_pwd, init_driver):
        driver = init_driver
        rp = RegisterPage(driver)  # rp = RegisterPage(init_driver)
        rp.click_register_link()
        rp.select_male_radio_btn()
        rp.enter_firstname(f_name)
        rp.enter_lastname(l_name)
        rp.enter_email(email)
        actual_pwd = rp.enter_password(pwd)
        rp.confirm_password(c_pwd, actual_pwd)