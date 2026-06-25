from tkinter import *
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"

# --------------------------
# Functions
# --------------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for task in file:
                task_listbox.insert(END, task.strip())

def save_tasks():
    tasks = task_listbox.get(0, END)

    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task!"
        )
        return

    task_listbox.insert(END, task)
    task_entry.delete(0, END)

    save_tasks()

def delete_task():
    try:
        selected = task_listbox.curselection()[0]

        task_listbox.delete(selected)

        save_tasks()

    except:
        messagebox.showwarning(
            "Warning",
            "Please select a task!"
        )

def mark_completed():

    try:
        selected = task_listbox.curselection()[0]

        task = task_listbox.get(selected)

        if "✓" not in task:

            task_listbox.delete(selected)

            task_listbox.insert(
                selected,
                f"✓ {task}"
            )

            save_tasks()

    except:
        messagebox.showwarning(
            "Warning",
            "Please select a task!"
        )

# --------------------------
# GUI
# --------------------------

root = Tk()

root.title("To-Do List App")
root.geometry("500x500")
root.resizable(False, False)

title = Label(
    root,
    text="📋 To-Do List",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

task_entry = Entry(
    root,
    width=40,
    font=("Arial", 14)
)
task_entry.pack(pady=10)

Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
).pack(pady=5)

Button(
    root,
    text="Delete Task",
    width=20,
    command=delete_task
).pack(pady=5)

Button(
    root,
    text="Mark Completed",
    width=20,
    command=mark_completed
).pack(pady=5)

task_listbox = Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 12)
)
task_listbox.pack(pady=20)

load_tasks()

root.mainloop()