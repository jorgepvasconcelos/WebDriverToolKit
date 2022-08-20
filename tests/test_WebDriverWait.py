import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium_toolkit import SeleniumToolKit


def test_element_is_present():
    options = Options()
    driver = Chrome(options=options)

    sk = SeleniumToolKit(driver=driver)

    sk.goto('https://webscraper.io/test-sites/e-commerce/allinone/product/545')
    sk.element_is_present(wait_time=5, query_selector='[class="pull-right price"]')

    driver.close()
