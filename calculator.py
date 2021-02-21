import tkinter as tk

main = tk.Tk()
main.title("Calculator")
main.resizable(0,0)

number1 = 0
number2 = 0

entry = tk.Entry(main, width=40,borderwidth=5)
entry.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

def buttonPressed(no):
    a = entry.get()
    b = len(a)
    entry.insert(b,str(no))

def operator(xyz):
    global number1,number2
    if number1 == 0:
        number1 = int(entry.get())
        print(number1)
        entry.delete(0,len(str(number1)))
    else:
        number2 = int(entry.get())
        entry.delete(0,len(str(number2)))
        if xyz == "+":
            s = number1 + number2
            number1, number2 = 0, 0
            c = str(s)
            c = "".join(reversed(c))
            for i in range(len(c)):
                entry.insert(0,c[i])


button7 = tk.Button(main,text="7",width = 5, padx=5, pady=5, command = lambda:buttonPressed(7))
button7.grid(row=1,column=0)

button8 = tk.Button(main,text="8",width = 5, padx=5, pady=5, command = lambda:buttonPressed(8))
button8.grid(row=1,column=1)

button9 = tk.Button(main,text="9",width = 5, padx=5, pady=5, command = lambda:buttonPressed(9))
button9.grid(row=1,column=2)

addButton = tk.Button(main,text="x",width = 5, padx=5, pady=5)
addButton.grid(row=1,column=3)

button4 = tk.Button(main,text="4",width = 5, padx=5, pady=5, command = lambda:buttonPressed(4))
button4.grid(row=2,column=0)

button5 = tk.Button(main,text="5",width = 5, padx=5, pady=5, command = lambda:buttonPressed(5))
button5.grid(row=2,column=1)

button6 = tk.Button(main,text="6",width = 5, padx=5, pady=5, command = lambda:buttonPressed(6))
button6.grid(row=2,column=2)

subButton = tk.Button(main,text="-",width = 5, padx=5, pady=5)
subButton.grid(row=2,column=3)

button1 = tk.Button(main,text="1",width = 5, padx=5, pady=5, command = lambda:buttonPressed(1))
button1.grid(row=3,column=0)

button2 = tk.Button(main,text="2",width = 5, padx=5, pady=5, command = lambda:buttonPressed(2))
button2.grid(row=3,column=1)

button3 = tk.Button(main,text="3",width = 5, padx=5, pady=5, command = lambda:buttonPressed(3))
button3.grid(row=3,column=2)

addButton = tk.Button(main,text="+",width = 5, padx=5, pady=5,command = lambda: operator("+"))
addButton.grid(row=3,column=3)

button0 = tk.Button(main,text="0",width = 16, padx=5, pady=5)
button0.grid(row=4,column=0,columnspan=2)

decimalButton = tk.Button(main,text=".",width = 5, padx=5, pady=5)
decimalButton.grid(row=4,column=2)

equalButton = tk.Button(main,text="=",width = 5, padx=5, pady=5)
equalButton.grid(row=4,column=3)

main.mainloop()