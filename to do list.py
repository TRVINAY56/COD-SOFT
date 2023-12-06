import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(master, width=30)
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)

        # Pack GUI elements
        self.task_entry.pack(pady=10)
        self.add_button.pack()
        self.task_listbox.pack(pady=10)
        self.delete_button.pack()

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append(task_description)
            self.task_listbox.insert(tk.END, task_description)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main application window
root = tk.Tk()

# Initialize the TodoApp
todo_app = TodoApp(root)

# Start the application main loop
root.mainloop()
