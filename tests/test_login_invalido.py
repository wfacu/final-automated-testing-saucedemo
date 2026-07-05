from pages.login_page import LoginPage


def test_login_invalido(driver):

    login = LoginPage(driver)

    login.open()
    login.login("usuario_invalido", "password_invalida")

    assert "Epic sadface" in login.get_error_message()
    assert "inventory.html" not in driver.current_url