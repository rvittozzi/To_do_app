import tkinter as tk

root = tk.Tk()
root.title("To-Do List App")

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = int(selected_task[0])
        listbox.delete(index)
        tasks.pop(index)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

root.mainloop()
