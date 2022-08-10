from _pytest.config.argparsing import Parser
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--url', action='store',
                     default='https://demo.opencart.com/')
    parser.addoption('--browser', action='store', default='chrome',
                     choices=['chrome', 'firefox', 'opera'])


@pytest.fixture(scope='module')
def driver(request: FixtureRequest) -> WebDriver:
    browser = request.config.getoption('--browser')

    if browser == "chrome":
        web_driver = webdriver.Chrome()
    elif browser == "firefox":
        web_driver = webdriver.Firefox()
    elif browser == "opera":
        web_driver = webdriver.Opera()
    web_driver.maximize_window()
    web_driver.url = request.config.getoption('--url')

    yield web_driver
    web_driver.quit()
