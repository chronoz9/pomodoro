import math
from tkinter import *
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_lbl.config(text='Timer', fg=GREEN)
    chk_lbl.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    minute = 60
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * minute)
        timer_lbl.config(text='Breather', fg=RED)
        messagebox.showwarning('Long Break', 'Take a walk for 20 minutes')
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * minute)
        timer_lbl.config(text='Break', fg=PINK)
        messagebox.showwarning('Take A Break!', 'Have a short break for 5 minutes')
    else:
        count_down(WORK_MIN * minute)
        timer_lbl.config(text='LET\'S GO!', fg=GREEN)
        if reps > 1:
            messagebox.showwarning('Get back there!', 'Continue what you were doing')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = "{:02d}".format(math.floor(count/60))
    secs = "{:02d}".format(count % 60)
    time_text = f"{mins}:{secs}"
    canvas.itemconfig(timer_text, text=time_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    global reps
    chk = ''
    for _ in range(math.floor(reps/2)):
        chk += '✔'

    chk_lbl.config(text=chk)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lbl = Label(text='TIMER', fg=GREEN, font=(FONT_NAME, 45, 'bold'), bg=YELLOW)
timer_lbl.grid(row=0, column=1)

chk_lbl = Label(text='', fg=GREEN, font=(FONT_NAME, 16, 'bold'), bg=YELLOW)
chk_lbl.grid(row=3, column=1)

start_btn = Button(text='Start', command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text='Reset', command=reset_timer)
reset_btn.grid(row=2, column=2)

canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(175, 112, image=image)
timer_text = canvas.create_text(175, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()