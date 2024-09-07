import tkinter as tk

def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

def clear_text():
    entry.delete(0, tk.END)

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Entry widget to display the calculation
entry = tk.Entry(root, font=('Arial', 20), bd=10, relief=tk.SUNKEN, width=16, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Define the buttons and their layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 18), command=evaluate_expression, width=6, height=2, bg="green", fg="white")
    elif text == '/':
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: click_button('/'), width=6, height=2, bg="black", fg="white")
    elif text == '*':
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: click_button('*'), width=6, height=2, bg="black", fg="white")
    elif text == '-':
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: click_button('-'), width=6, height=2, bg="black", fg="white")
    elif text == '+':
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: click_button('+'), width=6, height=2, bg="black", fg="white")
    elif text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 18), command=clear_text, width=6, height=2, bg="red", fg="white")
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: click_button(t), width=6, height=2, bg="black", fg="white")
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Additional clear button
clear_button = tk.Button(root, text="C", font=('Arial', 18), command=clear_text, width=6, height=2, bg="red", fg="white")
clear_button.grid(row=5, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()
