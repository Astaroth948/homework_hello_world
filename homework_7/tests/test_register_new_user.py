from selenium.webdriver.remote.webdriver import WebDriver
import allure

from homework_7.pages.admin_page import AdminPage
from homework_7.pages.elements.admin_menu import AdminMenu
from homework_7.pages.login_admin_page import LoginAdminPage
from homework_7.pages.register_page import RegisterPage

REGISTER_PATH = 'index.php?route=account/register'
LOGIN_ADMIN_PATH = 'admin/'


@allure.parent_suite('Проверки страницы регистрации пользователя')
@allure.epic('Проверки страницы регистрации пользователя')
@allure.title('Проверка регистрации и удаления нового пользователя')
def test_register_new_user(driver: WebDriver) -> None:
    register_page = RegisterPage(driver)
    login_admin_page = LoginAdminPage(driver)
    admin_menu = AdminMenu(driver)
    admin_page = AdminPage(driver)

    register_page._open(driver.url + REGISTER_PATH)
    register_page.input_text_in_field(field_name='First Name', text='Ivan')
    register_page.input_text_in_field(field_name='Last Name', text='Ivanov')
    register_page.input_text_in_field(field_name='E-Mail', text='ivan@qwe.qwe')
    register_page.input_text_in_field(field_name='Telephone', text='+7656555')
    register_page.input_text_in_field(
        field_name='Password', text='Password123')
    register_page.input_text_in_field(
        field_name='Password Confirm', text='Password123')
    register_page.select_subscribe(subscribe=True)
    register_page.select_agree_privacy_policy(agree=True)
    register_page.click_button_continue()
    register_page.assert_title_success_create_user()

    login_admin_page._open(driver.url + LOGIN_ADMIN_PATH)
    login_admin_page.input_text_in_field(field_name='Username', text='user')
    login_admin_page.input_text_in_field(field_name='Password', text='bitnami')
    login_admin_page.click_button_login()

    admin_menu.goto_customers_list()
    admin_page.assert_quantity_rows(quantity=1)
    admin_page.click_checkbox_select_all()
    admin_page.click_button_delete_all()
    admin_page._accept_alert()
    admin_page.assert_text_in_success_alert(
        text='Success: You have modified customers!')
    admin_page.assert_quantity_rows(quantity=0)
