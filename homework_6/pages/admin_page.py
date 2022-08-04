from selenium.webdriver.common.by import By
from homework_6.pages.base_page import BasePage


class AdminPage(BasePage):
    CHECKBOX_SELECT_ALL = (By.XPATH, '//thead//input')
    BUTTON_DELETE_ALL = (By.XPATH, '//button[@data-original-title="Delete"]')
    BUTTON_ADD_NEW = (By.XPATH, '//a[@data-original-title="Add New"]')
    BUTTON_SAVE = (By.XPATH, '//button[@data-original-title="Save"]')
    SUCCESS_ALERT = (
        By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
    TABLE_ROWS = (By.XPATH, '//tbody/tr//input')
    TABLE_EMPTY_ROW = (By.XPATH, '//tbody/tr/td[text()="No results!"]')
    INPUT_FIELD = (
        By.XPATH, '//label[text()="field-&"]/following-sibling::div/input')
    INPUT_AUTOCOMPLETE_FIELD = (
        By.XPATH, '//span[text()="field-&"]/parent::label/following-sibling::div/input')
    SELECT_AUTOCOMPLETE_OPTION = (
        By.XPATH, '//ul[@class="dropdown-menu"]/li/a[contains(text(), "text-&")]')
    SELECT_TAB = (By.XPATH, '//a[@data-toggle="tab" and text()="tab-&"]')

    def click_checkbox_select_all(self, timeout: int = 5) -> None:
        self._click(locator=self.CHECKBOX_SELECT_ALL, timeout=timeout)

    def click_button_delete_all(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_DELETE_ALL, timeout=timeout)

    def assert_text_in_success_alert(self, text: str, timeout: int = 5) -> None:
        self._assert_text_in_element(
            locator=self.SUCCESS_ALERT, text=text, timeout=timeout)

    def click_button_add_new(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_ADD_NEW, timeout=timeout)

    def click_button_add_new(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_ADD_NEW, timeout=timeout)

    def click_button_save(self, timeout: int = 5) -> None:
        self._click(locator=self.BUTTON_SAVE, timeout=timeout)

    def input_text_in_field(self, field_name: str, text: str, timeout: int = 5) -> None:
        self._input_text(locator=(self.INPUT_FIELD[0], self.INPUT_FIELD[1].replace(
            'field-&', field_name)), text=text, timeout=timeout)

    def input_text_in_autocomplete_field(self, field_name: str, text: str, timeout: int = 5) -> None:
        self._input_text(locator=(self.INPUT_AUTOCOMPLETE_FIELD[0], self.INPUT_AUTOCOMPLETE_FIELD[1].replace(
            'field-&', field_name)), text=text, timeout=timeout)
        self._click(locator=(self.SELECT_AUTOCOMPLETE_OPTION[0], self.SELECT_AUTOCOMPLETE_OPTION[1].replace(
            'text-&', text)), timeout=timeout)

    def switch_tabs(self, tab_name: str, timeout: int = 5) -> None:
        self._click(locator=(self.SELECT_TAB[0], self.SELECT_TAB[1].replace(
            'tab-&', tab_name)), timeout=timeout)

    def assert_quantity_rows(self, quantity: int, timeout: int = 5) -> None:
        self._assert_quantity_of_elements(
            locator=self.TABLE_ROWS, quantity=quantity, timeout=timeout)
        if quantity == 0:
            self._wait_element(locator=self.TABLE_EMPTY_ROW, timeout=timeout)
