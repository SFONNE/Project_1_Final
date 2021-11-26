from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
usernam = str(input('Enter your Username OR ID'))
password = str(input('Enter your password'))
frndId = str('104244495036936')
mesage = str(input('Enter your text message here: '))
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.facebook.com/')
driver.find_element_by_id("email").send_keys(usernam)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name("login").click()  # I click login button
sleep(1)
mesagAdd = 'https://www.facebook.com/messages/t/'
mesagLink = mesagAdd+frndId
driver.get(mesagLink)
driver.implicitly_wait(20)
driver.find_element_by_xpath('//div[@class="_1mf _1mj"]').send_keys(mesage, Keys.ENTER)
sleep(0.3)