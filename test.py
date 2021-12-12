from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_toolkit import WebDriverToolKit

options = Options()
options.add_argument('--start-maximized')
driver = Chrome(options=options)

wtk = WebDriverToolKit(driver=driver)

driver.get('https://webscraper.io/test-sites/e-commerce/allinone/product/545')

if wtk.element_is_clickable(wait_time=20, locator=(By.CSS_SELECTOR, '[class="btn swatch disabled btn-primary"]')):
    print('é clicavel')
else:
    print('nao é clicavel')

driver.close()
