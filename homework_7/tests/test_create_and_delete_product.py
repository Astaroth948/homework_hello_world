from selenium.webdriver.remote.webdriver import WebDriver

from homework_7.pages.admin_page import AdminPage
from homework_7.pages.elements.admin_filter_product import AdminFilterProduct
from homework_7.pages.elements.admin_menu import AdminMenu
from homework_7.pages.login_admin_page import LoginAdminPage

LOGIN_ADMIN_PATH = 'admin/'


def test_create_and_delete_product(driver: WebDriver) -> None:
    login_admin_page = LoginAdminPage(driver)
    admin_menu = AdminMenu(driver)
    admin_page = AdminPage(driver)
    admin_filter_product = AdminFilterProduct(driver)

    login_admin_page._open(driver.url + LOGIN_ADMIN_PATH)
    login_admin_page.input_text_in_field(field_name='Username', text='user')
    login_admin_page.input_text_in_field(field_name='Password', text='bitnami')
    login_admin_page.click_button_login()

    admin_menu.goto_products_list()
    admin_page.click_button_add_new()
    admin_page.input_text_in_field(
        field_name='Product Name', text='TestProduct')
    admin_page.input_text_in_field(
        field_name='Meta Tag Title', text='TestProductTag')
    admin_page.switch_tabs(tab_name='Data')
    admin_page.input_text_in_field(field_name='Model', text='TestModel')
    admin_page.switch_tabs(tab_name='Links')
    admin_page.input_text_in_autocomplete_field(
        field_name='Categories', text='PC')
    admin_page.click_button_save()
    admin_page.assert_text_in_success_alert(
        text='Success: You have modified products!')
    admin_page._refresh_page()

    admin_filter_product.input_text_in_autocomplete_field(
        field_name='Product Name', text='Test')
    admin_filter_product.click_button_filter()
    admin_page.assert_quantity_rows(quantity=1)
    admin_page.click_checkbox_select_all()
    admin_page.click_button_delete_all()
    admin_page._accept_alert()
    admin_page.assert_text_in_success_alert(
        text='Success: You have modified products!')
    admin_page.assert_quantity_rows(quantity=0)
