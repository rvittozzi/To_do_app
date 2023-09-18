import tkinter as tk
import time

root = tk.Tk()
root.title("To-Do List App")

# Function to save tasks and task history to a text file
def save_to_file():
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n".join(tasks))

def load_from_file():
    try:
        with open("tasks.txt", "r") as task_file:
            saved_tasks = task_file.read().splitlines()
        return saved_tasks
    except FileNotFoundError:
        return []

tasks = []
task_history = load_from_file()  # Load task history from the file at the beginning of the program

def add_task():
    task = entry.get()
    time = time_entry.get()  # Get the time for the task
    if task:
        task_with_time = f"{task} (Time: {time})" if time else task  # Add time if provided
        tasks.append(task_with_time)
        listbox.insert(tk.END, task_with_time)
        entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)  # Clear the time entry field
        save_to_file()  # Save the updated tasks to the file

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = int(selected_task[0])
        listbox.delete(index)
        task_history.append(tasks.pop(index))  # Move removed task to history
        save_to_file()  # Save the updated tasks and task history to the file

def clear_history():
    listbox_history.delete(0, tk.END)
    task_history.clear()
    save_to_file()  # Save the cleared task history to the file

def show_history():
    listbox_history.delete(0, tk.END)
    for task in task_history:
        listbox_history.insert(tk.END, task)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

time_label = tk.Label(root, text="Time for Task (optional):")
time_label.pack()

time_entry = tk.Entry(root, width=30)
time_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

history_label = tk.Label(root, text="Task History:")
history_label.pack()

listbox_history = tk.Listbox(root, width=40)
listbox_history.pack()

clear_history_button = tk.Button(root, text="Clear History", command=clear_history)
clear_history_button.pack()

show_history_button = tk.Button(root, text="Show History", command=show_history)
show_history_button.pack()

clock_label = tk.Label(root, text="", font=("Arial", 14))
clock_label.pack()

def update_clock():
    current_time = time.strftime("%H:%M")  # Display time in HH:MM format
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

update_clock()
# run loop
root.mainloop()