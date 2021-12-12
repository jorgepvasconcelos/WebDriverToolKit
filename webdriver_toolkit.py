from selenium.webdriver.common.by import By


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
        web_element = self.__driver.find_elements(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_element
