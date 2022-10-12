import re
import xlrd
import pytest
from selenium import webdriver

class ReadExcel:

    def read_testdata(self):
        f_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\test_data\demowebshop_testdata.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("reg_credentials")
        rows = ws.get_rows()       # generator object
        header = next(rows)
        data = []
        for row in rows:
            element = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
            data.append(element)
        return data

    def read_locators(self):
        f_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\test_data\locators.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("reg_objects")
        rows = ws.get_rows()
        header = next(rows)

        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)

        return d


@pytest.fixture(params=["Chrome", "firefox", "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path)

    elif browser.lower() == "firefox":
        firefox_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefox_path)

    else:
        edge_path = r"C:\Users\Vidyashree M C\PycharmProjects\Selenium_HTD\drivers\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_path)

    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()


class RegisterPage:

    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators()

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        locator = self.reg_locators["register_link"]
        self.driver.find_element(*locator).click()

    def select_female_radio_btn(self):
        locator_name, locator_value = self.reg_locators["female_radio_btn"]
        self.driver.find_element(locator_name, locator_value).click()

    def select_male_radio_btn(self):
        locator = self.reg_locators["male_radio_btn"]
        self.driver.find_element(*locator).click()

    def enter_firstname(self, f_name):
        locator = self.reg_locators["firstname_txt"]
        self.driver.find_element(*locator).send_keys(f_name)

    def enter_lastname(self, l_name):
        locator = self.reg_locators["lastname_txt"]
        self.driver.find_element(*locator).send_keys(l_name)

    def enter_email(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"

        locator = self.reg_locators["email_txt"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_password(self, pwd):
        if isinstance(pwd, float):
            pwd = str(int(pwd))

        assert len(pwd) >= 6, "password should have atleast 6 characters"
        locator = self.reg_locators["password_txt"]
        self.driver.find_element(*locator).send_keys(pwd)
        return pwd

    def confirm_password(self, c_pwd, actual_pwd):
        if isinstance(c_pwd, float):
            c_pwd = str(int(c_pwd))

        locator = self.reg_locators["confirm_password_txt"]
        assert actual_pwd == c_pwd, "passwords are different"
        self.driver.find_element(*locator).send_keys(c_pwd)


class TestRegisterPage:
    read_xl = ReadExcel()
    data = read_xl.read_testdata()

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