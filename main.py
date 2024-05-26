# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to retrieve system's time 
from time import strftime

# creating tkinter window
root=Tk()
root.title('Shyam Nair\'s Clock')

# Styling the label widget so that clock will look more attractive
# Placing clock at the centre of the tkinter window
lbl = Label(root, font=('ds-digital',80,'bold'), background = 'black',foreground=  'white')
lbl.pack(anchor="center")
 
# This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)

time()
mainloop()