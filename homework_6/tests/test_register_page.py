from selenium.webdriver.remote.webdriver import WebDriver

from homework_6.pages.elements.breadcrumbs import Breadcrumbs
from homework_6.pages.elements.header import Header
from homework_6.pages.elements.navigation_menu import NavigationMenu
from homework_6.pages.register_page import RegisterPage

REGISTER_PATH = 'index.php?route=account/register'
PAGE_TITLE = "Register Account"


def test_register_page(driver: WebDriver) -> None:
    header = Header(driver)
    navigation_menu = NavigationMenu(driver)
    breadcrumbs = Breadcrumbs(driver)
    register_page = RegisterPage(driver)

    header._open(driver.url + REGISTER_PATH)
    header._wait_title_contain(text=PAGE_TITLE)
    header.assert_logo()
    header.assert_button_basket()
    header.assert_search_string()
    navigation_menu.assert_top_menu()
    navigation_menu.assert_right_menu()
    breadcrumbs.assert_breadcrumbs()
    register_page.assert_input_field(field_name='First Name')
    register_page.assert_input_field(field_name='Last Name')
    register_page.assert_input_field(field_name='E-Mail')
    register_page.assert_input_field(field_name='Telephone')
    register_page.assert_input_field(field_name='Password')
    register_page.assert_input_field(field_name='Password Confirm')
