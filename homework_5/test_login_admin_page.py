from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_5.framework import wait_element, wait_title_contain

LOGIN_ADMIN_PATH = '/admin/'
PAGE_TITLE = "Administration"
LOGO = (By.XPATH, '//header//img')
FORM_HEADER = (By.XPATH, '//div[@class="card-header"]')
INPUT_LOGIN = (By.XPATH, '//input[@name="username"]')
INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
FORGOTTEN_PASSWORD = (By.XPATH, '//div[@class="mb-3"]/a')
BUTTON_LOGIN = (By.XPATH, '//button[@type="submit"]')


def test_login_admin_page(driver: WebDriver) -> None:
    driver.get(driver.url + LOGIN_ADMIN_PATH)
    wait_title_contain(driver=driver, text=PAGE_TITLE)
    wait_element(driver=driver, locator=LOGO)
    wait_element(driver=driver, locator=FORM_HEADER)
    wait_element(driver=driver, locator=INPUT_LOGIN)
    wait_element(driver=driver, locator=INPUT_PASSWORD)
    wait_element(driver=driver, locator=FORGOTTEN_PASSWORD)
    wait_element(driver=driver, locator=BUTTON_LOGIN)
