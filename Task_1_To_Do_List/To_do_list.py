import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must add a task")


#Creating the GUI
listbox_tasks = tkinter.Listbox(root, height = 10, width = 50)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width = 48, command=add_task)
button_add_task.pack()










root.mainloop()