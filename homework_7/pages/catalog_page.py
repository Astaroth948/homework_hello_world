from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class CatalogPage(BasePage):
    BUTTON_LIST_VIEW = (By.XPATH, '//button[@id="list-view"]')
    BUTTON_GRID_VIEW = (By.XPATH, '//button[@id="grid-view"]')
    SELECT_SORT = (By.XPATH, '//select[@id="input-sort"]')
    SELECT_SHOW_LIMIT = (By.XPATH, '//select[@id="input-limit"]')

    @allure.step('Проверить, что на странице есть кнопка отображения товаров "List"')
    def assert_button_list_view(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_LIST_VIEW, timeout=timeout)
        self._driver.logger.info('Assert "List" button')

    @allure.step('Проверить, что на странице есть кнопка отображения товаров "Grid"')
    def assert_button_grid_view(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_GRID_VIEW, timeout=timeout)
        self._driver.logger.info('Assert "Grid" button')

    @allure.step('Проверить, что на странице есть элемент select для сортировки товаров')
    def assert_select_sort(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.SELECT_SORT, timeout=timeout)
        self._driver.logger.info('Assert "Sort" select')

    @allure.step('Проверить, что на странице есть элемент select для отображения количества товаров')
    def assert_select_show_limit(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.SELECT_SHOW_LIMIT, timeout=timeout)
        self._driver.logger.info('Assert "Show limit" select')
