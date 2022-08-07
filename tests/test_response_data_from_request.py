import time

from selenium.webdriver import Chrome, DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium_toolkit import SeleniumToolKit


options = Options()
options.add_argument('--start-maximized')

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

driver = Chrome(executable_path="../chromedriver.exe", options=options, desired_capabilities=capabilities)

wtk = SeleniumToolKit(driver=driver)

driver.get("https://pizzeriacaliari.menudino.com/")
time.sleep(5)


a = wtk.response_data_from_request(url='https://pizzeriacaliari.menudino.com/pedido/carrinho')

print(a)


driver.close()
