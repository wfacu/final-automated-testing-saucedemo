import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.functions import setup_driver, login


@pytest.fixture
def driver():

    driver = setup_driver()

    yield driver

    driver.quit()


def test_login_exitoso(driver):

    login(driver)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("/inventory.html")
    )

    titulo = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert "/inventory.html" in driver.current_url
    assert titulo.text == "Products"


def test_verificacion_catalogo(driver):

    login(driver)

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre} - {precio}")

    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()


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