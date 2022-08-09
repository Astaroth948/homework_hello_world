from selenium.webdriver.common.by import By
from homework_6.pages.base_page import BasePage


class AdminMenu(BasePage):
    TAB_CUSTOMERS = (By.XPATH, '//li[@id="menu-customer"]/a')
    LINK_CUSTOMERS = (
        By.XPATH, '//li[@id="menu-customer"]//a[text()="Customers"]')
    TAB_CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a')
    LINK_PRODUCTS = (
        By.XPATH, '//li[@id="menu-catalog"]//a[text()="Products"]')

    def goto_customers_list(self, timeout: int = 5) -> None:
        if 'collapsed' in self._get_attribute(locator=self.TAB_CUSTOMERS, attribute='class', timeout=timeout):
            self._click(locator=self.TAB_CUSTOMERS, timeout=timeout)
        self._click(locator=self.LINK_CUSTOMERS, timeout=timeout)

    def goto_products_list(self, timeout: int = 5) -> None:
        if 'collapsed' in self._get_attribute(locator=self.TAB_CATALOG, attribute='class', timeout=timeout):
            self._click(locator=self.TAB_CATALOG, timeout=timeout)
        self._click(locator=self.LINK_PRODUCTS, timeout=timeout)
