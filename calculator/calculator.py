from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

def click(x):
    entry.insert(END, x)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        Button(root, text=text, command=clear).grid(row=row, column=col)
    elif text == "=":
        Button(root, text=text, command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=text, command=lambda t=text: click(t)).grid(row=row, column=col)

root.mainloop()
