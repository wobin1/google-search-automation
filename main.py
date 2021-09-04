from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.quora.com/')

emailField = driver.find_element_by_xpath('//*[@id="email"]')
emailField.send_keys('crixadsinfo@gmail.com')

passwordField = driver.find_element_by_xpath('//*[@id="password"]')
passwordField.send_keys('fakepassword')


button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button/div/div/div')

button.click()

