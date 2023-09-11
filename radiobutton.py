#radiobutton =
from tkinter import *

window = Tk()
window.geometry("250x250")
food = ["pizzz","cake","panipuri"]

pizzimage = PhotoImage(file= "pizz.png")
cakeimage= PhotoImage(file = "cake.png")
panipuriimage = PhotoImage(file= 'panipuri.png')
foodimage = [pizzimage,cakeimage,panipuriimage]
x =IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text = food[i],#adds text to radio buttons
                               variable =x,#groups radiobutton togetther if they share the same variable
                               value=i,# assigns each radiobutton a different value
                               padx = 25,
                               font = 50,#adds padding on x-axis
                               image = foodimage[i],#adds image to radiobuttton
                               compound ='left',#adds image & text left side
                               indicatoron = 0,#eliminate circle indicators

                               )
    radio_button.pack(anchor= W)
window.mainloop()