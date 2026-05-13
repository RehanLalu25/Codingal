from tkinter import *

window = Tk()

window.geometry("400x400")

window.title("Length Converter App")

window.configure(bg="#f0f0f0")


def check_strength():

    password = entry.get()

    length = len(password)

    if length <= 5:
        result.config(text="Weak", fg="red")

    elif length >= 6 and length <= 8:
        result.config(text="Medium", fg="yellow")

    elif length > 8 and length <= 12:
        result.config(text="Strong", fg="light green")

    else:
        result.config(text="Very Strong", fg="dark green")


heading = Label(window,
                text="Password Strength Checker",
                font=("Arial", 18, "bold"),
                bg="#f0f0f0",
                fg="blue")

heading.pack(pady=20)


label = Label(window,
              text="Enter Password:",
              font=("Arial", 12),
              bg="#f0f0f0")

label.pack(pady=10)


entry = Entry(window,
              width=25,
              font=("Arial", 14),
              show="*")

entry.pack(pady=10)


button = Button(window,
                text="Check Strength",
                font=("Arial", 12, "bold"),
                bg="#4CAF50",
                fg="white",
                command=check_strength)

button.pack(pady=20)


result = Label(window,
               text="",
               font=("Arial", 16, "bold"),
               bg="#f0f0f0")

result.pack(pady=20)


window.mainloop()