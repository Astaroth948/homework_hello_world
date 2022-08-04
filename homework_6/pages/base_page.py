from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from homework_6.tools import new_expected_conditions as NEC


class BasePage:
    def __init__(self, driver) -> None:
        self._driver = driver

    def _open(self, url: str) -> None:
        self._driver.get(url)

    def _wait_element(self, locator: tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Не найден элемент {locator}')

    def _wait_title_contain(self, text: str, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout).until(EC.title_contains(text))
        except TimeoutException:
            raise AssertionError(f'В заголовке страницы нет текста "{text}"')

    def _find_elements(self, locator: tuple) -> list:
        return self._driver.find_elements(locator)

    def _click(self, locator: tuple, timeout: int = 5) -> None:
        try:
            self._wait_element(locator=locator, timeout=timeout).click()
        except ElementClickInterceptedException:
            raise AssertionError(f"Элемент {locator} перекрыт")

    def _clear_input(self, locator: tuple, timeout: int = 5) -> None:
        element = self._wait_element(locator=locator, timeout=timeout)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def _input_text(self, locator: tuple, text: str, timeout: int = 5) -> None:
        self._clear_input(locator=locator, timeout=timeout)
        self._wait_element(locator=locator, timeout=timeout).send_keys(text)

    def _assert_text_in_element_equal_to(self, locator: tuple, text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                NEC.text_in_element_equal_to(locator=locator, text_=text))
        except TimeoutException:
            raise AssertionError(f'Текст элемента {locator} не равен "{text}"')

    def _assert_text_in_element(self, locator: tuple, text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError(
                f'В элементе {locator} нет вхождения текста "{text}"')

    def _get_attribute(self, locator: tuple, attribute: str, timeout: int = 5) -> str:
        return self._wait_element(locator=locator, timeout=timeout).get_attribute(attribute)

    def _accept_alert(self, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.alert_is_present()).accept()
        except TimeoutException:
            raise AssertionError('Алерт не появился')

    def _assert_quantity_of_elements(self, locator: tuple, quantity: int, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                NEC.quantity_of_elements(locator=locator, quantity=quantity))
        except TimeoutException:
            raise AssertionError(
                f'Кол-во элементов {locator} не равно "{quantity}"')

    def _refresh_page(self) -> None:
        self._driver.refresh()
