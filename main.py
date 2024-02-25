from tkinter import *
FONT = ("Arial", 12)


def conversion():
    calculate_value = float(input.get()) * 1.609
    calculated_value_label.config(text=str(calculate_value))


window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=20)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0
                 )
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

calculated_value_label = Label(text="0", font=FONT)
calculated_value_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=FONT)
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(column=1, row=2)


window.mainloop()