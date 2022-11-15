"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 28 - Pomodoro App                                                                                 *
*    Subject:  Application of knowledge on TkInter                                                                     *
*    Date: 2022-05-13                                                                                       *
*************************************************************************************************************
"""

# Day 28 project - Pomodoro App

from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"  # color hex code from https://colorhunt.co/
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)  # This is used to stop the timer (in count_down)
    start_button.config(state="normal")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")
    reset_button.config(state="disabled")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # Thus, first rep

    if reps % 8 == 0:
        focus_window("on")
        messagebox.showinfo(title="Break", message="Click 'Ok' to start Long break!")
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        focus_window("on")
        messagebox.showinfo(title="Break", message="Click 'Ok' to start short break!")
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Short Break", fg=PINK)
    else:
        focus_window("off")
        messagebox.showinfo(title="Work", message="Click 'Ok' to Start working~")
        count_down(WORK_MIN)
        title_label.config(text="Work Time", fg=GREEN)
    start_button.config(state="disabled")  # So that disabled once it has been started
    reset_button.config(state="normal")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(duration_to_count_down):
    count_min = math.floor(duration_to_count_down / 60)  # floor() discards all decimal places irrespectively
    count_sec = duration_to_count_down % 60

    if len(str(count_sec)) != 2:  # That's if it shows sth like 5:0, 5: 9 instead of 5:00, 5:09
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if duration_to_count_down > 0:
        global timer
        timer = window.after(1000, count_down, duration_to_count_down - 1)
    else:
        start_timer()
        window.bell()

        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔️"
            check_marks_label.config(text=mark)


def focus_window(option):
    """ Raises the window to front and gives it the focus"""
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- USER INTERFACE SETUP ------------------------------- #
window = Tk()
window.title("Seth's Pomodoro")
window.config(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

# ***************** canvas class allow a content to be placed on the other **************** #
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highlightthickness fades the borders of image
tomato_img = PhotoImage(file="tomato.png")  # photoImage locates and loads the image
canvas.create_image(100, 112, image=tomato_img)  # the numbers are the location coordinates
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, font=("Times New Roman", 12, "bold"), state="normal")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Times New Roman", 12, "bold"), command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

title_label = Label(text="Timer", font=("Times New Roman", 30, "bold"), fg=GREEN, bg=YELLOW)
# fg means foreground color which becomes the actual color of the inputted text
title_label.grid(column=1, row=0)

check_marks_label = Label(text="", font=("Times New Roman", 8, "bold"), fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=4)

window.mainloop()
