import allure
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.about_page import AboutPages
from config.conftest import Config


@pytest.fixture(scope='function')
def setup():
    driver = DriverFactory.create_driver()
    login_page = LoginPage(driver)
    about_page = AboutPages(driver)
    yield driver, login_page, about_page
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("standard_user", Config.PASSWORD),
    ("locked_out_user", Config.PASSWORD),
    ("problem_user", Config.PASSWORD),
    ("performance_glitch_user", Config.PASSWORD),
    ("error_user", Config.PASSWORD),
    ("visual_user", Config.PASSWORD)
])
@allure.epic("Test case login flow and add to chart")
@allure.story("As a user I want to login and add product to chart")
@allure.label("owner", "Arlingga")
@allure.description("This test to validate automate login flow and verify the item is added to chart")
@allure.title("Verify login and add to chart")
def test_loginflow_and_addtochart(setup, username, password):
    with allure.step("Running test login flow and add product to chart"):
        driver, login_page, _ = setup
        login_page.open(Config.BASE_URL)
        print(f"Opened URL: {Config.BASE_URL}")
        login_page.login(username, password)
        if username == "locked_out_user":
            error_element = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
            error_message = error_element.text
            expected_message = "Epic sadface: Sorry, this user has been locked out."
            assert error_message == expected_message, f"Expected message: '{expected_message}', but got: '{error_message}'"
            print("Assertion passed: Locked out user error message is correct.")
        else:
            login_page.add_to_chart()
            print("Added to chart successfully.")


@pytest.mark.parametrize("username, invalid_password", [
    ("standard_user", Config.INVALID_PASSWORD),
    ("locked_out_user", Config.INVALID_PASSWORD),
    ("problem_user", Config.INVALID_PASSWORD),
    ("performance_glitch_user", Config.INVALID_PASSWORD),
    ("error_user", Config.INVALID_PASSWORD),
    ("visual_user", Config.INVALID_PASSWORD)
])
@allure.epic("Test case invalid login flow and add to chart")
@allure.story("As a user I have invalid user and can't be login")
@allure.label("owner", "Arlingga")
@allure.description("This test to validate automate invalid login flow and verify should not be able to login")
@allure.title("Verify invalid login")
def test_invalid_login(setup, username, invalid_password):
    with allure.step("Running test invalid login flow and verify error message"):
        driver, login_page, _ = setup
        login_page.open(Config.BASE_URL)
        print(f"Opened URL: {Config.BASE_URL}")
        login_page.login(username, invalid_password)
        login_page.invalid_login()


@allure.epic("Test case login flow and navigate to about page")
@allure.story("As a user I want to login and see the about page")
@allure.label("owner", "Arlingga")
@allure.description("This test to validate automate login flow and verify navigate to about page")
@allure.title("Verify login and navigate to about page")
def test_loginflow_and_about(setup):
    with allure.step("Running test login flow and navigate to about page"):
        driver, login_page, about_page = setup
        login_page.open(Config.BASE_URL)
        print(f"Opened URL: {Config.BASE_URL}")
        login_page.login(Config.USERNAME, Config.PASSWORD)
        print(f"Opened URL: {Config.BASE_URL}")
        about_page.about()
        expected_url = Config.NAVIGATE_ABOUT_EXPECTED_URL
        print(f"Current URL: {driver.current_url}")
        assert driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {driver.current_url}"
        print("Assertion passed: Current URL matches expected URL.")