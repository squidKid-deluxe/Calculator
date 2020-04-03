"""
A simple GUI calculator
"""
import tkinter as tk
import numexpr

# Create window and set title
ROOT = tk.Tk()
ROOT.title("Calculator")


def _clear_():
    ENTER.delete(0, 100)

def calculate():
    """
    calculate tkinter entry
    """
    # get the entry
    cal_this = ENTER.get()
    # if entry is valid
    try:
        # evaluate entered equation
        number = numexpr.evaluate(cal_this)
        # clear the entry box
        ENTER.delete(0, 100)
        # write the answer to the entry box
        ENTER.insert(0, str(number))
    # else:
    except KeyError:
        # clear the entry box
        ENTER.delete(0, 100)
        # write `error` to the entry box
        ENTER.insert(0, "CALCULATION ERROR")
    except SyntaxError:
        # clear the entry box
        ENTER.delete(0, 100)
        # write `error` to the entry box
        ENTER.insert(0, "CALCULATION ERROR")
    except OverflowError:
        # clear the entry box
        ENTER.delete(0, 100)
        # write `error` to the entry box
        ENTER.insert(0, "OVERFLOW ERROR")



# create entry box and pack
ENTER = tk.Entry(ROOT, bg="green", relief=tk.RIDGE, borderwidth=20, width=37)
ENTER.grid(row=1, column=1, columnspan=5, rowspan=2)


# initalize all of the 21 tkinter buttons.

B1 = tk.Button(
    ROOT,
    text="=",
    command=calculate,
    width=39,
    bg="green",
    activebackground="red",)
B1.grid(row=3, column=1, columnspan=5)


B1 = tk.Button(
    ROOT,
    text="1",
    command=lambda: ENTER.insert(200, '1'),
    width=5,
    bg="green",
    activebackground="red",)
B1.grid(row=4, column=1)

B2 = tk.Button(
    ROOT,
    text="2",
    command=lambda: ENTER.insert(200, '2'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=4, column=2)

B2 = tk.Button(
    ROOT,
    text="3",
    command=lambda: ENTER.insert(200, '3'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=4, column=3)

B2 = tk.Button(
    ROOT,
    text="4",
    command=lambda: ENTER.insert(200, '4'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=5, column=1)

B2 = tk.Button(
    ROOT,
    text="Clear",
    command=_clear_,
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=4, column=5)

B2 = tk.Button(
    ROOT,
    text="5",
    command=lambda: ENTER.insert(200, '5'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=5, column=2)

B2 = tk.Button(
    ROOT,
    text="6",
    command=lambda: ENTER.insert(200, '6'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=5, column=3)

B2 = tk.Button(
    ROOT,
    text="7",
    command=lambda: ENTER.insert(200, '7'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=1)

B2 = tk.Button(
    ROOT,
    text="8",
    command=lambda: ENTER.insert(200, '8'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=2)

B2 = tk.Button(
    ROOT,
    text="/",
    command=lambda: ENTER.insert(200, '/'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=4, column=4)

B2 = tk.Button(
    ROOT,
    text="*",
    command=lambda: ENTER.insert(200, '*'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=5, column=4)

B2 = tk.Button(
    ROOT,
    text="-",
    command=lambda: ENTER.insert(200, '-'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=4)

B2 = tk.Button(
    ROOT,
    text="9",
    command=lambda: ENTER.insert(200, '9'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=3)

B2 = tk.Button(
    ROOT,
    text="0",
    command=lambda: ENTER.insert(200, '0'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=7, column=1)

B2 = tk.Button(
    ROOT,
    text="7",
    command=lambda: ENTER.insert(200, '7'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=1)

B2 = tk.Button(
    ROOT,
    text="(",
    command=lambda: ENTER.insert(200, '('),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=6, column=5)

B2 = tk.Button(
    ROOT,
    text=")",
    command=lambda: ENTER.insert(200, ')'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=7, column=5)

B2 = tk.Button(
    ROOT,
    text="+",
    command=lambda: ENTER.insert(200, '+'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=7, column=4)

B2 = tk.Button(
    ROOT,
    text="x^2",
    command=lambda: ENTER.insert(200, '**2'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=5, column=5)

B2 = tk.Button(
    ROOT,
    text="%",
    command=lambda: ENTER.insert(200, '%'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=7, column=3)

B2 = tk.Button(
    ROOT,
    text=".",
    command=lambda: ENTER.insert(200, '.'),
    width=5,
    bg="green",
    activebackground="red",)
B2.grid(row=7, column=2)

# tkinter main loop
tk.mainloop()
