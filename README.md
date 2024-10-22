# To-Do List with Reminders

## Overview
This project is a To-Do List application built using Python and Tkinter. It allows users to add tasks with details such as title, description, priority, and due date. The application also has features like task editing, task deletion, and automatic reminders for overdue tasks, accompanied by sound alerts.

## Features
- **Add Tasks**: Add new tasks with title, description, priority, and due date.
- **Edit Tasks**: Modify existing tasks' details.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Mark as Complete**: Mark tasks as done by checking the checkbox.
- **Reminder for Due Tasks**: The application checks for tasks' due dates every minute and shows a pop-up reminder for overdue tasks along with an alarm sound.
- **Dynamic Task List**: Task list updates dynamically as tasks are added, edited, or deleted.
- **Customizable UI**: Features an attractive and user-friendly interface with task buttons and animated task addition.

## Technologies Used
- **Python**: Core programming language for logic.
- **Tkinter**: Used for creating the graphical user interface (GUI).
- **Playsound**: To play sound alerts when a task is due.
- **Datetime**: To handle task due dates and reminders.

## How to Use
1. **Install Dependencies**:
   - Install the `playsound` package using:
     ```bash
     pip install playsound
     ```
2. **Run the Application**:
   - Download or clone the repository.
   - Make sure you have the necessary image and sound files in place.
   - Run the Python script:
     ```bash
     python todo_list.py
     ```
3. **Add Tasks**:
   - Click on the "+" button to open the task addition window.
   - Fill in the title, description, priority, and due date (in `YYYY-MM-DD HH:MM` format).
   - Click "Add Task" to save the task.
4. **Edit or Delete Tasks**:
   - Use the edit and delete icons to modify or remove tasks.
5. **Reminder Alerts**:
   - When a task's due date arrives, a pop-up reminder will appear, and an alarm sound will play.

## File Structure
- **main.py**: Contains the core logic of the To-Do List application.
- **delete.png**: The image used for the delete button.
- **edit.png**: The image used for the edit button.
- **alarm-clock-short-6402.mp3**: The sound file for the reminder alert.

## Future Enhancements
- **Recurring Tasks**: Add support for recurring tasks (daily, weekly, monthly).
- **Task Categorization**: Group tasks by categories or tags for better organization.
- **Task Filtering**: Allow users to filter tasks based on priority or due date.
- **Notification Settings**: Let users customize the type of reminder alerts (e.g., sound, pop-up).
