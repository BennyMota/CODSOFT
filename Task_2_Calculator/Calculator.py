import tkinter

calculator_win = tkinter.Tk()
calculator_win.title("Calculator")

expression = ""

def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "Syntax Error"
            expression = ""
    label_result.config(text=result)

#Creating GUI
label_result = tkinter.Label(calculator_win, height=4, text="0")
label_result.grid(row=0, column=0, columnspan=4)

button_7 = tkinter.Button(calculator_win, text="7", width=4, command=lambda: add("7"))
button_7.grid(row=1, column=0)

button_8 = tkinter.Button(calculator_win, text="8", width=4, command=lambda: add("8"))
button_8.grid(row=1, column=1)

button_9 = tkinter.Button(calculator_win, text="9", width=4, command=lambda: add("9"))
button_9.grid(row=1, column=2)

button_divide = tkinter.Button(calculator_win, text="/", width=4, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(calculator_win, text="4", width=4, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(calculator_win, text="5", width=4, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(calculator_win, text="6", width=4, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(calculator_win, text="*", width=4, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button_1 = tkinter.Button(calculator_win, text="1", width=4, command=lambda: add("1"))
button_1.grid(row=3, column=0)

button_2 = tkinter.Button(calculator_win, text="2", width=4, command=lambda: add("2"))
button_2.grid(row=3, column=1)

button_3 = tkinter.Button(calculator_win, text="3", width=4, command=lambda: add("3"))
button_3.grid(row=3, column=2)

button_subtract = tkinter.Button(calculator_win, text="-", width=4, command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

button_clear = tkinter.Button(calculator_win, text="C", width=4, command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(calculator_win, text="0", width=4, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(calculator_win, text=".", width=4, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_plus = tkinter.Button(calculator_win, text="+", width=4, command=lambda: add("+"))
button_plus.grid(row=4, column=3)

button_equals = tkinter.Button(calculator_win, text="=", width=20, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)


calculator_win.mainloop()