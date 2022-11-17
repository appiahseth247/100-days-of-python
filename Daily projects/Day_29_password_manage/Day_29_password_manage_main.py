"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 29 - Password Manager GUI with TKinter                                                            *
*    Subject:  Tkinter GUI, dialogue box and pop-ups and  saving data to file,                              *
*    Date: 2022-05-17                                                                                       *
*    Purpose: - Generates a random password                                                                 *
*             - made up of reshuffled 8-10 letters, 2-4 numbers and 2-4 symbols                             *
*             - Stores the website info and the generated password to a txt file                            *
*************************************************************************************************************
"""

from tkinter import *
from tkinter import messagebox  # not a class hence not  import with the * above therefore imported separately
from random import randint, shuffle, choice
import pyperclip


# Day 29 project - Password Manager

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)  # to reshuffle the generated password

    password = "".join(password_list)  # join the elements in a list or strings 0r tuple or dict spaced by whatever
    # is put inside the "". If nothing is placed inside the "", there won't be any separation

    print(f"Your password is: {password}")
    password_entry.delete(0, END)  # deletes whatever is in the password_entry box
    password_entry.insert(END, password)  # populates the password entry_entry box with the generated password

    pyperclip.copy(password)  # This copies the password to the clipboard ready to be pasted


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any field empty")
    else:
        save_it = messagebox.askokcancel(title=website, message=f"Please check the details entered\nemail: {email}\n"
                                                                f"password: {password}"f"\nDo you want to save it?")
        if save_it:
            with open("password_data.txt", "a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)  # deletes from the 0th entry to the end of the entry
                password_entry.delete(0, END)
                messagebox.showinfo(title="Success", message=f"Added {website} to the password_data successfully")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("the_Sethoo1 Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="EW")

# entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry(width=35)
email_entry.insert(0, "Enter email")  # pre-populate it with the email
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.insert(0, "Enter password")
password_entry.grid(column=1, row=3, sticky="EW")

# buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add", width=36, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
