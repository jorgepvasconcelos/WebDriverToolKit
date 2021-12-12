import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class WebDriverToolKit:
    def __init__(self, driver):
        self.__driver = driver

    def add_driver(self, driver):
        self.__driver = driver

    def open_site(self, url: str):
        self.__driver.get(url)

    def find_element_by_text(self, text):
        web_element = self.__driver.find_element(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_element

    def find_elements_by_text(self, text):
        web_elements = self.__driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_elements

    def find_element_by_tag_and_text(self, tag, text):
        web_element = self.__driver.find_element(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_element

    def find_elements_by_tag_and_text(self, tag, text):
        web_elements = self.__driver.find_elements(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_elements

    def element_is_clickable(self, wait_time, locator: tuple):
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
