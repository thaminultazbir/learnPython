from incog import driver
from Find_Element import findElemnt

driver.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier')
driver.implicitly_wait(10)

# btn_click = findElemnt('/html/body/header/div/div/div/a[2]')
# btn_click.click()
# driver.implicitly_wait(10)

mail_input_field = findElemnt('//*[@id="identifierId"]')
mail_input_field.send_keys('rangs.tazbir@gmail.com')
driver.implicitly_wait(5)

next_button = findElemnt('//*[@id="identifierNext"]/div/button/span')
next_button.click()
driver.implicitly_wait(5)


input("Press Enter to close the browser...")
driver.quit()