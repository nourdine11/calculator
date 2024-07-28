import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *
from tkinter import font

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(width=0, height=0)
root.configure(bg="black")

entr = Entry(root, bd=10, width=30, font="Arial 21", bg="LightGrey")
entr.pack()

# function definitions
def click(nbr):
    entr.insert(tk.END, nbr)

def addition():
    entr.insert(tk.END, "+")

def subtraction():
    entr.insert(tk.END, "-")

def multiplication():
    entr.insert(tk.END, "*")

def division():
    entr.insert(tk.END, "/")

def equal():
    try:
        expression = entr.get()
        result = eval(expression)
        entr.delete(0, tk.END)
        entr.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "you can't divide by zero !")

def clear():
    entr.delete(0, tk.END)

# define buttons
btn1 = Button(root, text="1", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(1))
btn1.place(x=10, y=60)

btn2 = Button(root, text="2", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(2))
btn2.place(x=85, y=60)

btn3 = Button(root, text="3", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(3))
btn3.place(x=160, y=60)

btn4 = Button(root, text="4", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(4))
btn4.place(x=10, y=145)

btn5 = Button(root, text="5", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(5))
btn5.place(x=85, y=145)

btn6 = Button(root, text="6", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(6))
btn6.place(x=160, y=145)

btn7 = Button(root, text="7", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(7))
btn7.place(x=10, y=230)

btn8 = Button(root, text="8", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(8))
btn8.place(x=85, y=230)

btn9 = Button(root, text="9", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(9))
btn9.place(x=160, y=230)

btn0 = Button(root, text="0", font="System 19 bold", bg="White", bd="10", padx=10, pady=5, command=lambda: click(0))
btn0.place(x=10, y=315)

btn_add = Button(root, text="+", font="Arial 19 bold", width=2, height=1, bg="Cyan", bd="10", padx=8, pady=5, command=addition)
btn_add.place(x=235, y=60)

btn_sub = Button(root, text="-", font="Arial 19 bold", width=2, height=1, bg="Cyan", bd="10", padx=8, pady=5, command=subtraction)
btn_sub.place(x=235, y=145)

btn_div = Button(root, text="÷", font="System 19 bold", bg="Cyan", bd="10", padx=10, pady=5, command=division)
btn_div.place(x=235, y=230)

btn_clear = Button(root, text="C", font="Arial 19 bold", bg="crimson", bd="10", padx=10, pady=5, command=clear)
btn_clear.place(x=85, y=315)

btn_eq = Button(root, text="=", font="Arial 19 bold", bg="khaki", bd="10", padx=10, pady=5, command=equal)
btn_eq.place(x=160, y=315)

btn_mul = Button(root, text="*", font="Arial 19 bold", bg="Cyan", bd="10", padx=8, pady=5, command=multiplication)
btn_mul.place(x=235, y=315)

root.mainloop()
