import logging

from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        logging.info("Obteniendo nombre del producto en el carrito")

        return self.driver.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

    def click_checkout(self):
        logging.info("Ingresando al checkout")

        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()