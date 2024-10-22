from tkinter import*
from tkinter import messagebox
from datetime import datetime, timedelta
import time
from playsound import playsound




tasks= []


def add_task():
    task={
        'title': title_Entry.get(),
        'description': description_Entry.get(),
        'priority': priority_Entry.get(),
        'dueDate': due_Date_Entry.get()
    }

    if task['title'] and task['dueDate']:
        try:
            # Check if the due date is in the correct format
            datetime.strptime(task['dueDate'], "%Y-%m-%d %H:%M")
            tasks.append(task)
            add_task_frame(task)
            title_Entry.delete(0, END)
            description_Entry.delete(0, END)
            priority_Entry.delete(0, END)
            due_Date_Entry.delete(0, END)
            task_window.destroy() # Close the task entry window after adding task
            check_empty_taskList() # Check if the task list is empty
        except ValueError:
            messagebox.showwarning("Warning", "Please enter the due date in the format YYYY-MM-DD HH:MM")
    else:
        messagebox.showwarning("Warning", "Please enter a task and due date.")

    
def add_task_frame(task):
    task_frame= Frame(task_container)
    task_frame.pack(fill=X, pady=2)

    task_var = BooleanVar()
    task_checkbutton = Checkbutton(task_frame, variable=task_var, command=lambda: mark_done(task_var, task_frame))
    task_checkbutton.pack(side=LEFT, padx=5)

    task_label = Label(task_frame, text=task['title'],font=("Arial", 12), bg="#97bff0" )
    task_label.pack(side=LEFT, padx=5)

    delete_button= Button(task_frame,image= deleteImage, command= lambda: delete_task(task, task_frame),bg="#97bff0" )
    delete_button.pack(side= RIGHT, padx=5)

    edit_button = Button(task_frame,image= editImage, command=lambda: editTask(task, task_frame), bg="#97bff0")
    edit_button.pack(side=RIGHT, padx=5)

    check_empty_taskList()


#edit window
def editTask(task, task_frame):
    global task_window, title_Entry, description_Entry, priority_Entry, due_Date_Entry

    task_window= Toplevel(window)
    task_window.title("Edit task")
    task_window.geometry("250x280")
    task_window.config(bg= "#b3d9f5")


    Label(task_window, text="Title:", bg= "#b3d9f5" ).pack()
    title_Entry = Entry(task_window, width=30)
    title_Entry.insert(0, task['title'])
    title_Entry.pack(padx=5, pady=5)

    Label(task_window, text="Description:", bg= "#b3d9f5").pack()
    description_Entry = Entry(task_window, width=30)
    description_Entry.insert(0, task['description'])
    description_Entry.pack(padx=5, pady=5)

    Label(task_window, text="Priority:", bg= "#b3d9f5").pack()
    priority_Entry = Entry(task_window, width=30)
    priority_Entry.insert(0, task['priority'])
    priority_Entry.pack(padx=5, pady=5)

    Label(task_window, text="Due Date:", bg= "#b3d9f5").pack()
    due_Date_Entry = Entry(task_window, width=30)
    due_Date_Entry.insert(0, task['dueDate'])
    due_Date_Entry.pack(padx=5, pady=5)

    save_button = Button(task_window, text="Save", command=lambda: save_task(task, task_frame), bg="#8cb6d4", font= 8)
    save_button.pack(pady=5)

def save_task(task, task_frame):
    task['title'] = title_Entry.get()
    task['description'] = description_Entry.get()
    task['priority'] = priority_Entry.get()
    task['dueDate'] = due_Date_Entry.get()

    try:
        # Validate the due date format
        datetime.strptime(task['dueDate'], "%Y-%m-%d %H:%M")

        for widget in task_frame.winfo_children():
            widget.destroy()

        task_checkbutton = Checkbutton(task_frame, variable=BooleanVar())
        task_checkbutton.pack(side=LEFT, padx=5)

        task_label = Label(task_frame, text=task['title'], font=("Arial", 12), bg="#97bff0")
        task_label.pack(side=LEFT, padx=5)

        delete_button = Button(task_frame, image=deleteImage, command=lambda: delete_task(task, task_frame), bg="#97bff0")
        delete_button.pack(side=RIGHT, padx=5)

        edit_button = Button(task_frame, image=editImage, command=lambda: editTask(task, task_frame), bg="#97bff0")
        edit_button.pack(side=RIGHT, padx=5)

        task_window.destroy()
    except ValueError:
        messagebox.showwarning("Warning", "Please enter the due date in the format YYYY-MM-DD HH:MM")


