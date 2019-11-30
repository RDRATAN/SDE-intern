from tkinter import *
import tkinter as tk
import datetime
import time
from PIL import Image,ImageTk
root=tk.Tk()
root.title("Visitor Application")
root.geometry('450x530')

#Global variable decklarion
v = tk.StringVar()
v.set("Med")
nm=tk.StringVar()
sec_data=tk.StringVar()
roll_n=tk.StringVar()
L1=Label()
L2=Label()
L3=Label()
L4=Label()

#fram declarion----------------------------------------------
ques_win=Frame(root)
window=Frame(root)
home_btn=Frame(root)
home=Frame(root)
about_win=Frame(root)
quiz_win=Frame(root)
user=Frame(root)


def start(): 
    global L1,L2,L3,L4
    L1.pack_forget()
    L2.pack_forget()
    L3.pack_forget()
    L4.pack_forget()
    window.pack_forget()
    user.pack_forget()
    L1=Label(ques_win,text="NAME:\t"+name.get(),font=("Arial", 10))
    #L1.pack()
    L2=Label(ques_win,text="Yor Response has been Recorded",font=("Arial", 10))
    L2.pack()
    L3=Label(ques_win,text="Your visit ID:\t"+roll.get(),font=("Arial", 10))
    L3.pack()
    L4=Label(ques_win,text="LEVEL:\t"+v.get(),font=("Arial", 10))
    #L4.pack()
    ques_win.pack()
    

#Game instruction function----------
def inst():
    window.pack()
def quiz():
    ques_win.pack_forget()
    home.pack_forget()
    home_btn.pack_forget()
    user.pack()
    window.pack_forget()
    quiz_win.pack(side=BOTTOM)
    
def home_fun():
    index = 0
    ques_win.pack_forget()
    user.pack_forget()
    window.pack_forget()
    quiz_win.pack_forget()
    about_win.pack_forget()
    home.pack()
    home_btn.pack()
def about():
    ques_win.pack_forget()
    window.pack_forget()
    user.pack_forget()
    quiz_win.pack_forget()
    home.pack_forget()
    home_btn.pack_forget()
    about_win.pack()

#Heading of the window---------
l = Label(root, text="INNOVACCER ",fg="Black",font=("Arial Bold", 25))
l.pack()
li = Label(root, text="______________________________________",fg="Blue",font=("Helvetica", 20))
li.pack()
spa=Label(home,text=" ")
spa.pack()

#python Icon------------------
icon=Image.open("pyt.png")
im=ImageTk.PhotoImage(icon)
img=Label(home,image=im )
img.pack()
Label(home, text="Dont't Affraid, I m not Poisonus !",fg="brown",font=("Arial Bold", 15)).pack()
spa3=Label(home,text="                         ")
spa3.pack()
spa3=Label(home,text="   ")
spa3.pack()

#footer of Window--------------
Label(root, text="© 2021: Ratan Kumar Das ",fg="Black",font=("Arial Bold", 10)).pack(side=BOTTOM)

#Home page button-------
MyButton1 = Button(home_btn, text="Check-In",font=("Arial Bold", 12) ,width=15,fg="white",bg="green",command=quiz)
MyButton1.grid(row=0, column=1)

MyButton2 = Button(home_btn, text="Check-Out",font=("Arial Bold", 12), width=15,fg="white",bg="blue",command=about)
MyButton2.grid(row=0, column=2)

MyButton3 = Button(home_btn, text="Host", font=("Arial Bold", 12),width=15,fg="white",bg="purple",)
MyButton3.grid(row=0, column=3)
Label(home_btn,text="  ").grid(row=1,column=2)
MyButton3 = Button(home_btn, text="Exit APP", font=("Arial Bold", 12),width=15,fg="white",bg="red",command=root.destroy)
MyButton3.grid(row=2, column=2)

#About window Button-------
with open("about.txt", "r") as f:
    Label(about_win, text=f.read(),fg="brown",font=("Arial Bold", 10)).pack()
btn = Button(about_win, text="HOME", font=("Arial Bold", 12),width=15,fg="white",bg="green",command=home_fun)
btn.pack(side=BOTTOM)
#Quiz game Inter face-------------
home1 = Button(quiz_win, text="HOME",font=("Arial Bold", 12) ,width=15,fg="white",bg="blue",command=home_fun)
home1.grid(row=0, column=1)
space1=Label(quiz_win,text="   ",font=("Arial Bold", 12))
space1.grid(row=0,column=2)
exit1 = Button(quiz_win, text="EXIT",font=("Arial Bold", 12), width=15,fg="white",bg="red",command=root.destroy)
exit1.grid(row=0, column=3)

home.pack()
home_btn.pack()
strt_over=Button(window,text="start Over",width=20)

#visitor  Cridential frame inside visitor window------------
tk.Label(user, 
         text="Name    :",
         padx = 20,font=("Arial Bold", 12)).grid(row=1,column=1)
name=tk.Entry(user,textvariable=nm)
name.grid(row=1,column=2)
tk.Label(user, 
         text="Email  :",
         padx = 20,font=("Arial Bold", 12)).grid(row=2,column=1)
sec=tk.Entry(user,textvariable=sec_data)
sec.grid(row=2,column=2)
tk.Label(user, 
         text="Phone No. :",
         padx = 20,font=("Arial Bold", 12)).grid(row=3,column=1)
roll=tk.Entry(user,textvariable=roll_n)
roll.grid(row=3,column=2)

tk.Label(user, 
         text="Check-In :",
         padx = 20,font=("Arial Bold", 12)).grid(row=4,column=1)
t=time.localtime()
ct=time.strftime("%H:%M:%S", t)
checkin_time=tk.Label(user, text=ct)
checkin_time.grid(row=4,column=2)

tkvar = StringVar(root)
# Dictionary with options
choices = { 'HostName1','HostName2','HostName3','HostName4','HostName5'}
tkvar.set('Select Host') # set the default option

popupMenu = OptionMenu(user, tkvar, *choices)
Label(user, text="To Visit:",font=("Arial Bold", 12)).grid(row = 5, column = 1)
popupMenu.grid(row = 5, column =2)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

button = Button(user, text="Submit",width=14,font=("Arial Bold", 12),fg="white",bg="green",command=start)
button.grid(row=8,column=2)
#button6 = Button(user, text="Instuction",width=14,font=("Arial Bold", 12),fg="white",bg="purple",command=inst)
#button6.grid(row=8,column=2)
var = tk.StringVar()
with open("inst.txt", "r") as g:
    var.set(g.read())
label2 = Message(window, textvariable=var, relief=RAISED ,width=330)
label2.pack()
root.mainloop()


