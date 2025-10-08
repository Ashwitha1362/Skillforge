import csv
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_csv(username, skills):
    if not skills:
        messagebox.showwarning("Warning", "No skills to export.")
        return
    filename = f"skills_{username}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["name", "category", "level"])
        writer.writeheader()
        writer.writerows(skills)
    messagebox.showinfo("Export Success", f"Skills exported to {filename}")

def export_pdf(username, skills):
    if not skills:
        messagebox.showwarning("Warning", "No skills to export.")
        return

    pdf_file = f"skills_{username}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(200, 750, f"SkillForge - {username}'s Skill Report")
    c.line(50, 740, 550, 740)

    y = 720
    for i, skill in enumerate(skills, start=1):
        text = f"{i}. {skill['name']} | {skill['category']} | {skill['level']}"
        c.drawString(50, y, text)
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()
    messagebox.showinfo("Export Success", f"Skills exported to {pdf_file}")