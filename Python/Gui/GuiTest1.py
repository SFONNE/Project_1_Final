from tkinter import *
import os
import sys

root = Tk()
root.geometry("250x250")
root.title(" AutoSales ")
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "6035512078"):
        Output.insert(END, 'เข้าใช้งาน')
        os.system(r'C:\Users\PosIT\Desktop\Project\RobotTest\Test-and-run.bat')
        Output.insert(END, 'ดำเนินการเสร็จสิ้น')
    else:
        Output.insert(END, "Code ผิด \n")


l = Label(text="input Code specifically")
inputtxt = Text(root, height=5,
                width=50,
                bg="light cyan")

Output = Text(root, height=5,
              width=50,
              bg="light cyan")

Display = Button(root, height=2,
                 width=25,
                 text="Go!",
                 command=lambda: Take_input())
Exit = Button(root, height=2,
                width=25,
                 text="Exit",
                 command=lambda: sys.exit()
)



                 


l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
Exit.pack()
mainloop()
