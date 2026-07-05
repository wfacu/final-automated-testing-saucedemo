import logging

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        logging.info("Abriendo SauceDemo")
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        logging.info(f"Intentando login con usuario: {username}")

        self.driver.find_element(
            By.ID,
            "user-name"
        ).send_keys(username)

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()

    def get_error_message(self):
        logging.info("Obteniendo mensaje de error del login")

        return self.driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        ).text