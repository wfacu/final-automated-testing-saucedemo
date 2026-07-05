from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_exitoso(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    assert inventory.get_title() == "Producto"