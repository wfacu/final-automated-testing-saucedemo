import logging

from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):
        logging.info("Completando datos del comprador")

        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def finish_checkout(self):
        logging.info("Finalizando compra")

        self.driver.find_element(
            By.ID,
            "finish"
        ).click()

    def get_confirmation_message(self):
        logging.info("Obteniendo mensaje de confirmación")

        return self.driver.find_element(
            By.CLASS_NAME,
            "complete-header"
        ).text