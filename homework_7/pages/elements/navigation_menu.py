from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class NavigationMenu(BasePage):
    MENU = (By.XPATH, '//ul[@class="nav navbar-nav"]')
    LEFT_MENU = (By.XPATH, '//aside[@id="column-left"]')
    RIGHT_MENU = (By.XPATH, '//aside[@id="column-right"]')

    @allure.step('Проверить, что на странице есть горизонтальное меню навигации')
    def assert_top_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.MENU, timeout=timeout)
        self._driver.logger.info('Assert horizontal navigation menu')

    @allure.step('Проверить, что на странице есть левое вертикальное меню навигации')
    def assert_left_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.LEFT_MENU, timeout=timeout)
        self._driver.logger.info('Assert left vertical navigation menu')

    @allure.step('Проверить, что на странице есть правое вертикальное меню навигации')
    def assert_right_menu(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.RIGHT_MENU, timeout=timeout)
        self._driver.logger.info('Assert right vertical navigation menu')
