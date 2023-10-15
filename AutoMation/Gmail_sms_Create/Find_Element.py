from incog import driver
from selenium.webdriver.common.by import By


def findElemnt(xpath):
    return driver.find_element(By.XPATH,xpath)
