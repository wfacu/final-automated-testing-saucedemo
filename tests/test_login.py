from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.functions import login


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