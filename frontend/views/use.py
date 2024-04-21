import tkinter as tk
from tkinter import messagebox
import requests


def get_classes():
    try:
        response = requests.get("http://127.0.0.1:5000/get_classes")
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()['classes']
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch classes: {e}")
        return []

def get_courses_for_class(class_id):
    response = requests.get(f"http://127.0.0.1:5000/classes/{class_id}/get_courses_for_class")
    if response.status_code == 200:
        return response.json()['courses']
    else:
        messagebox.showerror("Error", "Failed to fetch courses for class")

def get_course_id(class_id, course_name):
    response = requests.get(f"http://127.0.0.1:5000/classes/{class_id}/courses")
    if response.status_code == 200:
        courses = response.json()['courses']
        for course in courses:
            if course['course_name'] == course_name:
                return course['id']
    messagebox.showerror("Error", "Failed to get course ID")

def increment_hours(class_id, course_id):
    response = requests.post(f"http://127.0.0.1:5000/classes/{class_id}/courses/{course_id}/increment-hours")
    if response.status_code == 200:
        messagebox.showinfo("Success", "Hours incremented successfully")
    else:
        messagebox.showerror("Error", "Failed to increment hours")

root = tk.Tk()
root.geometry("800x400")

classes = get_classes()

class_var = tk.StringVar(root)
class_var.set(classes[0]['class_name'])  # Set default class

class_label = tk.Label(root, text="Select Class:")
class_label.pack()

class_option_menu = tk.OptionMenu(root, class_var, *[c['class_name'] for c in classes])
class_option_menu.pack()

def get_class_id(class_name):
    for c in classes:
        if c['class_name'] == class_name:
            return c['id']

def update_courses_dropdown(class_id):
    courses = get_courses_for_class(class_id)
    course_var.set(courses[0]['course_name'])
    course_menu = course_option_menu['menu']
    course_menu.delete(0, 'end')
    for course in courses:
        course_menu.add_command(label=course['course_name'], command=tk._setit(course_var, course['course_name']))

def on_button_click():
    class_id = get_class_id(class_var.get())
    course_name = course_var.get()
    course_id = get_course_id(class_id, course_name)
    increment_hours(class_id, course_id)

course_var = tk.StringVar(root)
course_label = tk.Label(root, text="Select Course:")
course_label.pack()

course_option_menu = tk.OptionMenu(root, course_var, "")
course_option_menu.pack()

class_var.trace("w", lambda name, index, mode, sv=class_var: update_courses_dropdown(get_class_id(class_var.get())))

button = tk.Button(root, text="Increment Hours", command=on_button_click)
button.pack()

root.mainloop()
