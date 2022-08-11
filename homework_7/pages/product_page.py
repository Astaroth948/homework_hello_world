from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class ProductPage(BasePage):
    PRODUCT_IMAGES = (By.XPATH, '//ul[@class="thumbnails"]')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="col-sm-4"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-4"]//h2')
    BUTTON_ADD_TO_CART = (By.XPATH, '//button[@id="button-cart"]')

    @allure.step('Проверить, что на странице есть изображения товара')
    def assert_product_images(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.PRODUCT_IMAGES, timeout=timeout)
        self._driver.logger.info('Assert product images')

    @allure.step('Проверить, что на странице есть заголовок товара')
    def assert_product_title(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.PRODUCT_TITLE, timeout=timeout)
        self._driver.logger.info('Assert product title')

    @allure.step('Проверить, что на странице есть цена товара')
    def assert_product_price(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.PRODUCT_PRICE, timeout=timeout)
        self._driver.logger.info('Assert product price')

    @allure.step('Проверить, что на странице есть кнопка "Add to Cart"')
    def assert_button_add_to_cart(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_ADD_TO_CART, timeout=timeout)
        self._driver.logger.info('Assert "Add to Cart" button')
