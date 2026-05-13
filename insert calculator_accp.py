from tkinter import *

window = Tk()

window.title("Age Calculator App")

window.geometry("400x400")

window.config(bg="#dfe6e9")


def calculate():

    p = float(principle_entry.get())

    t = float(time_entry.get())

    r = float(rate_entry.get())

    simple_interest = (p * t * r) / 100

    compound_interest = p * ((1 + r / 100) ** t) - p

    si_result.config(text="Simple Interest = " + str(round(simple_interest, 2)))

    ci_result.config(text="Compound Interest = " + str(round(compound_interest, 2)))


title_label = Label(window,
                    text="Interest Calculator",
                    font=("Arial", 18, "bold"),
                    bg="#74b9ff",
                    fg="white",
                    pady=10)

title_label.pack(fill=X)


frame = Frame(window, bg="#dfe6e9")

frame.pack(pady=30)


principle_label = Label(frame,
                        text="Principle:",
                        font=("Arial", 12),
                        bg="#dfe6e9")

principle_label.grid(row=0, column=0, padx=10, pady=10)

principle_entry = Entry(frame,
                        font=("Arial", 12),
                        width=15)

principle_entry.grid(row=0, column=1, padx=10, pady=10)


time_label = Label(frame,
                   text="Time (Years):",
                   font=("Arial", 12),
                   bg="#dfe6e9")

time_label.grid(row=1, column=0, padx=10, pady=10)

time_entry = Entry(frame,
                   font=("Arial", 12),
                   width=15)

time_entry.grid(row=1, column=1, padx=10, pady=10)


rate_label = Label(frame,
                   text="Rate (%):",
                   font=("Arial", 12),
                   bg="#dfe6e9")

rate_label.grid(row=2, column=0, padx=10, pady=10)

rate_entry = Entry(frame,
                   font=("Arial", 12),
                   width=15)

rate_entry.grid(row=2, column=1, padx=10, pady=10)


calculate_button = Button(window,
                          text="Calculate",
                          font=("Arial", 12, "bold"),
                          bg="#00b894",
                          fg="white",
                          command=calculate)

calculate_button.pack(pady=20)


si_result = Label(window,
                  text="Simple Interest = ",
                  font=("Arial", 12),
                  bg="#dfe6e9",
                  fg="#2d3436")

si_result.pack(pady=10)


ci_result = Label(window,
                  text="Compound Interest = ",
                  font=("Arial", 12),
                  bg="#dfe6e9",
                  fg="#2d3436")

ci_result.pack(pady=10)


window.mainloop()