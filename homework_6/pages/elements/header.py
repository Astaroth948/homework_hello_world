from selenium.webdriver.common.by import By
from homework_6.pages.base_page import BasePage


class Header(BasePage):
    LOGO = (By.XPATH, '//div[@id="logo"]')
    BUTTON_BASKET = (By.XPATH, '//button[@data-toggle="dropdown"]')
    SEARCH_STRING = (By.XPATH, '//div[@id="search"]')
    SELECT_CURRENCY = (By.XPATH, '//form[@id="form-currency"]')
    OPTION_CURRENCY = (
        By.XPATH, '//form[@id="form-currency"]//ul/li/button[text()="currency-&"]')
    ICON_CURRENCY = (By.XPATH, '//form[@id="form-currency"]//strong')

    def assert_logo(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.LOGO, timeout=timeout)

    def assert_button_basket(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_BASKET, timeout=timeout)

    def assert_search_string(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.SEARCH_STRING, timeout=timeout)

    def select_currency(self, currency: str = '€ Euro', timeout: int = 5) -> None:
        self._click(locator=self.SELECT_CURRENCY, timeout=timeout)
        self._click(locator=(self.OPTION_CURRENCY[0], self.OPTION_CURRENCY[1].replace(
            'currency-&', currency)), timeout=timeout)

    def assert_icon_currency(self, currency: str, timeout: int = 5) -> None:
        self._assert_text_in_element_equal_to(
            locator=self.ICON_CURRENCY, text=currency[0], timeout=timeout)
