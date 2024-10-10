import allure
import pytest
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

@allure.epic("Test case login flow and add to chart")
@allure.story("As a user I want to login and add product to chart")
@allure.label("owner", "Arlingga")
@allure.description("This test to validate automate login flow and verify the item is added to chart")
@allure.title("Verify login and add to chart")
def test_loginflow_and_addtochart(setup):
    with allure.step("Running test login flow and add product to chart"):
        driver, login_page, about_page = setup
        login_page.open(Config.BASE_URL)
        print(f"Opened URL: {Config.BASE_URL}")
        login_page.login(Config.USERNAME, Config.PASSWORD)
        print(f"Opened URL: {Config.BASE_URL}")
        login_page.add_to_chart()
        print("Added to chart successfully.")


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