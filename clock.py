from tkinter import *
from tkinter.ttk import *
 
from time import strftime



root=Tk()
root.title('Shyam Nair\'s Clock')
lbl = Label(root, font=('ds-digital',90,'bold'), background = 'white',foreground=  'Red')
lbl.pack(anchor="center")

def time():
    string = strftime('%D\n   %B\n%H:%M:%S %p')
    lbl.config(text=(string))
    lbl.after(1000,time)

time()


mainloop()