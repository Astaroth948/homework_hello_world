import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import allure

from homework_7.pages.elements.header import Header


@allure.parent_suite('Проверки главной страницы')
@allure.epic('Проверки главной страницы')
@allure.title('Проверка переключения валют')
@pytest.mark.parametrize('currency', ['€ Euro', '£ Pound Sterling', '$ US Dollar'])
def test_switching_currencies(driver: WebDriver, currency: str) -> None:
    header = Header(driver)

    header._open(driver.url)
    header.select_currency(currency=currency)
    header.assert_icon_currency(currency=currency)
