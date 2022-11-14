"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 27 - Units converter                                                                              *
*    Subject:  GUI with Tkinter, Function Arguments (*Args, **Kwargs)                                       *
*    Date: 2022-05-09                                                                                       *
*************************************************************************************************************
"""
# Day 27 project - Miles to Km converter
from tkinter import *  # asterisk(*) here means import all classes from this modules

FONT = ("Arial", 15, "bold")
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def mile_km_converter():
    miles_entered = mile_input.get()
    km_output_label.config(text=round(float(miles_entered) * 1.6))


mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0, sticky="EW")

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1, sticky="EW")

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1, sticky="EW")

mile_input = Entry(width=30)
mile_input.config(width=10)
mile_input.focus()
mile_input.grid(column=1, row=0, sticky="EW")

km_output_label = Label(text=0, font=FONT)
km_output_label.grid(column=1, row=1, sticky="EW")

calculate_button = Button(text="Calculate", command=mile_km_converter, font=FONT)
calculate_button.grid(column=1, row=2, sticky="EW")

window.mainloop()  # mainloop is a while loop in tkinter that keeps the window open
