from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage


class CatalogPage(BasePage):
    BUTTON_LIST_VIEW = (By.XPATH, '//button[@id="list-view"]')
    BUTTON_GRID_VIEW = (By.XPATH, '//button[@id="grid-view"]')
    SELECT_SORT = (By.XPATH, '//select[@id="input-sort"]')
    SELECT_SHOW_LIMIT = (By.XPATH, '//select[@id="input-limit"]')

    def assert_button_list_view(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_LIST_VIEW, timeout=timeout)

    def assert_button_grid_view(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_GRID_VIEW, timeout=timeout)

    def assert_select_sort(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.SELECT_SORT, timeout=timeout)

    def assert_select_show_limit(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.SELECT_SHOW_LIMIT, timeout=timeout)
