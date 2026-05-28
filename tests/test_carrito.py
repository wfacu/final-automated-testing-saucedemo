from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.functions import login


def test_interaccion_carrito(driver):

    login(driver)

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    boton_agregar = primer_producto.find_element(
        By.TAG_NAME,
        "button"
    )

    boton_agregar.click()

    wait = WebDriverWait(driver, 10)

    contador_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador_carrito.text == "1"

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert producto_carrito.text == nombre_producto