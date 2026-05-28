import os
import pytest
import logging

from datetime import datetime

from utils.functions import setup_driver

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def driver():

    driver = setup_driver()

    logging.info("Driver iniciado")

    yield driver

    driver.quit()

    logging.info("Driver cerrado")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_name)

            logging.error(
                f"Test fallido: {item.name}"
            )

            logging.error(
                f"Screenshot guardado en: {screenshot_name}"
            )