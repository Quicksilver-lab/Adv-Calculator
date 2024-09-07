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

# Function to undo the last character
def undo_last():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

# Function to clear the entry widget
def clear_text():
    entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x600")

# Set the font style and size
button_font = ('Arial', 12, 'bold')
entry_font = ('Arial', 20, 'bold')

# Set the display variable
display = tk.StringVar()

# Entry widget to display results (expanded for larger text)
entry = tk.Entry(root, textvariable=display, font=entry_font, justify="right", bd=10, relief=tk.SUNKEN, bg="white", fg="black", width=30)
entry.grid(row=0, column=0, columnspan=6, pady=20, ipady=10)

# Buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4), ('√', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('%', 2, 4), ('^', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4), (')', 3, 5),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sin', 4, 4), ('cos', 4, 5),
    ('tan', 5, 0), ('ln', 5, 1), ('log', 5, 2), ('π', 5, 3), ('e', 5, 4), ('exp', 5, 5)
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=button_font, command=lambda: evaluate_expression(entry.get()), bg="green", fg="white", width=6, height=2)
    elif text == 'C':
        button = tk.Button(root, text=text, font=button_font, command=clear_text, bg="red", fg="white", width=6, height=2)
    elif text == '√':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.sqrt('), bg="lightblue", fg="black", width=6, height=2)
    elif text == '^':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('**'), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'exp':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.exp('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'sin':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.sin('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'cos':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.cos('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'tan':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.tan('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'ln':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.log('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'log':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.log10('), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'π':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.pi'), bg="lightblue", fg="black", width=6, height=2)
    elif text == 'e':
        button = tk.Button(root, text=text, font=button_font, command=lambda: insert_text('math.e'), bg="lightblue", fg="black", width=6, height=2)
    else:
        button = tk.Button(root, text=text, font=button_font, command=lambda t=text: insert_text(t), bg="black", fg="white", width=6, height=2)
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Additional undo button
undo_button = tk.Button(root, text="Undo", font=button_font, command=undo_last, bg="orange", fg="white", width=6, height=2)
undo_button.grid(row=6, column=0, columnspan=6, pady=10)

root.mainloop()
