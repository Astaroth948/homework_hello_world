from selenium.webdriver.common.by import By
from homework_6.pages.base_page import BasePage


class MainPage(BasePage):
    TOP_CAROUSEL = (By.XPATH, '//div[@id="slideshow0"]')
    BOTTOM_CAROUSEL = (By.XPATH, '//div[@id="carousel0"]')

    def assert_top_carousel(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.TOP_CAROUSEL, timeout=timeout)

    def assert_bottom_carousel(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BOTTOM_CAROUSEL, timeout=timeout)
