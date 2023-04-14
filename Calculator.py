import parser
from tkinter import *

root = Tk()
# giving name to calculator
root.title("calculator")
display = Entry(root)
# column span for combining column
display.grid(row=1, columnspan=6, sticky=W + E)
# get the user input  and place it in test field
i = 0


def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)


def UNDO():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "error")


def get_operation(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length


def calculate():
    entire_string = display.get()
    # parser function will divide the codes into parse tree and evaluate the result with python standard program.
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "error")


# Adding Num Buttons to the calculator
Button(root, text="1",width=2, command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2",width=2, command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3",width=2, command=lambda: get_variable(3)).grid(row=2, column=2)
Button(root, text="4",width=2, command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5",width=2, command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6",width=2, command=lambda: get_variable(6)).grid(row=3, column=2)
Button(root, text="7",width=2, command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8",width=2, command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9",width=2, command=lambda: get_variable(9)).grid(row=4, column=2)
Button(root, text="0",width=2, command=lambda: get_variable(0)).grid(row=5, column=1)
# Adding Operator Buttons to the calculator
Button(root, text="AC",width=2, command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="=",width=2, command=lambda: calculate()).grid(row=5, column=2)
Button(root, text="+",width=2, command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-",width=2, command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*",width=2, command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/",width=2, command=lambda: get_operation("/")).grid(row=5, column=3)
Button(root, text="pi",width=2, command=lambda: get_operation("3.14")).grid(row=2, column=4)
Button(root, text="%",width=2, command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(",width=2, command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="x^2",width=2, command=lambda: get_operation("**")).grid(row=5, column=4)
Button(root, text="exp",width=2, command=lambda: get_operation("**")).grid(row=2, column=5)
Button(root,width=2, text="x!").grid(row=3, column=5)
Button(root,width=2, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root,width=2, text="<-", command=lambda: UNDO()).grid(row=5, column=5)
root.mainloop()
