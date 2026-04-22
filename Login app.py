from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame
frame = Frame(root, height=300, width=360, bg="#d0efff")
frame.place(x=20, y=20)

# Labels
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=15)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg='white', width=15)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=15)

# Entry boxes
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function
def display():
    name = name_entry.get()
    textbox.delete("1.0", END)  # clear old text
    greet = "Hey " + name + "\n"
    message = "Congratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

# Button
btn = Button(frame, text="Create Account", command=display, bg="red", fg="white")

# Textbox
textbox = Text(root, bg="#BEBEBE", fg="black", height=4, width=45)

# Placement inside frame
lbl1.place(x=20, y=20)
name_entry.place(x=180, y=20)

lbl2.place(x=20, y=80)
email_entry.place(x=180, y=80)

lbl3.place(x=20, y=140)
pass_entry.place(x=180, y=140)

btn.place(x=120, y=200)

# Textbox placement
textbox.place(x=20, y=300)

# Run app
root.mainloop()