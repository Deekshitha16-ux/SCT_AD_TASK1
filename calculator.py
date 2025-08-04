import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Main GUI window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

expression = ""
equation = tk.StringVar()

# Input field
entry_field = tk.Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry_field.grid(columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x != '=' else equalpress()
    tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 15), command=action).grid(row=row, column=col)

# Clear button
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 15), command=clear).grid(row=5, columnspan=4)

# Run the application
window.mainloop()