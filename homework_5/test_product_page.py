from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_5.framework import wait_element, wait_title_contain

PRODUCT_PATH = '/index.php?route=product/product&product_id=43'
PAGE_TITLE = "MacBook"
LOGO = (By.XPATH, '//div[@id="logo"]')
BUTTON_BASKET = (By.XPATH, '//button[@data-bs-toggle="dropdown"]')
MENU = (By.XPATH, '//div[@id="narbar-menu"]')
SEARCH = (By.XPATH, '//div[@id="search"]')
BREADCRUMB = (By.XPATH, '//ul[@class="breadcrumb"]')
PRODUCT_IMAGE = (By.XPATH, '//div[@class="image magnific-popup"]/a/img')
PRODUCT_IMAGES_CAROUSEL = (
    By.XPATH, '//div[@class="image magnific-popup"]/div')
PRODUCT_TITLE = (By.XPATH, '//div[@class="col-sm"]/h1')
PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm"]//h2/span')
BUTTON_ADD_TO_CART = (By.XPATH, '//button[@id="button-cart"]')


def test_product_page(driver: WebDriver) -> None:
    driver.get(driver.url + PRODUCT_PATH)
    wait_title_contain(driver=driver, text=PAGE_TITLE)
    wait_element(driver=driver, locator=LOGO)
    wait_element(driver=driver, locator=BUTTON_BASKET)
    wait_element(driver=driver, locator=MENU)
    wait_element(driver=driver, locator=SEARCH)
    wait_element(driver=driver, locator=BREADCRUMB)
    wait_element(driver=driver, locator=PRODUCT_IMAGE)
    wait_element(driver=driver, locator=PRODUCT_IMAGES_CAROUSEL)
    wait_element(driver=driver, locator=PRODUCT_TITLE)
    wait_element(driver=driver, locator=PRODUCT_PRICE)
    wait_element(driver=driver, locator=BUTTON_ADD_TO_CART)
