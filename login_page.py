import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title(" Basic Login Page using Python")

window.configure(bg='#8F00FF')

def login():
    username = "pavi"
    password = "123"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Basic Login Successful!", message="You perfectly logged in.")
    else:
        messagebox.showerror(title="Error", message="wrong login.")

frame = tkinter.Frame(bg='#8F00FF')

login_label = tkinter.Label(frame, text="Basic Login Page Using Python", bg='#000000', fg="#DC143C", font=("italic", 20))
username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("italic", 20, 'italic'))
password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("italic", 20, 'italic'))
username_entry = tkinter.Entry(frame, font=("italic", 20))
password_entry = tkinter.Entry(frame, show="*", font=("italic", 20))
login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("italic", 20), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()