from selenium.webdriver.common.by import By
from homework_6.pages.base_page import BasePage


class Breadcrumbs(BasePage):
    BREADCRUMBS = (By.XPATH, '//ul[@class="breadcrumb"]')

    def assert_breadcrumbs(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BREADCRUMBS, timeout=timeout)
