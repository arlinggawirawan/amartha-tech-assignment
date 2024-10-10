import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.add_to_chart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.chart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.assert_chart = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def add_to_chart(self):
        self.driver.find_element(*self.add_to_chart_button).click()
        self.driver.find_element(*self.chart_button).click()
        try:
            price = self.driver.find_element(*self.assert_chart)
            assert price.text == "$29.99", f"Expected price '$29.99', but got {price.text}"
            print("Product successfully added, price is displayed correctly.")
        except NoSuchElementException:
            pytest.fail("Product was not added to the cart, price element is missing.")
        except AssertionError as e:
            pytest.fail(str(e))

