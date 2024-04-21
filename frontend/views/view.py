import tkinter as tk
from tkinter import messagebox
import requests


class App:
    def __init__(self, master):
        self.master = master
        master.title("App")
        master.configure(bg="#F0F0F0") 
        

        self.class_hours = {}
        

        self.teacher_id_label = tk.Label(master, text="Teacher ID:", font=("Arial", 12), bg="#F0F0F0")
        self.teacher_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.teacher_id_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.teacher_id_entry.grid(row=0, column=1, padx=10, pady=5)
        

        self.teacher_name_label = tk.Label(master, text="Teacher's Name:", font=("Arial", 12), bg="#F0F0F0")
        self.teacher_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.teacher_name_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.teacher_name_entry.grid(row=1, column=1, padx=10, pady=5)
        

        self.subject_label = tk.Label(master, text="Subject:", font=("Arial", 12), bg="#F0F0F0")
        self.subject_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.subject_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.subject_entry.grid(row=2, column=1, padx=10, pady=5)
        

        self.class_label = tk.Label(master, text="Class:", font=("Arial", 12), bg="#F0F0F0")
        self.class_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.class_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.class_entry.grid(row=3, column=1, padx=10, pady=5)
        

        self.add_button = tk.Button(master, text="Submit", command=self.submit, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)


        self.hours_label = tk.Label(master, text="Class Hours:", font=("Arial", 12, "bold"), bg="#F0F0F0")
        self.hours_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.hours_display = tk.Label(master, text="", font=("Arial", 12), bg="#F0F0F0")
        self.hours_display.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
    def submit(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        subject = self.subject_entry.get()
        class_name = self.class_entry.get()
        

        data = {
            "teacher_id": teacher_id,
            "teacher_name": teacher_name,
            "subject": subject,
            "class_name": class_name
        }
        

        response = requests.post("http://127.0.0.1:5000/add_subject", json=data)
        

        if response.status_code == 200:
            message = response.json()["message"]
            messagebox.showinfo("Success", message)

            self.update_hours_display(class_name)
        else:
            messagebox.showerror("Error", "Failed to add subject")
            
    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.subject_entry.get()
        
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
            messagebox.showerror("Error", "Failed to add subject")


    def update_hours_display(self, class_name):
        # This method remains the same
        pass

root = tk.Tk()
app = App(root)
root.mainloop()
