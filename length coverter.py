from tkinter import *

# Create window
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Function to convert cm to meters
def convert():
    try:
        cm = float(entry.get())
        meters = cm / 100
        result_label.config(text=f"{meters} meters")
    except:
        result_label.config(text="Invalid input")

# Widgets
title_label = Label(root, text="Length Converter", font=("Arial", 16), bg="#4CAF50", fg="white")
title_label.pack(pady=10, fill=X)

entry = Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=20)

convert_button = Button(root, text="Convert to Meters", command=convert, bg="#2196F3", fg="white")
convert_button.pack(pady=10)

result_label = Label(root, text="Result will appear here", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=20, fill=X)

# Run app
root.mainloop()