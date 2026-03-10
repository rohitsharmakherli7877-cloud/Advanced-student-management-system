# ===============================================
# Advanced Student Management System
# Developed By: Rohit Sharma
# Apex University
# ===============================================

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ------------------ DATABASE ------------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    marks INTEGER,
    grade TEXT
)
""")
conn.commit()

# ------------------ FUNCTIONS ------------------

def calculate_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    name = name_entry.get()
    course = course_entry.get()
    marks = marks_entry.get()

    if name == "" or course == "" or marks == "":
        messagebox.showerror("Error", "All fields required")
        return

    grade = calculate_grade(marks)

    cursor.execute("INSERT INTO students (name, course, marks, grade) VALUES (?, ?, ?, ?)",
                   (name, course, marks, grade))
    conn.commit()
    messagebox.showinfo("Success", "Student Added")
    clear_fields()
    view_students()

def view_students():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)
    total_label.config(text=f"Total Students: {len(rows)}")

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select student")
        return

    student = listbox.get(selected)
    cursor.execute("DELETE FROM students WHERE id=?", (student[0],))
    conn.commit()
    messagebox.showinfo("Deleted", "Student Deleted")
    view_students()

def search_student():
    name = name_entry.get()
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%'+name+'%',))
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)

def clear_fields():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# ------------------ LOGIN WINDOW ------------------

def login():
    if username_entry.get() == "Rohit" and password_entry.get() == "1234":
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Login Failed", "Wrong Username or Password")

login_window = tk.Tk()
login_window.title("Login - Rohit Sharma")
login_window.geometry("400x300")
login_window.config(bg="#1f4e79")

tk.Label(login_window, text="Admin Login",
         font=("Arial", 18, "bold"),
         bg="#1f4e79", fg="white").pack(pady=20)

tk.Label(login_window, text="Username", bg="#1f4e79", fg="white").pack()
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password", bg="#1f4e79", fg="white").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

tk.Button(login_window, text="Login", width=15, command=login).pack(pady=20)

# ------------------ MAIN WINDOW ------------------

def main_window():
    global name_entry, course_entry, marks_entry, listbox, total_label

    root = tk.Tk()
    root.title("Advanced Student Management - Rohit Sharma")
    root.state("zoomed")
    root.config(bg="#e6f2ff")

    tk.Label(root, text="Advanced Student Management System",
             font=("Arial", 22, "bold"),
             bg="#e6f2ff", fg="#003366").pack(pady=15)

    tk.Label(root, text="Student Name:", bg="#e6f2ff").pack()
    name_entry = tk.Entry(root, width=40)
    name_entry.pack(pady=5)

    tk.Label(root, text="Course:", bg="#e6f2ff").pack()
    course_entry = tk.Entry(root, width=40)
    course_entry.pack(pady=5)

    tk.Label(root, text="Marks:", bg="#e6f2ff").pack()
    marks_entry = tk.Entry(root, width=40)
    marks_entry.pack(pady=5)

    tk.Button(root, text="Add Student", width=20, command=add_student).pack(pady=5)
    tk.Button(root, text="View Students", width=20, command=view_students).pack(pady=5)
    tk.Button(root, text="Search Student", width=20, command=search_student).pack(pady=5)
    tk.Button(root, text="Delete Student", width=20, command=delete_student).pack(pady=5)

    listbox = tk.Listbox(root, width=100)
    listbox.pack(pady=20)

    total_label = tk.Label(root, text="Total Students: 0",
                           font=("Arial", 12, "bold"),
                           bg="#e6f2ff")
    total_label.pack()

    tk.Label(root, text="Developed By Rohit Sharma - Apex University",
             bg="#e6f2ff", fg="gray").pack(side="bottom", pady=10)

    view_students()
    root.mainloop()

login_window.mainloop()

