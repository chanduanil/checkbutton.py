from tkinter import *

def Registration():
    pass

window = Tk()
window.geometry("520x520")
window.title("Python Registration Form")

name = Label(window,text="User name")
age = Label(window,text="age")
gender = Label(window,text="Gender")
name.grid(row = 2,column=1)
age.grid(row = 3,column=1)
gender.grid(row = 4,column=1)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.grid(row = 2, column = 2)
e2.grid(row = 3, column = 2)
e3.grid(row = 4, column = 2)

check_button = Checkbutton(window,text="submit", command=Registration)
check_button.grid(row = 10,column = 2)
b2 = Button(window,text="confirm")
b2.grid(row = 15,column = 2)

window.mainloop()