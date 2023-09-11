from tkinter import *

def click():
    print("you have entered the right button")
window = Tk()

photo = PhotoImage(file ='ballon.png')
button = Button(window,
                text = "click me!",
                command = click,
                font=("Comic sans",30),
                fg ="red",
                bg = "black",
                image =photo,
                compound='top'
                )
button.pack()

window.mainloop()
