class WebDriverToolKit:
    __driver = None

    @classmethod
    def add_driver(cls, driver):
        cls.__driver = driver

    @classmethod
    def open_site(cls, url: str):
        cls.__driver.get(url)
