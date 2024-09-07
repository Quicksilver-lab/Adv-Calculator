import tkinter as tk
import math

# Function to evaluate expressions
def evaluate_expression(expression):
    try:
        result = eval(expression)
        display.set(result)
    except:
        display.set("Error")

# Function to insert text into the entry widget
def insert_text(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(text))

# Function to clear the entry widget
def clear_text():
    entry.delete(0, tk.END)

# Additional Mathematical Functions
def sqrt():
    try:
        current_text = entry.get()
        result = math.sqrt(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def sine():
    try:
        current_text = entry.get()
        result = math.sin(math.radians(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def cosine():
    try:
        current_text = entry.get()
        result = math.cos(math.radians(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def tangent():
    try:
        current_text = entry.get()
        result = math.tan(math.radians(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def logarithm():
    try:
        current_text = entry.get()
        result = math.log10(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def natural_log():
    try:
        current_text = entry.get()
        result = math.log(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def power():
    try:
        current_text = entry.get()
        entry.insert(tk.END, "**")
    except:
        display.set("Error")

def factorial():
    try:
        current_text = entry.get()
        result = math.factorial(int(current_text))
        display.set(result)
    except:
        display.set("Error")

def exp():
    try:
        current_text = entry.get()
        result = math.exp(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def arcsine():
    try:
        current_text = entry.get()
        result = math.degrees(math.asin(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def arccosine():
    try:
        current_text = entry.get()
        result = math.degrees(math.acos(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def arctangent():
    try:
        current_text = entry.get()
        result = math.degrees(math.atan(float(current_text)))
        display.set(result)
    except:
        display.set("Error")

def hyperbolic_sine():
    try:
        current_text = entry.get()
        result = math.sinh(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def hyperbolic_cosine():
    try:
        current_text = entry.get()
        result = math.cosh(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def hyperbolic_tangent():
    try:
        current_text = entry.get()
        result = math.tanh(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def percentage():
    try:
        current_text = entry.get()
        result = float(current_text) / 100
        display.set(result)
    except:
        display.set("Error")

def absolute_value():
    try:
        current_text = entry.get()
        result = abs(float(current_text))
        display.set(result)
    except:
        display.set("Error")

def pi():
    display.set(math.pi)

def modulus():
    try:
        current_text = entry.get()
        entry.insert(tk.END, "%")
    except:
        display.set("Error")

# Initialize the main window
root = tk.Tk()
root.title("Comprehensive Scientific Calculator")
root.geometry("500x700")
root.config(bg="black")

# Set the font style and size
button_font = ('Arial', 18, 'bold')
entry_font = ('Arial', 24, 'bold')

# Set the display variable
display = tk.StringVar()

# Entry widget to display results
entry = tk.Entry(root, textvariable=display, font=entry_font, justify="right", bd=10, relief=tk.SUNKEN, bg="black", fg="green")
entry.grid(row=0, column=0, columnspan=5, pady=20)

# Buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('%', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), (')', 4, 3), ('=', 4, 4),
    ('sqrt', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3), ('log', 5, 4),
    ('exp', 6, 0), ('pow', 6, 1), ('!', 6, 2), ('arcsin', 6, 3), ('arccos', 6, 4),
    ('arctan', 7, 0), ('sinh', 7, 1), ('cosh', 7, 2), ('tanh', 7, 3), ('ln', 7, 4),
    ('abs', 8, 0), ('pi', 8, 1), ('mod', 8, 2)
]

# Create and place the buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=button_font, command=lambda: evaluate_expression(entry.get()), bg="green", fg="white", width=4, height=2)
    elif text == 'C':
        button = tk.Button(root, text=text, font=button_font, command=clear_text, bg="red", fg="white", width=4, height=2)
    elif text == 'sqrt':
        button = tk.Button(root, text=text, font=button_font, command=sqrt, bg="purple", fg="white", width=4, height=2)
    elif text == 'sin':
        button = tk.Button(root, text=text, font=button_font, command=sine, bg="blue", fg="white", width=4, height=2)
    elif text == 'cos':
        button = tk.Button(root, text=text, font=button_font, command=cosine, bg="blue", fg="white", width=4, height=2)
    elif text == 'tan':
        button = tk.Button(root, text=text, font=button_font, command=tangent, bg="blue", fg="white", width=4, height=2)
    elif text == 'log':
        button = tk.Button(root, text=text, font=button_font, command=logarithm, bg="orange", fg="white", width=4, height=2)
    elif text == 'ln':
        button = tk.Button(root, text=text, font=button_font, command=natural_log, bg="orange", fg="white", width=4, height=2)
    elif text == 'pow':
        button = tk.Button(root, text=text, font=button_font, command=power, bg="grey", fg="white", width=4, height=2)
    elif text == '!':
        button = tk.Button(root, text=text, font=button_font, command=factorial, bg="grey", fg="white", width=4, height=2)
    elif text == 'exp':
        button = tk.Button(root, text=text, font=button_font, command=exp, bg="grey", fg="white", width=4, height=2)
    elif text == 'arcsin':
        button = tk.Button(root, text=text, font=button_font, command=arcsine, bg="blue", fg="white", width=4, height=2)
    elif text == 'arccos':
        button = tk.Button(root, text=text, font=button_font, command=arccosine, bg="blue", fg="white", width=4, height=2)
    elif text == 'arctan':
        button = tk.Button(root, text=text, font=button_font, command=arctangent, bg="blue", fg="white", width=4, height=2)
    elif text == 'sinh':
        button = tk.Button(root, text=text, font=button_font, command=hyperbolic_sine, bg="blue", fg="white", width=4, height=2)
    elif text == 'cosh':
        button = tk.Button(root, text=text, font=button_font, command=hyperbolic_cosine, bg="blue", fg="white", width=4, height=2)
    elif text == 'tanh':
        button = tk.Button(root, text=text, font=button_font, command=hyperbolic_tangent, bg="blue", fg="white", width=4, height=2)
    elif text == 'abs':
        button = tk.Button(root, text=text, font=button_font, command=absolute_value, bg="grey", fg="white", width=4, height=2)
    elif text == 'pi':
        button = tk.Button(root, text=text, font=button_font, command=pi, bg="grey", fg="white", width=4, height=2)
    elif text == 'mod':
        button = tk.Button(root, text=text, font=button_font, command=modulus, bg="grey", fg="white", width=4, height=2)
    else:
        button = tk.Button(root, text=text, font=button_font, command=lambda t=text: insert_text(t), bg="black", fg="white", width=4, height=2)
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()
