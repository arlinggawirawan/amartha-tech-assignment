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
        self.invalid_user = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def invalid_login(self):
        error_element = self.driver.find_element(*self.invalid_user)
        error_message = error_element.text
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        assert error_message == expected_message, f"Expected message: '{expected_message}', but got: '{error_message}'"
        print("Assertion passed: Locked out user error message is correct.")

    def add_to_chart(self):
        self.driver.find_element(*self.add_to_chart_button).click()
        self.driver.find_element(*self.chart_button).click()
        try:
            price = self.driver.find_element(*self.assert_chart)
            product_price = price.text
            print(f"Product price from UI: {product_price}")
            assert "$" in product_price, f"Expected a valid price format, but got: {product_price}"
            print("Product successfully added, price is displayed correctly.")
        except NoSuchElementException:
            pytest.fail("Product was not added to the cart, price element is missing.")
        except AssertionError as e:
            pytest.fail(str(e))
