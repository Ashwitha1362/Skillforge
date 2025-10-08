import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from users import load_users, save_users
from skills import load_skills, save_skills
from export_utils import export_csv, export_pdf


class SkillForgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SkillForge - Personal Skill Growth Tracker")
        self.root.geometry("750x500")
        self.username = None
        self.skills = []

        self.root.configure(bg="#f4f6f7")
        self.style = ttk.Style()
        self.style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="black")
        self.style.map("Treeview", background=[("selected", "#3498db")])

        self.create_login_screen()

    # ------------------ Login/Register ------------------
    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#1abc9c")

        frame = tk.Frame(self.root, bg="#1abc9c")
        frame.pack(expand=True)

        tk.Label(frame, text="SkillForge Login", font=("Arial", 18, "bold"), bg="#1abc9c", fg="white").pack(pady=10)

        tk.Label(frame, text="Username:", bg="#1abc9c", fg="white").pack()
        self.username_entry = tk.Entry(frame, bg="#ecf0f1", fg="black")
        self.username_entry.pack()

        tk.Label(frame, text="Password:", bg="#1abc9c", fg="white").pack()
        self.password_entry = tk.Entry(frame, show="*", bg="#ecf0f1", fg="black")
        self.password_entry.pack()

        tk.Button(frame, text="Login", bg="#3498db", fg="white", command=self.login).pack(pady=5)
        tk.Button(frame, text="Register", bg="#2ecc71", fg="white", command=self.register).pack(pady=5)

    def login(self):
        users = load_users()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username] == password:
            self.username = username
            self.skills = load_skills(username)
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        users = load_users()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users:
            messagebox.showerror("Error", "Username already exists")
            return
        if not username or not password:
            messagebox.showerror("Error", "Enter both username and password")
            return

        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "Registration successful! Please log in.")

    # ------------------ Main Screen ------------------
    def create_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#34495e")

        tk.Label(self.root, text=f"Welcome {self.username}!", font=("Arial", 16, "bold"), bg="#34495e", fg="white").pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Name", "Category", "Level"), show="headings")
        self.tree.heading("Name", text="Skill Name")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Level", text="Level")
        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        self.load_tree()

        frame = tk.Frame(self.root, bg="#34495e")
        frame.pack(pady=10)

        tk.Button(frame, text="Add Skill", bg="#2980b9", fg="white", command=self.add_skill).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Update Skill", bg="#f39c12", fg="white", command=self.update_skill).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Delete Skill", bg="#e74c3c", fg="white", command=self.delete_skill).grid(row=0, column=2, padx=5)

        tk.Button(frame, text="Filter Skills", bg="#9b59b6", fg="white", command=self.filter_skills).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Summary Analytics", bg="#16a085", fg="white", command=self.show_summary).grid(row=0, column=4, padx=5)

        tk.Button(frame, text="Export CSV", bg="#27ae60", fg="white", command=lambda: export_csv(self.username, self.skills)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Export PDF", bg="#8e44ad", fg="white", command=lambda: export_pdf(self.username, self.skills)).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(frame, text="Settings", bg="#d35400", fg="white", command=self.open_settings).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="Logout", bg="#95a5a6", fg="black", command=self.create_login_screen).grid(row=1, column=3, padx=5, pady=5)

    def load_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for skill in self.skills:
            self.tree.insert("", "end", values=(skill["name"], skill["category"], skill["level"]))

    # ------------------ CRUD ------------------
    def add_skill(self):
        name = simpledialog.askstring("Input", "Enter skill name:")
        category = simpledialog.askstring("Input", "Enter category:")
        level = simpledialog.askstring("Input", "Enter level (Beginner/Intermediate/Advanced):")
        if name and category and level:
            self.skills.append({"name": name, "category": category, "level": level})
            save_skills(self.username, self.skills)
            self.load_tree()

    def update_skill(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a skill to update")
            return
        index = self.tree.index(selected[0])
        skill = self.skills[index]

        skill["name"] = simpledialog.askstring("Input", "Enter new skill name:", initialvalue=skill["name"])
        skill["category"] = simpledialog.askstring("Input", "Enter new category:", initialvalue=skill["category"])
        skill["level"] = simpledialog.askstring("Input", "Enter new level:", initialvalue=skill["level"])

        save_skills(self.username, self.skills)
        self.load_tree()

    def delete_skill(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a skill to delete")
            return
        index = self.tree.index(selected[0])
        del self.skills[index]
        save_skills(self.username, self.skills)
        self.load_tree()

    # ------------------ Filters & Analytics ------------------
    def filter_skills(self):
        category = simpledialog.askstring("Filter", "Enter category to filter (leave blank for all):")
        level = simpledialog.askstring("Filter", "Enter level to filter (Beginner/Intermediate/Advanced):")

        filtered = self.skills
        if category:
            filtered = [s for s in filtered if s["category"].lower() == category.lower()]
        if level:
            filtered = [s for s in filtered if s["level"].lower() == level.lower()]

        if not filtered:
            messagebox.showinfo("Result", "No skills found for this filter")
        else:
            result = "\n".join([f"{s['name']} - {s['category']} - {s['level']}" for s in filtered])
            messagebox.showinfo("Filtered Skills", result)

    def show_summary(self):
        if not self.skills:
            messagebox.showinfo("Summary", "No skills added yet.")
            return

        categories = {}
        levels = {}
        for s in self.skills:
            categories[s["category"]] = categories.get(s["category"], 0) + 1
            levels[s["level"]] = levels.get(s["level"], 0) + 1

        summary = "📊 Skill Summary:\n\nBy Category:\n"
        for c, count in categories.items():
            summary += f"  {c}: {count}\n"
        summary += "\nBy Level:\n"
        for l, count in levels.items():
            summary += f"  {l}: {count}\n"

        messagebox.showinfo("Summary Analytics", summary)

    # ------------------ Settings ------------------
    def open_settings(self):
        choice = messagebox.askyesno("Settings", "Do you want to clear all skills?")
        if choice:
            self.skills = []
            save_skills(self.username, self.skills)
            self.load_tree()
