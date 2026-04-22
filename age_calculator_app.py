from tkinter import *
from datetime import date

# Create window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#e6f2ff")

# Function to calculate age
def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        birth_date = date(year, month, day)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(
            text=f"Hey {name}! You are {age} years old 🎉",
            fg="green"
        )
    except:
        result_label.config(text="Invalid input! Please check your data.", fg="red")

# Labels + Entries
Label(root, text="Name", bg="#4da6ff", fg="white", width=12).place(x=40, y=50)
name_entry = Entry(root)
name_entry.place(x=180, y=50)

Label(root, text="Day", bg="#4da6ff", fg="white", width=12).place(x=40, y=100)
day_entry = Entry(root)
day_entry.place(x=180, y=100)

Label(root, text="Month", bg="#4da6ff", fg="white", width=12).place(x=40, y=150)
month_entry = Entry(root)
month_entry.place(x=180, y=150)

Label(root, text="Year", bg="#4da6ff", fg="white", width=12).place(x=40, y=200)
year_entry = Entry(root)
year_entry.place(x=180, y=200)

# Button
Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white").place(x=130, y=260)

# Result
result_label = Label(root, text="", bg="#e6f2ff", font=("Arial", 12))
result_label.place(x=60, y=320)

# Run app
root.mainloop()