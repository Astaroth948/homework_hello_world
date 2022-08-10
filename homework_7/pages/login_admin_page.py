from selenium.webdriver.common.by import By
from homework_7.pages.base_page import BasePage


class LoginAdminPage(BasePage):
    LOGO = (By.XPATH, '//header//img')
    FORM_HEADER = (By.XPATH, '//div[@class="panel-heading"]')
    INPUT_FIELD = (
        By.XPATH, '//label[text()="field-&"]/following-sibling::div/input')
    BUTTON_FORGOTTEN_PASSWORD = (By.XPATH, '//a[text()="Forgotten Password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@type="submit"]')

    def assert_logo(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.LOGO, timeout=timeout)

    def assert_form_header(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.FORM_HEADER, timeout=timeout)

    def assert_input_field(self, field_name: str, timeout: int = 5) -> None:
        self._wait_element(locator=(self.INPUT_FIELD[0], self.INPUT_FIELD[1].replace(
            'field-&', field_name)), timeout=timeout)

    def input_text_in_field(self, field_name: str, text: str, timeout: int = 5) -> None:
        self._input_text(locator=(self.INPUT_FIELD[0], self.INPUT_FIELD[1].replace(
            'field-&', field_name)), text=text, timeout=timeout)

    def assert_button_forgotten_password(self, timeout: int = 5) -> None:
        self._wait_element(
            locator=self.BUTTON_FORGOTTEN_PASSWORD, timeout=timeout)

    def assert_button_login(self, timeout: int = 5) -> None:
        self._wait_element(locator=self.BUTTON_LOGIN, timeout=timeout)

    def click_button_login(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_LOGIN, timeout=timeout)
