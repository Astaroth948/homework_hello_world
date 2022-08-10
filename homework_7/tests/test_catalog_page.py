from selenium.webdriver.remote.webdriver import WebDriver

from homework_7.pages.catalog_page import CatalogPage
from homework_7.pages.elements.breadcrumbs import Breadcrumbs
from homework_7.pages.elements.header import Header
from homework_7.pages.elements.navigation_menu import NavigationMenu

CATALOG_PATH = 'index.php?route=product/category&language=en-gb&path=20'
PAGE_TITLE = "Desktops"


def test_catalog_page(driver: WebDriver) -> None:
    header = Header(driver)
    navigation_menu = NavigationMenu(driver)
    breadcrumbs = Breadcrumbs(driver)
    catalog_page = CatalogPage(driver)

    header._open(driver.url + CATALOG_PATH)
    header._wait_title_contain(text=PAGE_TITLE)
    header.assert_logo()
    header.assert_button_basket()
    header.assert_search_string()
    navigation_menu.assert_top_menu()
    breadcrumbs.assert_breadcrumbs()
    navigation_menu.assert_left_menu()
    catalog_page.assert_button_list_view()
    catalog_page.assert_button_grid_view()
    catalog_page.assert_select_sort()
    catalog_page.assert_select_show_limit()
