from selenium.webdriver.common.by import By

from utils.functions import login


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