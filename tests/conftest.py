import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import attach
browser.config.timeout = 20


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = os.getenv('selene.base_url', 'https://www.labirint.ru')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    remote_drv = os.getenv('REMOTE_DRV')
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    driver = webdriver.Remote(
        # command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        command_executor=f"{remote_drv}",

        options=options)

    browser.config.driver = driver
    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()