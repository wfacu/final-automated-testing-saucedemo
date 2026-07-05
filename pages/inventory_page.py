import logging

from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        logging.info("Obteniendo título del catálogo")

        return self.driver.find_element(
            By.CLASS_NAME,
            "title"
        ).text

    def get_products(self):
        logging.info("Obteniendo listado de productos")

        return self.driver.find_elements(
            By.CLASS_NAME,
            "inventory_item"
        )

    def get_first_product_name(self):
        producto = self.get_products()[0]

        return producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

    def get_first_product_price(self):
        producto = self.get_products()[0]

        return producto.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        ).text

    def add_first_product(self):
        logging.info("Agregando primer producto al carrito")

        producto = self.get_products()[0]

        producto.find_element(
            By.TAG_NAME,
            "button"
        ).click()

    def get_cart_badge(self):
        logging.info("Consultando cantidad de productos en el carrito")

        return self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_badge"
        ).text

    def open_cart(self):
        logging.info("Abriendo carrito")

        self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

    def is_menu_displayed(self):
        return self.driver.find_element(
            By.ID,
            "react-burger-menu-btn"
        ).is_displayed()

    def is_sort_displayed(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        ).is_displayed()