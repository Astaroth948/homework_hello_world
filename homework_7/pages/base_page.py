from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from homework_7.tools import new_expected_conditions as NEC

import allure


class BasePage:
    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step('Открыть страницу {url}')
    def _open(self, url: str) -> None:
        self._driver.get(url)
        self._driver.logger.info(f'Open page "{url}"')

    @allure.step('Найти элемент {locator}')
    def _wait_element(self, locator: tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self._fail(f'Не найден элемент {locator}')

    @allure.step('Проверить, что заголовок страницы содержит "{text}"')
    def _wait_title_contain(self, text: str, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self._driver, timeout).until(EC.title_contains(text))
        except TimeoutException:
            self._fail(f'В заголовке страницы нет текста "{text}"')

    @allure.step('Найти элементы {locator}')
    def _find_elements(self, locator: tuple) -> list:
        return self._driver.find_elements(locator)

    @allure.step('Нажать на элемент {locator}')
    def _click(self, locator: tuple, timeout: int = 5) -> None:
        try:
            self._wait_element(locator=locator, timeout=timeout).click()
        except ElementClickInterceptedException:
            self._fail(f"Элемент {locator} перекрыт")

    @allure.step('Очистить поле ввода {locator}')
    def _clear_input(self, locator: tuple, timeout: int = 5) -> None:
        element = self._wait_element(locator=locator, timeout=timeout)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    @allure.step('Ввести текст "{text}" в элемент {locator}')
    def _input_text(self, locator: tuple, text: str, timeout: int = 5) -> None:
        self._clear_input(locator=locator, timeout=timeout)
        self._wait_element(locator=locator, timeout=timeout).send_keys(text)

    @allure.step('Проверить, что текст элемента {locator} равен "{text}"')
    def _assert_text_in_element_equal_to(self, locator: tuple, text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                NEC.text_in_element_equal_to(locator=locator, text_=text))
        except TimeoutException:
            self._fail(f'Текст элемента {locator} не равен "{text}"')

    @allure.step('Проверить, что текст "{text}" содержится в элементе {locator}')
    def _assert_text_in_element(self, locator: tuple, text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self._fail(f'В элементе {locator} нет вхождения текста "{text}"')

    @allure.step('Получить значение аттрибута "{attribute}" элемента {locator}')
    def _get_attribute(self, locator: tuple, attribute: str, timeout: int = 5) -> str:
        return self._wait_element(locator=locator, timeout=timeout).get_attribute(attribute)

    @allure.step('Дождаться и принять аллерт')
    def _accept_alert(self, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.alert_is_present()).accept()
        except TimeoutException:
            self._fail('Алерт не появился')
        self._driver.logger.info('Accept alert')

    @allure.step('Проверить, что количество элементов {locator} равно {quantity}')
    def _assert_quantity_of_elements(self, locator: tuple, quantity: int, timeout: int = 5) -> None:
        try:
            WebDriverWait(self._driver, timeout).until(
                NEC.quantity_of_elements(locator=locator, quantity=quantity))
        except TimeoutException:
            self._fail('Кол-во элементов {locator} не равно "{quantity}"')

    @allure.step('Обновить страницу')
    def _refresh_page(self) -> None:
        self._driver.refresh()
        self._driver.logger.info('Refresh page')

    def _fail(self, error_text: str) -> None:
        allure.attach(
            name=self._driver.session_id,
            body=self._driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        raise AssertionError(error_text)
