from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class RegisterPage(BasePage):
    INPUT_FIELD = (
        By.XPATH, '//label[text()="field-&"]/following-sibling::div/input')
    BUTTON_CONTINUE = (By.XPATH, '//input[@type="submit"]')
    RADIO_SUBSCRIBE_YES = (
        By.XPATH, '//input[@name="newsletter" and @value="1"]')
    RADIO_SUBSCRIBE_NO = (
        By.XPATH, '//input[@name="newsletter" and @value="0"]')
    CHECKBOX_PRIVACY_POLICY = (By.XPATH, '//input[@name="agree"]')
    TITLE_SUCCESS_CREATE_USER = (
        By.XPATH, '//div[@id="content"]/h1[text()="Your Account Has Been Created!"]')

    @allure.step('Проверить, что на странице есть поле ввода "{field_name}"')
    def assert_input_field(self, field_name: str, timeout: int = 5) -> None:
        self._wait_element(locator=(self.INPUT_FIELD[0], self.INPUT_FIELD[1].replace(
            'field-&', field_name)), timeout=timeout)
        self._driver.logger.info(f'Assert text field "{field_name}"')

    @allure.step('Ввести "{text}" в текстовое поле "{field_name}"')
    def input_text_in_field(self, field_name: str, text: str, timeout: int = 5) -> None:
        self._input_text(locator=(self.INPUT_FIELD[0], self.INPUT_FIELD[1].replace(
            'field-&', field_name)), text=text, timeout=timeout)
        self._driver.logger.info(
            f'Input "{text}" in the text field "{field_name}"')

    @allure.step('Проверить, что на странице есть кнопка "Continue"')
    def assert_button_continue(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_CONTINUE, timeout=timeout)
        self._driver.logger.info('Assert "Continue" button')

    @allure.step('Нажать на кнопку "Continue"')
    def click_button_continue(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_CONTINUE, timeout=timeout)
        self._driver.logger.info('Click on the "Continue" button')

    @allure.step('Выставить радиокнопки "Subscribe" в положение {subscribe}')
    def select_subscribe(self, subscribe: bool = False, timeout: int = 5) -> None:
        if subscribe:
            self._click(locator=self.RADIO_SUBSCRIBE_YES, timeout=timeout)
        else:
            self._click(locator=self.RADIO_SUBSCRIBE_NO, timeout=timeout)
        self._driver.logger.info(
            f'Set the "Subscribe" radio buttons to {subscribe}')

    @allure.step('Выставить чекбокс "I have read and agree to the Privacy Policy" в положение {agree}')
    def select_agree_privacy_policy(self, agree: bool = True, timeout: int = 5) -> None:
        if agree:
            self._click(locator=self.CHECKBOX_PRIVACY_POLICY, timeout=timeout)
        self._driver.logger.info(
            f'Set a checkbox "I have read and agree to the Privacy Policy" to "{agree}"')

    @allure.step('Проверить, что на странице появился заголовок "Your Account Has Been Created!"')
    def assert_title_success_create_user(self, timeout: int = 5):
        self._wait_element(
            locator=self.TITLE_SUCCESS_CREATE_USER, timeout=timeout)
        self._driver.logger.info(
            'Assert title "Your Account Has Been Created!"')
