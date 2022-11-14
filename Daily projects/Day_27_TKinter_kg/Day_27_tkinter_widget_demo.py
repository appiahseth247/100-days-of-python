from tkinter import *

"""
window = Tk()  # A class for creating a window
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)  # To add space around the ENTIRE program written (window)
my_label = Label(text="I am a label", font=("Arial", 10, "bold"))  # A class for creating a label
# my_label.pack()  # A method for packing a text onto the window just like "place" and "grid"
my_label.grid(column=0, row=0)  # grid() places content relative to others in column-row style
my_label.config(padx=10, pady=10)  # To add space around ONLY the my_label object
# NOTE1: editing the label
# my_label["text"] = "I am the new label now"
my_label.config(text="I am the new label now")
# Creating a button
def button_clicked():
    print("I got clicked")
    my_label.config(text=my_input.get())
button = Button(text="click me", command=button_clicked)
button.place(x=100, y=50)  # Takes the coordinates to place the info at a precise location
# unlike pack which is limited to up,bottom, left, right
# Entering
my_input = Entry(width=30)
my_input.get()  # The get method gets hold of what is typed in the entry box
my_input.grid(column=2, row=2)
"""

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)  # Accept inputs from user
# Add some text to begin with
entry.insert(END, string="email.")  # can be a description of what the user should type in the box
# Gets text in entry
print(entry.get())  # The get method gets hold of what is typed in the entry box
entry.pack()

# Text
text = Text(height=5, width=30)  # A large area where the user can edit

text.focus()  # Puts cursor in textbox.
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  # click up and down to change values
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
