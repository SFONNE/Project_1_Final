from tkinter import *
from functools import partial
from tkinter.ttk import *
import os
import sys
from tkinter import messagebox


def validateLogin(username, password, Tess):
    username.get()
    password.get()
    Tess.get()
    if not username:
        messagebox.showerror("showerror", "กรุณาใส่ให้ครบทุกช่องค่ะ")
    else:
        exec(open('deSentAndLogin.py').read())

    

# window
tkWindow = Tk()
tkWindow.geometry('250x100')
tkWindow.title('Send To Help')
# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,
                      show='*').grid(row=1, column=1)

TessLabel = Label(tkWindow, text="Text").grid(row=2, column=0)
Tess = StringVar()
TessEntry = Entry(tkWindow, textvariable=Tess,
                  show='*').grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password, Tess)




# login button
loginButton = Button(tkWindow, text="Login",
                     command=validateLogin).grid(row=4, column=1)


tkWindow.mainloop()
