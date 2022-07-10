import json
import traceback
import time
from random import uniform
from typing import Union

from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class SeleniumToolKit:
    def __init__(self, driver):
        self.__driver: Union[WebDriver, ChromiumDriver] = driver

    @property
    def driver(self) -> Union[WebDriver, ChromiumDriver]:
        return self.__driver

    def goto(self, url: str, wait_time: Union[int, float] = 0) -> None:
        if wait_time:
            time.sleep(wait_time)
        self.__driver.get(url=url)

    def query_selector(self, query_selector: str) -> Union[WebElement, None]:
        if not query_selector:
            raise ValueError('You need send a query_selector')

        if query_selector[0] == '/':
            web_element = self.__driver.find_element(By.XPATH, query_selector)
        else:
            web_element = self.__driver.find_element(By.CSS_SELECTOR, query_selector)

        return web_element

    def query_selector_all(self, query_selector: str) -> Union[list[WebElement], None]:
        if not query_selector:
            raise ValueError('You need send a query_selector')

        if query_selector[0] == '/':
            web_elements = self.__driver.find_elements(By.XPATH, query_selector)
        else:
            web_elements = self.__driver.find_elements(By.CSS_SELECTOR, query_selector)

        return web_elements

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

    def get_text(self, locator: tuple) -> str:
        try:
            return self.__driver.find_element(*locator).text
        except NoSuchElementException as e:
            raise e

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        try:
            return self.__driver.find_element(*locator).get_attribute(attribute)
        except NoSuchElementException as e:
            raise e

    def click(self, locator: tuple) -> None:
        self.__driver.find_element(*locator).click()

    def fill(self, text: str, locator: tuple) -> None:
        element = self.__driver.find_element(*locator)
        element.send_keys(text)

    def fill_in_random_time(self, text: str, locator: tuple) -> None:
        element = self.__driver.find_element(*locator)
        for letter in text:
            time.sleep(uniform(0.3, 0.8))
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
        if not isinstance(self.__driver, ChromiumDriver):
            TypeError("Your driver must be a ChromiumDriver type to use this method")

        self.__driver.execute_cdp_cmd('Network.setBlockedURLs', {'urls': urls})
        self.__driver.execute_cdp_cmd('Network.enable', {})

    def driver_hard_refresh(self) -> None:
        self.__driver.execute_script('location.reload(true)')

    def webdriver_is_open(self) -> bool:
        try:
            self.__driver.execute_script("console.log('ola eu estou funcionando');")
            return True
        except InvalidSessionIdException:
            return False

    def response_data_from_request(self, url: str) -> list:
        if not isinstance(self.__driver, ChromiumDriver):
            TypeError("Your driver must be a ChromiumDriver type to use this method")

        logs_raw = self.__driver.get_log("performance")
        parsed_logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

        received_response_list = [response for response in parsed_logs
                                  if response["method"] == "Network.responseReceived"]

        response_list = []
        for response in received_response_list:
            request_id = response["params"]["requestId"]
            resp_url = response["params"]["response"]["url"]

            if resp_url == url:
                response_body = self.__driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                response_list.append(response_body)

        return response_list
