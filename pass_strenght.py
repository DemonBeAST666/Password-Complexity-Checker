import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) < 8:
        feedback.append("Use at least 8 characters.")
    else:
        score += 1
    
    if not re.search(r"[A-Z]", password):
        feedback.append("Use at least one uppercase letter.")
    else:
        score += 1
    
    if not re.search(r"[a-z]", password):
        feedback.append("Use at least one lowercase letter.")
    else:
        score += 1
    
    if not re.search(r"\d", password):
        feedback.append("Use at least one number.")
    else:
        score += 1
    
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        feedback.append("Use at least one special character.")
    else:
        score += 1
    
    return score, feedback

# Function to determine password strength level
def get_strength_label(score):
    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"

# Evaluate password strength
def evaluate_password():
    password = password_entry.get()
    score, feedback = check_password_strength(password)
    
    feedback_text = "\n".join(feedback) if feedback else "Password is strong!"
    strength_label.config(text=f"Strength: {get_strength_label(score)}\n{feedback_text}", fg=get_color(score))

# Get color for password strength label
def get_color(score):
    if score <= 1:
        return "red"
    elif score == 2:
        return "orange"
    elif score == 3:
        return "green"
    else:
        return "blue"

# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showwarning("Login", "Please enter username and password.")

# Toggle password visibility
def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="🔦")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="💡")

# GUI Setup
root = tk.Tk()
root.title("Secure Login")
root.geometry("360x640")  # Phone screen size

# Load and display background image
try:
    bg_image = Image.open("C:/clg_python/cyber Security/img_folder/images.jpg")  # Updated path
    bg_image = bg_image.resize((360, 640))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    print("Error loading image:", e)

# Transparent Frame
frame = tk.Frame(root, bg="#2b2b2b", padx=20, pady=20, relief="ridge", borderwidth=2)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.configure(bg="black", highlightbackground="white", highlightthickness=2)

# Title Label
title_label = tk.Label(frame, text="Login", font=("Arial", 16, "bold"), bg="black", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Username Label & Entry with Icon
username_label = tk.Label(frame, text="Username", font=("Arial", 12), bg="black", fg="white")
username_label.grid(row=1, column=0, padx=5, sticky="e")
username_icon = tk.Label(frame, text="👤", bg="black", fg="white")
username_icon.grid(row=1, column=1, padx=5)
username_entry = tk.Entry(frame, font=("Arial", 12), bg="black", fg="white", insertbackground="white", relief="flat")
username_entry.grid(row=1, column=2, pady=5, padx=10)
username_entry.config(highlightthickness=1, highlightbackground="cyan", highlightcolor="cyan")

# Password Label & Entry with Icon
password_label = tk.Label(frame, text="Password", font=("Arial", 12), bg="black", fg="white")
password_label.grid(row=2, column=0, padx=5, sticky="e")
password_icon = tk.Label(frame, text="🔒", bg="black", fg="white")
password_icon.grid(row=2, column=1, padx=5)
password_entry = tk.Entry(frame, font=("Arial", 12), show="*", bg="black", fg="white", insertbackground="white", relief="flat")
password_entry.grid(row=2, column=2, pady=5, padx=10)
password_entry.bind("<KeyRelease>", lambda event: evaluate_password())
password_entry.config(highlightthickness=1, highlightbackground="cyan", highlightcolor="cyan")

# Toggle Password Visibility Button
toggle_button = tk.Button(frame, text="💡", font=("Arial", 13), command=toggle_password_visibility, bg="black", fg="white", relief="flat")
toggle_button.grid(row=2, column=3, padx=5)

# Strength Label
strength_label = tk.Label(frame, text="Strength: ", font=("Arial", 10), bg="black", fg="white", justify="left")
strength_label.grid(row=3, column=0, columnspan=4, pady=5)

# Login Button
login_button = ttk.Button(frame, text="Login", command=login)
login_button.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
