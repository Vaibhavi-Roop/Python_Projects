import tkinter
from tkinter import messagebox
from tkinter import *
root = Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning("Alert! Virus Found")
button = Button(root, text="Scan For Virus", command=msg)
button.place(x=40, y=80)
root.mainloop()