import tkinter as tk
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        desired_length = int(length_entry.get())
        password = generate_password(desired_length)
        password_label.config(text=f"Generated password: {password}")
    except ValueError:
        password_label.config(text="Invalid input. Please enter a valid integer for password length.")

root = tk.Tk()
root.title("Password Generator")
root.config(background="black")
root.geometry("450x450")

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)
length_label = tk.Label(root, text="Enter desired password length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
password_label = tk.Label(root, text="")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)
length_label.grid(row=1, column=0, padx=10, pady=10)
length_entry.grid(row=1, column=1, padx=10, pady=10)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)
password_label.grid(row=3, columnspan=2, padx=10, pady=10)
root.mainloop()
