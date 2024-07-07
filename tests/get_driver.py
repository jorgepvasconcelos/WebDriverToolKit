from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium_toolkit import SeleniumToolKit


def get_latest_chrome_driver_path() -> str:
    latest_driver_path = ChromeDriverManager().install()
    return latest_driver_path


def get_selenium_toolkit() -> SeleniumToolKit:
    options = Options()
    options.add_argument('--start-maximized')

    capabilities = {"performance": "ALL"}
    options.set_capability("goog:loggingPrefs", capabilities)

    executable_path = get_latest_chrome_driver_path()
    driver = webdriver.Chrome(options=options,
                              service=Service(executable_path=executable_path))

    stk = SeleniumToolKit(driver=driver)
    return stk
