# Creating email with log in

import tkinter as tk
from tkinter import messagebox
import random
import time
person = {}

root = tk.Tk()
root.title("Z8Game Login")
root.geometry("400x500")
root.configure(bg="#2f2f2f")

current_code = None

def code():
    return random.randint(100000, 999999)

signup_frame = tk.Frame(root, bg="#2f2f2f")
login_frame = tk.Frame(root, bg="#2f2f2f")
success_frame = tk.Frame(root, bg="#2f2f2f")

for frame in (signup_frame, login_frame, success_frame):
    frame.place(relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

# SIGNUP 

def signup():
    user = su_user.get().lower()
    password = su_pass.get()
    email = su_email.get()
    nickname = su_nick.get()
    dob = su_dob.get()
    gender = su_gender.get()

    if gender.lower() not in ["f", "m"]:
        messagebox.showerror("Error", "Gender must be F or M")
        return

    if not all([user, password, email, nickname, dob, gender]):
        messagebox.showerror("Error", "Fill all fields")
        return

    if su_confirm.get() != password:
        messagebox.showerror("Error", "Password mismatch")
        return

    person[user] = password

    messagebox.showinfo("Success", "Sign up completed!")
    show_frame(login_frame)

# LOGIN 
def send_code():
    global current_code
    current_code = code()
    messagebox.showinfo("Code Sent", f"Your code is: {current_code}")

def login():
    user = li_user.get().lower()
    password = li_pass.get()

    if user not in person:
        messagebox.showerror("Error", "User not found")
        return

    if person[user] != password:
        messagebox.showerror("Error", "Wrong password")
        return

    
    messagebox.showinfo("Success", "Login correct. Now send code.")

    send_code_btn.pack(pady=5)

def verify_code():
    user_code = li_code.get()

    if str(current_code) == user_code:
        messagebox.showinfo("Success", "Verified Successfully!")
        show_frame(success_frame)
    else:
        messagebox.showerror("Error", "Wrong verification code")

# SIGNUP UI 

tk.Label(signup_frame, text="SIGN UP", bg="#2f2f2f", fg="white", font=("Arial", 18)).pack(pady=10)

su_user = tk.Entry(signup_frame)
su_pass = tk.Entry(signup_frame, show="*")
su_confirm = tk.Entry(signup_frame, show="*")
su_email = tk.Entry(signup_frame)
su_nick = tk.Entry(signup_frame)
su_dob = tk.Entry(signup_frame)
su_gender = tk.Entry(signup_frame)

fields = [
    ("User", su_user),
    ("Password", su_pass),
    ("Confirm Password", su_confirm),
    ("Email", su_email),
    ("Nickname", su_nick),
    ("Date of Birth", su_dob),
    ("Gender (F/M)", su_gender)
]

for label, entry in fields:
    tk.Label(signup_frame, text=label, bg="#2f2f2f", fg="white").pack()
    entry.pack(pady=2)

tk.Button(signup_frame, text="Sign Up", command=signup, bg="gray").pack(pady=10)
tk.Button(signup_frame, text="Go to Login", command=lambda: show_frame(login_frame), bg="gray").pack()
time.sleep(3)
# LOGIN UI 

tk.Label(login_frame, text="LOGIN", bg="#2f2f2f", fg="white", font=("Arial", 18)).pack(pady=10)

li_user = tk.Entry(login_frame)
li_pass = tk.Entry(login_frame, show="*")
li_code = tk.Entry(login_frame)

tk.Label(login_frame, text="User", bg="#2f2f2f", fg="white").pack()
li_user.pack()

tk.Label(login_frame, text="Password", bg="#2f2f2f", fg="white").pack()
li_pass.pack()

tk.Button(login_frame, text="Login", command=login, bg="gray").pack(pady=10)

send_code_btn = tk.Button(login_frame, text="Send Code", command=send_code, bg="gray")

tk.Label(login_frame, text="Enter Code", bg="#2f2f2f", fg="white").pack()
li_code.pack()

tk.Button(login_frame, text="Verify Code", command=verify_code, bg="gray").pack(pady=10)

tk.Label(success_frame, text="WELCOME TO Z8GAME 🎮", bg="#2f2f2f", fg="white", font=("Arial", 16)).pack(pady=200)

show_frame(signup_frame)
root.mainloop()

#that's all ^-^




