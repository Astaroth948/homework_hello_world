from selenium.webdriver.remote.webdriver import WebDriver

from homework_6.pages.elements.breadcrumbs import Breadcrumbs
from homework_6.pages.elements.header import Header
from homework_6.pages.elements.navigation_menu import NavigationMenu
from homework_6.pages.product_page import ProductPage

PRODUCT_PATH = 'index.php?route=product/product&product_id=43'
PAGE_TITLE = "MacBook"


def test_product_page(driver: WebDriver) -> None:
    header = Header(driver)
    navigation_menu = NavigationMenu(driver)
    breadcrumbs = Breadcrumbs(driver)
    product_page = ProductPage(driver)

    header._open(driver.url + PRODUCT_PATH)
    header._wait_title_contain(text=PAGE_TITLE)
    header.assert_logo()
    header.assert_button_basket()
    header.assert_search_string()
    navigation_menu.assert_top_menu()
    breadcrumbs.assert_breadcrumbs()
    product_page.assert_product_images()
    product_page.assert_product_title()
    product_page.assert_product_price()
    product_page.assert_button_add_to_cart()
