from tkinter import *
import math
import time
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# TIMER RESET


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# TIMER MECHANISM
def start_timer():
    global reps
    reps = reps+1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=RED)


# COUNTDOWN MECHANISM


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks = marks+"✓"
        check_mark.config(text=marks)



# UI SETUP
window = Tk()
window.title("Pomodoro")   # Pomodoro Refers to tomato in italian
window.config(padx=200, pady=120, bg=GREEN)

title_label = Label(text="Pomodoro", fg=RED,bg=GREEN, font=(FONT_NAME, 20))
title_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=GREEN, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark = Label(fg=RED, bg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
