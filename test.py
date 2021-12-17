import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_toolkit import WebDriverToolKit

options = Options()
options.add_argument('--start-maximized')
driver = Chrome(options=options)

wtk = WebDriverToolKit(driver=driver)

driver.get('https://webscraper.io/test-sites/e-commerce/allinone/product/545')


time.sleep(2)
driver.close()

if wtk.webdriver_is_open():
    print('esta aberto')
else:
    print('esta fechado')