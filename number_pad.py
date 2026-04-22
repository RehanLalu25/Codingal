from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

nums = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
        ['#', 0, '*']]

# Configure grid
for i in range(4):
    root.rowconfigure(i, weight=1, minsize=50)

for j in range(3):
    root.columnconfigure(j, weight=1, minsize=75)

# Create buttons
for i in range(4):
    for j in range(3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")

        label = Label(
            master=frame,
            text=nums[i][j],
            bg='#d0efff',
            font=("Arial", 14)
        )
        label.pack(expand=True, fill='both')

# Run app
root.mainloop()