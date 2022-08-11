from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class Breadcrumbs(BasePage):
    BREADCRUMBS = (By.XPATH, '//ul[@class="breadcrumb"]')

    @allure.step('Проверить что на странице есть элемент breadcrumb')
    def assert_breadcrumbs(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BREADCRUMBS, timeout=timeout)
        self._driver.logger.info('Assert "breadcrumb" element')
