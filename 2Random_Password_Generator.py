import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Password Generator Logic
def generate_password():
    length = int(length_slider.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if not (use_upper or use_lower or use_digits or use_symbols):
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    char_pool = ''
    password = []

    if use_upper:
        char_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        password.append(random.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if length < len(password):
        messagebox.showwarning("Warning", f"Minimum length should be {len(password)}!")
        return

    remaining_length = length - len(password)
    password += random.choices(char_pool, k=remaining_length)
    random.shuffle(password)

    final_password = ''.join(password)
    password_var.set(final_password)
    pyperclip.copy(final_password)
    status_label.config(text="Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Variables
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)
length_slider = tk.IntVar(value=12)
password_var = tk.StringVar()

# Widgets
tk.Label(root, text="Advanced Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Checkbutton(frame, text="Include Uppercase (A-Z)", variable=upper_var).grid(row=0, column=0, sticky='w')
tk.Checkbutton(frame, text="Include Lowercase (a-z)", variable=lower_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(frame, text="Include Digits (0-9)", variable=digit_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(frame, text="Include Symbols (!@#$)", variable=symbol_var).grid(row=3, column=0, sticky='w')

tk.Label(root, text="Password Length").pack(pady=5)
tk.Scale(root, from_=6, to=32, orient='horizontal', variable=length_slider).pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

tk.Entry(root, textvariable=password_var, font=("Courier", 14), justify="center", width=30).pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# Run app
root.mainloop()
