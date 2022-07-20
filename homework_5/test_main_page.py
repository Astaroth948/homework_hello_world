from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_5.framework import wait_element, wait_title_contain

PAGE_TITLE = "Your Store"
LOGO = (By.XPATH, '//div[@id="logo"]')
BUTTON_BASKET = (By.XPATH, '//button[@data-bs-toggle="dropdown"]')
MENU = (By.XPATH, '//div[@id="narbar-menu"]')
SEARCH = (By.XPATH, '//div[@id="search"]')
TOP_CAROUSEL = (By.XPATH, '//div[@id="carousel-banner-0"]')
BOTTOM_CAROUSEL = (By.XPATH, '//div[@id="carousel-banner-1"]')


def test_main_page(driver: WebDriver) -> None:
    driver.get(driver.url)
    wait_title_contain(driver=driver, text=PAGE_TITLE)
    wait_element(driver=driver, locator=LOGO)
    wait_element(driver=driver, locator=BUTTON_BASKET)
    wait_element(driver=driver, locator=MENU)
    wait_element(driver=driver, locator=SEARCH)
    wait_element(driver=driver, locator=TOP_CAROUSEL)
    wait_element(driver=driver, locator=BOTTOM_CAROUSEL)
