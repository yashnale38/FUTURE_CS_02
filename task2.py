import tkinter as tk
from tkinter import messagebox
import hashlib
import re

def analyze_password(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[\W_]', password):  # Check for special characters
        strength += 1

    if strength == 5:
        return 'Strong: Your password is secure!', strength
    elif strength >= 3:
        return 'Medium: Your password is decent, but could be stronger.', strength
    else:
        return 'Weak: Your password is not secure enough.', strength

def hash_password(password):
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

def check_password():
    password = password_entry.get()
    strength_message, strength_value = analyze_password(password)
    hashed_password = hash_password(password)
    strength_meter.set(strength_value)  # Update the strength meter
    messagebox.showinfo("Password Strength", "Strength: " + strength_message + "\n\nHashed Password: " + hashed_password)

# Create the main window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("300x250")

# Set dark theme colors
root.configure(bg='black')
label_color = 'white'
entry_color = '#333333'  # Dark gray for entry
button_color = 'red'
scale_color = '#444444'  # Darker gray for scale
highlight_color = '#555555'  # Slightly lighter gray for highlights

# Create and pack widgets with dark, white, and red theme
tk.Label(root, text="Please enter your password:", bg='black', fg=label_color).pack(pady=5)
password_entry = tk.Entry(root, show='*', width=30, bg=entry_color, fg=label_color, insertbackground=label_color)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password, bg=button_color, fg=label_color)
check_button.pack(pady=10)

# Strength meter
strength_meter = tk.Scale(root, from_=0, to=5, orient='horizontal', length=200, label='Password Strength', tickinterval=1, bg=scale_color, fg=label_color, highlightbackground=highlight_color)
strength_meter.pack(pady=10)

# Start the main loop
root.mainloop()