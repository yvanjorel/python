import tkinter as tk
from tkinter import messagebox
import requests


class CourseApp:
    def __init__(self, master):
        self.master = master
        master.title("Course App")
        master.configure(bg="#F0F0F0") 
        
        
        self.course_id_label = tk.Label(master, text="Course ID:", font=("Arial", 12), bg="#F0F0F0")
        self.course_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.course_id_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.course_id_entry.grid(row=0, column=1, padx=10, pady=5)


        self.course_name_label = tk.Label(master, text="Course Name:", font=("Arial", 12), bg="#F0F0F0")
        self.course_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.course_name_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.course_name_entry.grid(row=1, column=1, padx=10, pady=5)
               
               
        self.add_button = tk.Button(master, text="Add Course", command=self.add_course, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.hours_label = tk.Label(master, text="Class Hours:", font=("Arial", 12, "bold"), bg="#F0F0F0")
        self.hours_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.hours_display = tk.Label(master, text="", font=("Arial", 12), bg="#F0F0F0")
        self.hours_display.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
            
    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        
        data = {
            "course_id": course_id,
            "course_name": course_name
        }
        
        response = requests.post("http://127.0.0.1:5000/add_course", json=data)
 
        if response.status_code == 200:
            message = response.json()["message"]
            messagebox.showinfo("Success", message)

            self.update_hours_display(course_name)
        else:
            messagebox.showerror("Error", "Failed to add course")




root = tk.Tk()
app = CourseApp(root)
root.mainloop()
