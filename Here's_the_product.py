from tkinter import *

# Create window
root = Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

# Function to calculate product
def calculate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 * num2

        # Clear previous result
        result_box.delete("1.0", END)
        result_box.insert(END, f"Product: {result}")
    except:
        result_box.delete("1.0", END)
        result_box.insert(END, "Enter valid numbers!")

# Description label
label_desc = Label(root, text="Enter two numbers to calculate their product")
label_desc.pack(pady=10)

# Label + Entry for first number
label1 = Label(root, text="Enter first number:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

# Label + Entry for second number
label2 = Label(root, text="Enter second number:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

# Button
btn = Button(root, text="Calculate Product", command=calculate)
btn.pack(pady=10)

# Text box for result
result_box = Text(root, height=2, width=25)
result_box.pack()

# Run window
root.mainloop()