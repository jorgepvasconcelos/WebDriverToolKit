# selenium-toolkit

This library provides an easier way to use and interact with selenium driver. 

Features that currently selenium-toolkit can offer:

- ✅️ **More legible selenium code**
- ✅️ **Abstractions of selenium methods**
- ✅️ **Helpful tools to use when interacting with browsers**



## Install
```
pip install selenium-toolkit
```

## Basic
```python
from selenium.webdriver import Chrome
from selenium_toolkit import SeleniumToolKit

# Create chomedriver instance
driver = Chrome()

# Pass driver to SeleniumToolKit
selenium_kit = SeleniumToolKit(driver=driver)

# Use SeleniumToolKit to find a web element
web_element = selenium_kit.query_selector('.class1')

# With returned web_element use click() method
web_element.click()
```