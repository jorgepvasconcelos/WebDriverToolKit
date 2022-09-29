import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium_toolkit import SeleniumToolKit
from selenium_toolkit.auto_wait import AutoWait


def test_AutoWait():
    AutoWait.change_wait_time(times=1)

    options = Options()
    options.add_argument('--start-maximized')
    driver = Chrome(executable_path='../chromedriver.exe', options=options)

    sk = SeleniumToolKit(driver=driver)

    sk.goto('https://webscraper.io/test-sites/e-commerce/allinone/product/545')

    AutoWait.change_wait_time(times=5)

    sk.goto('https://webscraper.io/test-sites/e-commerce/allinone/product/544')

    assert True
