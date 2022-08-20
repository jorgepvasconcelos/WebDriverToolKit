import time

from selenium.webdriver import Chrome, DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium_toolkit import SeleniumToolKit


def test_element_is_present():
    options = Options()
    options.add_argument('--start-maximized')

    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = Chrome(options=options, desired_capabilities=capabilities)

    wtk = SeleniumToolKit(driver=driver)

    driver.get("https://pizzeriacaliari.menudino.com/")
    time.sleep(5)

    value = wtk.response_data_from_request(url='https://pizzeriacaliari.menudino.com/pedido/carrinho')
    driver.close()

    assert value

