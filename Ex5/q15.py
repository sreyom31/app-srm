from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar')


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


def start():
    for i in range(5):
        progress()


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=3, padx=10, pady=20)
# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=3)
# start button
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
start_button = ttk.Button(root, text="Start", command=start)
start_button.grid(column=2, row=2, padx=10, pady=10, sticky=tk.E)
root.mainloop()
