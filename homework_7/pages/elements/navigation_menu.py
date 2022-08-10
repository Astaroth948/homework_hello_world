from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage


class NavigationMenu(BasePage):
    MENU = (By.XPATH, '//ul[@class="nav navbar-nav"]')
    LEFT_MENU = (By.XPATH, '//aside[@id="column-left"]')
    RIGHT_MENU = (By.XPATH, '//aside[@id="column-right"]')

    def assert_top_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.MENU, timeout=timeout)

    def assert_left_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.LEFT_MENU, timeout=timeout)

    def assert_right_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.RIGHT_MENU, timeout=timeout)
