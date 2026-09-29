import tkinter
from tkinter import *
root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry('400x500')
frame_details = Frame(master=root, height=150, width=360, bg="#ddb9f9")
lbl = Label(frame_details, text="Account Name:", bg="#9561bc", fg='white', width=14)
lbl2 = Label(frame_details, text="Enter PIN:", bg="#52098A", fg="white", width=14)
acc_entry = Entry(frame_details)
pin_entry = Entry(frame_details, show="*")
def confirm_PIN():
    acc= acc_entry.get()
    pin = pin_entry.get()
    message = "Hello" +acc+ "Congratualtions on setting up your ATM PIN!"
    textbox.insert(END, message)
    textbox = Text(bg="#BF51D2")
keypad_frame = Frame(master=root, relief=SUNKEN, borderwidth=2)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["!", 0, "@"]
]
for i in range(4):
    keypad_frame.columnconfigure(i, weight=1, minsize=40)
    for j in range(3):
        keypad_frame.rowconfigure(i, weight=1, minsize=70)      
        cell = Frame(master=keypad_frame, relief= RAISED, borderwidth=1)
        cell.grid(row=i, column=j, sticky="nsew")
        number_label = Label(master=cell, text=numbers[i][j], bg="#860086")
        number_label.pack(padx=8, pady=8)
confirm_bttn = Button(root, text="Set ATM PIN", command=confirm_PIN, bg="#a58ea7", fg="white")
message_box = Text(root, height=5, width=42, bg="#870EBF", fg="white") 
frame_details.place(x=20, y=10)
lbl.place(x=15, y=25)
acc_entry.place(x=155, y=25)
lbl2.place(x=15, y=85)
pin_entry.place(x=155, y=85)
message_box.place(x=25, y=410)
keypad_frame.place(x=85, y=180)
confirm_bttn.place(x=145, y=370)
root.mainloop