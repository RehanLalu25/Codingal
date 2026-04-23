from tkinter import *

window = Tk()

window.title("Event Handler")
window.geometry("200x150")

# Function to handle key press
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind key press event to window
window.bind("<Key>", handle_keypress)

# Function to handle button click
def handle_click(event):
    print("\nThe button was clicked!")

# Create button
button = Button(window, text="Click me!")
button.pack(pady=20)

# Bind left mouse click to button
button.bind("<Button-1>", handle_click)

window.mainloop()