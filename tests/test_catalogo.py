from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_verificacion_catalogo(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.get_title() == "Products"

    productos = inventory.get_products()

    assert len(productos) > 0

    nombre = inventory.get_first_product_name()

    precio = productos[0].find_element(
        "class name",
        "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre} - {precio}")

    menu = driver.find_element(
        "id",
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        "class name",
        "product_sort_container"
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()