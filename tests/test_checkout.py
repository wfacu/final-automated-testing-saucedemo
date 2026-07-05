from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_exitoso(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product()

    inventory.open_cart()

    cart.click_checkout()

    checkout.fill_information(
        "Facundo",
        "Perez",
        "1234"
    )

    checkout.finish_checkout()

    assert checkout.get_confirmation_message() == "Thank you for your order!"