from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


