from selenium.webdriver.common.by import By


class WebDriverToolKit:
    __driver = None

    @classmethod
    def add_driver(cls, driver):
        cls.__driver = driver

    @classmethod
    def open_site(cls, url: str):
        cls.__driver.get(url)

    @classmethod
    def find_element_by_text(cls, text):
        web_element = cls.__driver.find_element(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_element

    @classmethod
    def find_elements_by_text(cls, text):
        web_elements = cls.__driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}' )]")
        return web_elements

    @classmethod
    def find_element_by_tag_and_text(cls, tag, text):
        web_element = cls.__driver.find_element(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_element

    @classmethod
    def find_elements_by_tag_and_text(cls, tag, text):
        web_element = cls.__driver.find_elements(By.XPATH, f"//{tag}[contains(text(), '{text}' )]")
        return web_element
