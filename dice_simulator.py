import random
import tkinter as tk

main = tk.Tk()
main.title("Dice Sim")
main.geometry("200x200")
main.resizable(0,0)

l1 = tk.Label(main,text="")
l1.place(x=92,y=90)

def roll():
    global l1
    number = random.randrange(1,7)
    l1.config(text=number)

def clear():
    global l1
    l1.config(text="")

b = tk.Button(main,text="Roll a dice!",command=roll)
b.place(x=47,y=55)

clearButton = tk.Button(main,text="Clear",command=clear)
clearButton.place(x=65,y=115)

main.mainloop()