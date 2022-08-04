from selenium.webdriver.remote.webdriver import WebDriver

from homework_6.pages.login_admin_page import LoginAdminPage

LOGIN_ADMIN_PATH = 'admin/'
PAGE_TITLE = "Administration"


def test_login_admin_page(driver: WebDriver) -> None:
    login_admin_page = LoginAdminPage(driver)

    login_admin_page._open(driver.url + LOGIN_ADMIN_PATH)
    login_admin_page._wait_title_contain(text=PAGE_TITLE)
    login_admin_page.assert_logo()
    login_admin_page.assert_form_header()
    login_admin_page.assert_input_field(field_name='Username')
    login_admin_page.assert_input_field(field_name='Password')
    login_admin_page.assert_button_forgotten_password()
    login_admin_page.assert_button_login()
