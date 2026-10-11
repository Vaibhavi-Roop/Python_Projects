import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination Calculator")
root.configure(bg='light blue')
root.geometry("650x400")
upload = Image.open('money.png')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label_1 = Label(root, text="Hi User! Welcome To The Denomination Counter Application!", bg='light blue')
label_1.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    msg_box = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if msg_box == 'ok':
        topwin()
button_1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button_1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry('600x350+50+50')
    label = Label(top, text="Enter the total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are the number of notes for each denomination", bg='light grey')
    l1 = Label(top, text="100", bg='light grey')
    l2 = Label(top, text="50", bg='light grey')
    l3 = Label(top, text="20", bg='light grey')
    l4 = Label(top, text="10", bg='light grey')
    l5 = Label(top, text="5", bg='light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    def calculator():
        try:
            amount = int(entry.get())
            note_100 = amount // 100
            amount %= 100
            note_50 = amount // 50
            amount %= 50
            note_20 = amount // 20
            amount %= 20
            note_10 = amount // 10
            amount %= 10
            note_5 = amount // 5
            amount %= 5 
            t1.delete(0, END)
            t2.delete(0, END) 
            t3.delete(0, END)
            t4.delete(0, END)  
            t5.delete(0, END)
            t1.insert(END, str(note_100))
            t2.insert(END, str(note_50))
            t3.insert(END, str(note_20))
            t4.insert(END, str(note_10))
            t5.insert(END, str(note_5))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)      
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)
    top.mainloop()
root.mainloop()