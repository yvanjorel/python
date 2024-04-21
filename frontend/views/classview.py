import tkinter as tk
from tkinter import messagebox
import requests


class ClassApp:
    def __init__(self, master):
        self.master = master
        master.title("Class App")
        master.configure(bg="#F0F0F0") 
        
        
        self.class_id_label = tk.Label(master, text="Class ID:", font=("Arial", 12), bg="#F0F0F0")
        self.class_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.class_id_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.class_id_entry.grid(row=0, column=1, padx=10, pady=5)


        self.class_name_label = tk.Label(master, text="Class Name:", font=("Arial", 12), bg="#F0F0F0")
        self.class_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.class_name_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.class_name_entry.grid(row=1, column=1, padx=10, pady=5)
               
               
        self.add_button = tk.Button(master, text="Add Class", command=self.add_class, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.hours_label = tk.Label(master, text="Class Hours:", font=("Arial", 12, "bold"), bg="#F0F0F0")
        self.hours_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.hours_display = tk.Label(master, text="", font=("Arial", 12), bg="#F0F0F0")
        self.hours_display.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
            
    def add_class(self):
        class_id = self.class_id_entry.get()
        class_name = self.class_name_entry.get()
        
        data = {
            "id": class_id,
            "class_name": class_name
        }
        
        response = requests.post("http://127.0.0.1:5000/add_class", json=data)
 
        if response.status_code == 200:
            message = response.json()["message"]
            messagebox.showinfo("Success", message)

            self.update_hours_display(class_name)
        else:
            messagebox.showerror("Error", "Failed to add class")



root = tk.Tk()
app = ClassApp(root)
root.mainloop()
