# 🚀 SkillForge - Personal Skill Growth Tracker

SkillForge is a personal skill management and growth tracking application built with Python and Tkinter. It allows users to track their skills, categorize them, assign proficiency levels, and generate professional reports in CSV and PDF formats.

## ✨ Features

* User Authentication: Secure registration and login system.
* Skill Management (CRUD): Easily C**reate, **R**ead, **U**pdate, and **D**elete skills.
* **Skill Tracking: Track skill name, category, and proficiency level (Beginner, Intermediate, Advanced).
* Data Persistence: User and skill data are saved locally using JSON files.
* Filtering: Filter skills by category or proficiency level.
* Analytics: View a summary of skills grouped by category and level.
* Professional Export: Export your skill report to CSV and PDF formats using csv and reportlab.
* Intuitive GUI: A clean, color-coded graphical user interface built with Tkinter and ttk.

## 🛠 Installation and Setup

### Prerequisites

You need Python 3.x installed on your system.

SkillForge relies on the following Python packages:

* tkinter (usually bundled with Python)
* reportlab (for PDF export)

### Steps

1.  Clone the Repository:
        git clone [https://github.com/YourUsername/SkillForge.git](https://github.com/YourUsername/SkillForge.git)
    cd SkillForge
    

2.  Install Dependencies:
        pip install reportlab
    

3.  Run the Application:
        python skillforge.py # Assuming your file is named skillforge.py
    

## 🖥 How to Use

### 1. Login/Register

When you first open the app, you'll be presented with the Login screen.

* New Users: Click Register to create a new username and password.
* Returning Users: Enter your credentials and click Login.

### 2. Main Skill Tracker

Once logged in, you can manage your skills:

* Add Skill: Click Add Skill to enter a new skill name, category, and level.
* Update Skill: Select a skill from the list and click Update Skill to modify its details.
* Delete Skill: Select a skill and click Delete Skill to remove it.
* Filter Skills: Click Filter Skills to search for skills based on category or level.
* Summary Analytics: Click Summary Analytics to view a breakdown of your skills by category and proficiency level.

### 3. Exporting Reports

Use the dedicated buttons to generate professional reports of your current skills:

* Export CSV: Creates a file named skills_YOURUSERNAME.csv.
* Export PDF: Creates a file named skills_YOURUSERNAME.pdf.

### 4. Logout

Click Logout to return to the login screen and protect your data.

## 📂 Project Structure
