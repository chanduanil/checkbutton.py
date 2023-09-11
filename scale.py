from tkinter import *
def submit():
    print("temperature is :" +str(scale.get())+ "degree c")
window = Tk()

scale = Scale(window,from_= 0,
                     to=100,
                     length = 600,
                     orient = VERTICAL,# orientation of scale
                     font= ('consoles', 20),
                     tickinterval= 10,# numeric indicator for value
                     showvalue = 0#this will hide the current value

                   )
scale.set(50)
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()
