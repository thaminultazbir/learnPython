from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.add_

driver.implicitly_wait(10)

user_input_field = driver.find_element(By.ID, "email")
user_input_field.send_keys("kalilinux157@gmail.com")
password_input_field = driver.find_element(By.ID, "pass")
password_input_field.send_keys("asdjfhfjg")



input("Press Enter to close the browser...")
driver.quit()