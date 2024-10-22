import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Config:
    BASE_URL = "https://www.saucedemo.com"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    INVALID_PASSWORD = "secret_sauce123"
    NAVIGATE_ABOUT_EXPECTED_URL = "https://saucelabs.com/"

    @staticmethod
    def get_driver():
        chrome_options = Options()
        headless_mode = os.getenv("HEADLESS", "true").lower() == "true"
        if headless_mode:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver