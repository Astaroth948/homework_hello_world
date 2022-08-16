from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class MainPage(BasePage):
    TOP_CAROUSEL = (By.XPATH, '//div[@id="slideshow0"]')
    BOTTOM_CAROUSEL = (By.XPATH, '//div[@id="carousel0"]')

    @allure.step('Проверить, что на странице есть верхняя карусель')
    def assert_top_carousel(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.TOP_CAROUSEL, timeout=timeout)
        self._driver.logger.info('Assert top carousel')

    @allure.step('Проверить, что на странице есть нижняя карусель')
    def assert_bottom_carousel(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BOTTOM_CAROUSEL, timeout=timeout)
        self._driver.logger.info('Assert bottom carousel')
