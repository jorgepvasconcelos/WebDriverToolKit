import traceback
from time import sleep
from random import uniform

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException
from selenium.webdriver.remote.webdriver import WebDriver


class WebDriverToolKit:
    def __init__(self, driver):
        self.__driver: WebDriver = driver

    def find_element_by_text(self, text: str):
        web_element = self.__driver.find_element(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_element

    def find_elements_by_text(self, text: str):
        web_elements = self.__driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_elements

    def find_element_by_tag_and_text(self, tag: str, text: str):
        web_element = self.__driver.find_element(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_element

    def find_elements_by_tag_and_text(self, tag: str, text: str):
        web_elements = self.__driver.find_elements(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_elements

    def fill(self, text: str, locator: tuple) -> None:
        element = self.__driver.find_element(*locator)
        element.send_keys(text)

    def fill_in_random_time(self, text: str, locator: tuple) -> None:
        element = self.__driver.find_element(*locator)
        for letter in text:
            time = uniform(0.3, 0.8)
            sleep(time)
            element.send_keys(letter)

    def clear_and_fill(self, text: str, locator: tuple, random_time=False) -> None:
        self.__driver.find_element(*locator).clear()
        if random_time:
            self.fill_in_random_time(text=text, locator=locator)
        else:
            self.fill(text=text, locator=locator)

    def element_is_present(self, wait_time: int, locator: tuple) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def element_is_visible(self, wait_time: int, locator: tuple) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def element_is_invisible(self, wait_time: int, locator: tuple) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def element_is_clickable(self, wait_time: int, locator: tuple) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def text_is_present(self, wait_time: int, locator: tuple, text: str) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.text_to_be_present_in_element(locator, text_=text))
            return True
        except TimeoutException:
            return False

    def alert_is_present(self, wait_time: int, message: str) -> bool:
        try:
            WebDriverWait(self.__driver, wait_time).until(EC.alert_is_present(), message=message)
            return True
        except TimeoutException:
            return False

    def page_is_loading(self) -> bool:
        if self.__driver.execute_script('return document.readyState') != 'complete':
            return True
        else:
            return False

    def block_urls(self, urls: list) -> None:
        self.__driver.execute_cdp_cmd('Network.setBlockedURLs', {'urls': urls})
        self.__driver.execute_cdp_cmd('Network.enable', {})

    def driver_hard_refresh(self):
        self.__driver.execute_script('location.reload(true)')

    def webdriver_is_open(self) -> bool:
        try:
            self.__driver.execute_script("console.log('ola eu estou funcionando');")
            return True
        except InvalidSessionIdException:
            return False
