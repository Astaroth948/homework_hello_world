from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage

import allure


class AdminFilterProduct(BasePage):
    INPUT_AUTOCOMPLETE_FIELD = (
        By.XPATH, '//label[text()="field-&"]/following-sibling::input')
    SELECT_AUTOCOMPLETE_OPTION = (
        By.XPATH, '//ul[@class="dropdown-menu"]/li/a[contains(text(), "text-&")]')
    BUTTON_FILTER = (By.XPATH, '//button[@id="button-filter"]')

    @allure.step('Ввести "{text}" в поле с автозаполнением "{field_name}"')
    def input_text_in_autocomplete_field(self, field_name: str, text: str, timeout: int = 5) -> None:
        self._input_text(locator=(self.INPUT_AUTOCOMPLETE_FIELD[0], self.INPUT_AUTOCOMPLETE_FIELD[1].replace(
            'field-&', field_name)), text=text, timeout=timeout)
        self._click(locator=(self.SELECT_AUTOCOMPLETE_OPTION[0], self.SELECT_AUTOCOMPLETE_OPTION[1].replace(
            'text-&', text)), timeout=timeout)
        self._driver.logger.info(
            f'Input "{text}" in the autocomplete field "{field_name}"')

    @allure.step('Нажать на кнопку "Filter"')
    def click_button_filter(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_FILTER, timeout=timeout)
        self._driver.logger.info('Click on the "Filter" button')
