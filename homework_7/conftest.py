from _pytest.config.argparsing import Parser
import pytest
import logging
import datetime

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.opera import options as OperaOptions


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--url', action='store',
                     default='https://demo.opencart.com/')
    parser.addoption('--browser', action='store', default='chrome',
                     choices=['chrome', 'firefox', 'opera'])
    parser.addoption('--executor', default='local')
    parser.addoption("--log_level", default="DEBUG")
    parser.addoption('--bv', default=None)
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--logs', action='store_true')
    parser.addoption('--videos', action='store_true')
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='module')
def driver(request: FixtureRequest) -> WebDriver:
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    executor = request.config.getoption('--executor')
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption('--bv')
    vnc = request.config.getoption('--vnc')
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == 'local':
        if browser == 'chrome':
            options = ChromeOptions()
            options.headless = headless
            options.add_argument('window-size=1920,1080')
            web_driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            options = FirefoxOptions()
            options.headless = headless
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            web_driver = webdriver.Firefox(options=options)
        elif browser == 'opera':
            options = OperaOptions.ChromeOptions()
            options.headless = headless
            options.add_argument('window-size=1920,1080')
            options.add_experimental_option('w3c', True)
            web_driver = webdriver.Opera(options=options)
    else:
        executor_url = f'http://{executor}:4444/wd/hub'
        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Marat",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs,
                "sessionTimeout": "2m"
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
        }
        options = Options()
        options.headless = headless
        options.add_argument('window-size=1920,1080')
        if browser == "opera":
            options.add_experimental_option('w3c', True)

        web_driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

    logger = logging.getLogger(request.node.name)
    logger.addHandler(logging.FileHandler(
        f"homework_7/logs/{web_driver.session_id}.log"))
    logger.setLevel(level=log_level)

    date_test_started = datetime.datetime.now()
    logger.info(
        f"===> Test {request.node.name} started at {date_test_started}")

    web_driver.log_level = log_level
    web_driver.logger = logger
    web_driver.test_name = request.node.name

    if not headless:
        web_driver.maximize_window()
    web_driver.url = request.config.getoption('--url')

    yield web_driver
    date_test_finished = datetime.datetime.now()
    web_driver.logger.info(
        f"===> Test {request.node.name} finished at {date_test_finished}. "
        f"Execution time {date_test_finished - date_test_started}")
    web_driver.quit()
