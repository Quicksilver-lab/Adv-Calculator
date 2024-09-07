import tkinter as tk
import math
import random
import matplotlib.pyplot as plt

# Function to evaluate expressions
def evaluate_expression(expression):
    try:
        result = eval(expression)
        display.set(result)
        history.append(expression + " = " + str(result))
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

# Prime Number Checker
def prime_check():
    try:
        current_text = entry.get()
        num = int(current_text)
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    display.set(f"{num} is not prime")
                    return
            display.set(f"{num} is prime")
        else:
            display.set(f"{num} is not prime")
    except:
        display.set("Error")

# Random Number Generator
def random_number():
    try:
        min_val = int(entry.get())
        max_val = min_val + 100
        random_num = random.randint(min_val, max_val)
        display.set(random_num)
    except:
        display.set("Error")

# Coin Flip
def coin_flip():
    result = random.choice(['Heads', 'Tails'])
    display.set(result)

# Dice Roll
def dice_roll():
    result = random.randint(1, 6)
    display.set(result)

# History Viewer
def show_history():
    history_text = "\n".join(history)
    display.set(history_text)

# Function Plotter
def plot_function():
    try:
        expr = entry.get()
        x_vals = list(range(-100, 100))
        y_vals = [eval(expr.replace("x", str(x))) for x in x_vals]
        plt.plot(x_vals, y_vals)
        plt.title(f"Graph of {expr}")
        plt.grid(True)
        plt.show()
    except:
        display.set("Error")

# Celsius to Fahrenheit Converter
def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        display.set(f"{celsius}°C = {fahrenheit}°F")
    except:
        display.set("Error")

# Themes/Skin (Switch Themes)
def switch_theme(theme):
    if theme == "dark":
        root.config(bg="black")
        entry.config(bg="black", fg="green")
    elif theme == "light":
        root.config(bg="white")
        entry.config(bg="white", fg="black")

# Magic 8 Ball Fun Feature
def magic_8_ball():
    responses = ['Yes', 'No', 'Maybe', 'Definitely', 'Ask again later', 'I don\'t know']
    result = random.choice(responses)
    display.set(result)

# Joke Generator Fun Feature
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? It had too many problems.",
        "Parallel lines have so much in common, it’s a shame they’ll never meet!"
    ]
    display.set(random.choice(jokes))

# Initialize the main window
root = tk.Tk()
root.title("Enhanced Scientific Calculator")
root.geometry("600x700")
root.config(bg="black")

# Set the font style and size
button_font = ('Arial', 18, 'bold')
entry_font = ('Arial', 24, 'bold')

# Set the display variable and history
display = tk.StringVar()
history = []

# Entry widget to display results
entry = tk.Entry(root, textvariable=display, font=entry_font, justify="right", bd=10, relief=tk.SUNKEN, bg="black", fg="green")
entry.grid(row=0, column=0, columnspan=6, pady=20)

# Buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3), ('C', 1, 4), ('Undo', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3), ('%', 2, 4), ('√', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4), (')', 3, 5),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sin', 4, 4), ('cos', 4, 5),
    ('tan', 5, 0), ('ln', 5, 1), ('log', 5, 2), ('π', 5, 3), ('e', 5, 4), ('^', 5, 5),
    
    # Fun and advanced features buttons
    ('Prime?', 6, 0), ('Rand', 6, 1), ('Coin Flip', 6, 2), ('Dice Roll', 6, 3), ('Magic 8-Ball', 6, 4), ('Joke', 6, 5),
    ('Plot', 7, 0), ('C to F', 7, 1), ('Theme Dark', 7, 2), ('Theme Light', 7, 3), ('History', 7, 4)
]

# Create and place the buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=button_font, command=lambda: evaluate_expression(entry.get()), bg="green", fg="white", width=4, height=2)
    elif text == 'C':
        button = tk.Button(root, text=text, font=button_font, command=clear_text, bg="red", fg="white", width=4, height=2)
    elif text == 'Undo':
        button = tk.Button(root, text=text, font=button_font, command=undo_last, bg="orange", fg="white", width=4, height=2)
    elif text == 'Prime?':
        button = tk.Button(root, text=text, font=button_font, command=prime_check, bg="purple", fg="white", width=4, height=2)
    elif text == 'Rand':
        button = tk.Button(root, text=text, font=button_font, command=random_number, bg="blue", fg="white", width=4, height=2)
    elif text == 'Coin Flip':
        button = tk.Button(root, text=text, font=button_font, command=coin_flip, bg="orange", fg="white", width=4, height=2)
    elif text == 'Magic 8-Ball':
        button = tk.Button(root, text=text, font=button_font, command=magic_8_ball, bg="cyan", fg="black", width=4, height=2)
    elif text == 'Joke':
        button = tk.Button(root, text=text, font=button_font, command=tell_joke, bg="yellow", fg="black", width=4, height=2)
    elif text == 'Plot':
        button = tk.Button(root, text=text, font=button_font, command=plot_function, bg="grey", fg="white", width=4, height=2)
    elif text == 'C to F':
        button = tk.Button(root, text=text, font=button_font, command=celsius_to_fahrenheit, bg="grey", fg="white", width=4, height=2)
    elif text == 'Theme Dark':
        button = tk.Button(root, text=text, font=button_font, command=lambda: switch_theme("dark"), bg="black", fg="green", width=6, height=2)
    elif text == 'Theme Light':
        button = tk.Button(root, text=text, font=button_font, command=lambda: switch_theme("light"), bg="white", fg="black", width=6, height=2)
    else:
        button = tk.Button(root, text=text, font=button_font, command=lambda t=text: insert_text(t), bg="black", fg="white", width=4, height=2)
    
    button.grid(row=row, column=col)

root.mainloop()
