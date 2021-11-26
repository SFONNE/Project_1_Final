# Yacine BOUSLAHI
from time import sleep

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('utilisateur fbk')
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('mot de passe')
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("facebook opened")

print('go to AXA page')

driver.get('https://www.facebook.com/monaxa/')

commentaires = driver.find_elements_by_xpath(
    "//div [@data-testid='UFI2Comment/body']")


print('nombre de commentaires trouvés :', str(len(x)))

for com in commentaires:
    print(com.text)
