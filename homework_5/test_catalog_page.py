from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_5.framework import wait_element, wait_title_contain

CATALOG_PATH = '/index.php?route=product/category&language=en-gb&path=20'
PAGE_TITLE = "Desktops"
LOGO = (By.XPATH, '//div[@id="logo"]')
BUTTON_BASKET = (By.XPATH, '//button[@data-bs-toggle="dropdown"]')
MENU = (By.XPATH, '//div[@id="narbar-menu"]')
SEARCH = (By.XPATH, '//div[@id="search"]')
BREADCRUMB = (By.XPATH, '//ul[@class="breadcrumb"]')
LEFT_MENU = (By.XPATH, '//div[@class="list-group mb-3"]')
DISPLAY_CONTROL = (By.XPATH, '//div[@id="display-control"]')
PRODUCT_LIST = (By.XPATH, '//div[@id="product-list"]')


def test_catalog_page(driver: WebDriver) -> None:
    driver.get(driver.url + CATALOG_PATH)
    wait_title_contain(driver=driver, text=PAGE_TITLE)
    wait_element(driver=driver, locator=LOGO)
    wait_element(driver=driver, locator=BUTTON_BASKET)
    wait_element(driver=driver, locator=MENU)
    wait_element(driver=driver, locator=SEARCH)
    wait_element(driver=driver, locator=BREADCRUMB)
    wait_element(driver=driver, locator=LEFT_MENU)
    wait_element(driver=driver, locator=DISPLAY_CONTROL)
    wait_element(driver=driver, locator=PRODUCT_LIST)
