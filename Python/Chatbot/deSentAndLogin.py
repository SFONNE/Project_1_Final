from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from tkinter import *
from functools import partial
from tkinter.ttk import *
from tkinter import messagebox

def validateLogin(username, password, Tess):
 
    usernam = str(username.get())
    pasword = str(password.get())
    frandId = str('104244495036936')
    mmesage = str(Tess.get())
    print(username)
    print(password)
    print(Tess)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    driver.find_element_by_id("email").send_keys(usernam)
    driver.find_element_by_id('pass').send_keys(pasword)
    driver.find_element_by_name("login").click()  # I click login button
    sleep(1)
    mmesagAdd = 'https://www.facebook.com/messages/t/'
    mmesagLink = mmesagAdd+frandId
    driver.get(mmesagLink)
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//div[@class="_1mf _1mj"]').send_keys(mmesage, Keys.ENTER)
    sleep(3)
    messagebox.showinfo("แจ้งเตือน", "กดSendได้เลยค่ะ")

# window
tkWindow = Tk()
tkWindow.geometry('250x150')
tkWindow.title('Send To Help')
# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password).grid(row=1, column=1)

TessLabel = Label(tkWindow, text="Text").grid(row=2, column=0)
Tess = StringVar()
TessEntry = Entry(tkWindow, textvariable=Tess).grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password, Tess)

# login button
loginButton = Button(tkWindow, text="Save",
                     command=validateLogin).grid(row=4, column=1)


tkWindow.mainloop()
