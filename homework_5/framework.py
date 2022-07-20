from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_element(driver, locator: tuple, timeout: int = 5) -> WebElement:
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f'Не найден элемент {locator}')


def wait_title_contain(driver, text: str, timeout: int = 5) -> WebElement:
    try:
        return WebDriverWait(driver, timeout).until(EC.title_contains(text))
    except TimeoutException:
        raise AssertionError(f'В заголовке страницы нет текста "{text}"')
