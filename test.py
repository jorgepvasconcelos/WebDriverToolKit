from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from webdriver_toolkit import WebDriverToolKit

driver = Chrome()

wtk = WebDriverToolKit(driver=driver)

wtk.open_site(url='https://www.google.com/')
