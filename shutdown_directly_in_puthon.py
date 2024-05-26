from tkinter import * 
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /r /t 1")

st=Tk()    # st is the object of tk
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Green")  #change in interface color


rt_button=Button(st,text="Restart ",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
rt_button.place(x=150,y=70,height=50,width=200)

r_button=Button(st,text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time) 
r_button.place(x=150,y=170,height=50,width=200)

lg_button =Button(st,text="Log-out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_out) 
lg_button.place(x=150,y=270,height=50,width=200)

sd_button=Button(st,text="Shutdown",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown) 
sd_button.place(x=150,y=370,height=50,width=200)


st.mainloop()