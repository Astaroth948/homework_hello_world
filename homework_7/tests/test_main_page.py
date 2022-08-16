from selenium.webdriver.remote.webdriver import WebDriver
import allure

from homework_7.pages.main_page import MainPage
from homework_7.pages.elements.header import Header
from homework_7.pages.elements.navigation_menu import NavigationMenu

PAGE_TITLE = "Your Store"


@allure.parent_suite('Проверки главной страницы')
@allure.epic('Проверки главной страницы')
@allure.title('Проверка наличия основных элементов страницы')
def test_main_page(driver: WebDriver) -> None:
    header = Header(driver)
    navigation_menu = NavigationMenu(driver)
    main_page = MainPage(driver)

    header._open(driver.url)
    header._wait_title_contain(text=PAGE_TITLE)
    header.assert_logo()
    header.assert_button_basket()
    header.assert_search_string()
    navigation_menu.assert_top_menu()
    main_page.assert_top_carousel()
    main_page.assert_bottom_carousel()
