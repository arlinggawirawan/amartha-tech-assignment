from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AboutPages:
    def __init__(self, driver):
        self.driver = driver
        self.hamburger_button = (By.ID, "react-burger-menu-btn")
        self.about_button = (By.XPATH, "//a[@id='about_sidebar_link']")


    def about(self):
        self.driver.find_element(*self.hamburger_button).click()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.about_button)
        )
        self.driver.find_element(*self.about_button).click()
