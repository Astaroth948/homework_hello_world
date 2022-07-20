from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_5.framework import wait_element, wait_title_contain

REGISTER_PATH = '/index.php?route=account/register'
PAGE_TITLE = "Register Account"
LOGO = (By.XPATH, '//div[@id="logo"]')
BUTTON_BASKET = (By.XPATH, '//button[@data-bs-toggle="dropdown"]')
MENU = (By.XPATH, '//div[@id="narbar-menu"]')
SEARCH = (By.XPATH, '//div[@id="search"]')
BREADCRUMB = (By.XPATH, '//ul[@class="breadcrumb"]')
INPUT_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
INPUT_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
INPUT_MAIL = (By.XPATH, '//input[@name="email"]')
INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
BUTTON_CONTINUE = (By.XPATH, '//button[@type="submit"]')


def test_register_page(driver: WebDriver) -> None:
    driver.get(driver.url + REGISTER_PATH)
    wait_title_contain(driver=driver, text=PAGE_TITLE)
    wait_element(driver=driver, locator=LOGO)
    wait_element(driver=driver, locator=BUTTON_BASKET)
    wait_element(driver=driver, locator=MENU)
    wait_element(driver=driver, locator=SEARCH)
    wait_element(driver=driver, locator=BREADCRUMB)
    wait_element(driver=driver, locator=INPUT_FIRST_NAME)
    wait_element(driver=driver, locator=INPUT_LAST_NAME)
    wait_element(driver=driver, locator=INPUT_MAIL)
    wait_element(driver=driver, locator=INPUT_PASSWORD)
    wait_element(driver=driver, locator=BUTTON_CONTINUE)