def delete_task(task, task_frame):
    tasks.remove(task)
    task_frame.destroy()
    check_empty_taskList()


def mark_done(task_var, task_frame):
    if task_var.get():
        task_frame.config(bg='lightgray')
    else:
        task_frame.config(bg='white')

#add task window
def open_task_window():
    global task_window
    task_window= Toplevel(window)
    task_window.title("Add task")
    task_window.geometry("250x280")
    task_window.config(bg= "#b3d9f5")
    

    global title_Entry, description_Entry, priority_Entry, due_Date_Entry

    Label(task_window, text="Title:",bg= "#b3d9f5" ).pack()
    title_Entry= Entry(task_window, width= 30 )
    title_Entry.pack(padx=5, pady= 5)

    Label(task_window, text="Description:" ,bg= "#b3d9f5").pack()
    description_Entry= Entry(task_window, width= 30)
    description_Entry.pack(padx=5, pady= 5)

    Label(task_window, text="Priority:" ,bg= "#b3d9f5").pack()
    priority_Entry= Entry(task_window, width= 30)
    priority_Entry.pack(padx=5, pady= 5)

    Label(task_window, text="Due Date:" ,bg= "#b3d9f5").pack()
    due_Date_Entry= Entry(task_window, width= 30)
    due_Date_Entry.pack(padx=5, pady= 5)

    addButton= Button(task_window, text= "Add Task", command= add_task, bg="#8cb6d4", font= 8)
    addButton.pack(pady= 5)

#plus button ko lagi
def circle_button(canvas, x, y, radius, text, command):
    circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#4f78e0", outline="")
    text = canvas.create_text(x, y, text=text, font=("Arial", 15, "bold"))
    canvas.tag_bind(circle, "<Button-1>", lambda event: command())

def check_empty_taskList():
    if not tasks:
        no_task_label.pack()
    else:
        no_task_label.pack_forget()


def check_due_dates():
    current_time = datetime.now()
    for task in tasks:
        try:
            due_date = datetime.strptime(task['dueDate'], "%Y-%m-%d %H:%M")
            if due_date <= current_time:
                show_reminder(task)
                tasks.remove(task) # Remove the task once the reminder is shown

        except ValueError:
            continue
    window.after(60000, check_due_dates) # Check every minute

def show_reminder(task):
    reminder_window = Toplevel(window)
    reminder_window.title("Task Reminder")
    reminder_window.geometry("250x150")
    reminder_window.config(bg="#b3d9f5")

    Label(reminder_window, text="Reminder!", bg="#b3d9f5", font=("Arial", 14, "bold")).pack(pady=10)
    Label(reminder_window, text=f"Task: {task['title']}", bg="#b3d9f5", font=("Arial", 12)).pack(pady=5)
    Label(reminder_window, text=f"Due: {task['dueDate']}", bg="#b3d9f5", font=("Arial", 12)).pack(pady=5)

    Button(reminder_window, text="Dismiss", command=reminder_window.destroy, bg="#b3d9f5").pack(pady=10)

    # Play a sound effect
    playsound(r'C:\Users\User\Downloads\alarm-clock-short-6402.mp3')   
    
            


window= Tk()
window.title("To-Do List")
window.geometry("375x812")
window.configure(bg="#9ab6db")

#images for edit and delete button
deleteImage= PhotoImage(file= 'C:\\Users\\User\\Downloads\\delete.png')
deleteImage= deleteImage.subsample(25,25)
editImage= PhotoImage(file= 'C:\\Users\\User\\Downloads\\edit.png')
editImage= editImage.subsample(25,25)

task_container = Frame(window)
task_container.pack(fill=BOTH, expand=True, padx=10, pady=10)

no_task_label = Label(task_container, text="You don't have any active task! ", font= 20)
no_task_label.pack(expand=True)  # initially show the label

bottom_canvas= Canvas(window, width=100, height= 100, bg="#9ab6db", highlightthickness=0)
bottom_canvas.pack(side="bottom",anchor= SE, padx=10,pady=10)


#plus button
circle_button(bottom_canvas, 70,70,30,"+", open_task_window)

# Start checking due dates
check_due_dates()

window.mainloop()