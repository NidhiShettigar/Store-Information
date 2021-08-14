#Nidhi's code on phone number(1st project)
import tkinter as tk
from tkinter import *
from tkinter import messagebox
window = Tk() #variable for Tk object
window.geometry("900x600")
window.title("Mobile Number File Store")
input1 = StringVar()
input2 = StringVar()
#labels
label1 = Label(window,text="Enter your information here",fg="purple2",bg="OliveDrab1",relief="solid",width=25,font=("Times New Roman",19,"bold"))
label1.place(x=250,y=30)
label2 = Label(window,text="Enter Name",fg="deep pink",bg="light cyan",relief="solid",width=20,font=("arial",10,"bold"))
label2.place(x=60,y=100)
label3 = Label(window,text="Enter Number",fg="deep pink",bg="light cyan",relief="solid",width=20,font=("arial",10,"bold"))
label3.place(x=60,y=150)
label4 = Label(window,text="View your information",fg="purple2",bg="OliveDrab1",relief="solid",width=25,font=("Times New Roman",19,"bold"))
label4.place(x=250,y=280)
#input boxes
your_name = Entry(window,textvar=input1,width=50)
your_name.place(x=250,y=100)
your_number = Entry(window,textvar=input2,width=50)
your_number.place(x=250,y=150)
#view data box
text1 = Text(window, height=11, width=90)
text1.grid(row=5, columnspan=4)
text1.place(x=60,y=350)


def function():
    name = str(your_name.get())
    number = str(your_number.get())
    if len(number) == 10:
        check_update = open('datastore.txt', 'a')
        check_input = open('datastore.txt', 'r')
        entry = check_input.read()
        if number in entry:
            messagebox.showwarning("Duplicate number","Number already exits")
        else:
            check_update.write(f"{name}\t\t{number}\n")
            messagebox.showinfo("Message","Number sucessfully added")
    elif number == str(number):
        messagebox.showwarning("Invalid Input","Please enter numbers")


def check():
    check_update = open('datastore.txt', 'r')
    show = check_update.read()
    for a in show[::-1]:
        text1.insert(0.0, a)


def clear():
    text1.delete(0.0, tk.END)


#buttons
b1 = Button(window,text="CHECK",width=15,bg="SeaGreen2",fg="magenta3",command=check,font=("verdana",10,"bold"))
b1.place(x=520,y=550)
b2 = Button(window,text="CLEAR",width=15,bg="SeaGreen2",fg="magenta3",command=clear,font=("verdana",10,"bold"))
b2.place(x=680,y=550)
b3 = Button(window,text="INSERT",width=15,bg="SeaGreen2",fg="magenta3",command=function,font=("verdana",10,"bold"))
b3.place(x=170,y=220)

window.mainloop()