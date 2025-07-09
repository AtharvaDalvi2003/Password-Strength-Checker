import tkinter as tk
from tkinter import messagebox
import re

# Create main window
window = tk.Tk()
window.title("Password Strength Checker (Regex Based)")
window.geometry("500x470")
window.config(bg="#f4f6f9")

# GUI Header
head = tk.Label(window, text="🔐 Password Strength Checker", font=("Helvetica", 17, "bold"), bg="#f4f6f9", fg="#333")
head.pack(pady=15)

# Entry label
label = tk.Label(window, text="Enter Your Password", font=("Helvetica", 11, "bold"), bg="#f4f6f9")
label.pack()

# Entry field
entry = tk.Entry(window, show="*", font=("Helvetica", 11), width=30, bd=2, relief="groove")
entry.pack(pady=5)

# Toggle password visibility
show_password = False
def toggle_visibility():
    global show_password
    show_password = not show_password
    entry.config(show="" if show_password else "*")
    toggle_button.config(text="Hide Password" if show_password else "Show Password")

toggle_button = tk.Button(window, text="Show Password", font=("Helvetica", 9), command=toggle_visibility)
toggle_button.pack(pady=(0, 10))

# Check strength button
button = tk.Button(window, text="Check Strength", font=("Helvetica", 11), bg="#4287f5", fg="white", command=lambda: check())
button.pack(pady=5, ipadx=5, ipady=3)

# Strength bar canvas
w = tk.Canvas(window, height=100, width=400, bg="#f4f6f9", highlightthickness=0)
w.pack(pady=(10, 0))

# Result frame below canvas
result_frame = tk.Frame(window, bg="#f4f6f9")
result_frame.pack(pady=(0, 5))

# Strength label (percentage)
label1 = tk.Label(result_frame, text="", font=("Helvetica", 13, "bold"), bg="#f4f6f9", fg="black")
label1.pack()

# Strength message (e.g., Excellent password!)
strong_label = tk.Label(result_frame, text="", font=("Helvetica", 11), fg="green", bg="#f4f6f9")
strong_label.pack()

# Suggestion label
suggestion_label = tk.Label(window, text="", font=("Helvetica", 10), fg="#e63946", bg="#f4f6f9", justify="left", wraplength=380)
suggestion_label.pack(pady=(5, 0))

# Password strength evaluation
def evaluate_password(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"\d", pw): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw): score += 1
    return score

# Suggestions for improvement
def suggest_improvements(pw):
    suggestions = []
    if len(pw) < 8:
        suggestions.append("• Use at least 8 characters.")
    if not re.search(r"[A-Z]", pw):
        suggestions.append("• Add at least one uppercase letter.")
    if not re.search(r"[a-z]", pw):
        suggestions.append("• Include at least one lowercase letter.")
    if not re.search(r"\d", pw):
        suggestions.append("• Add at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        suggestions.append("• Use at least one special character (!@#...).")
    return "\n".join(suggestions)

# Check password strength
def check():
    w.delete("all")
    label1["text"] = ""
    strong_label["text"] = ""
    suggestion_label["text"] = ""

    pw = entry.get()

    if pw == "":
        messagebox.showinfo("Error", "Password can't be empty")
        return

    score = evaluate_password(pw)
    percent = int((score / 5) * 100)
    label1["text"] = f"{percent} %"

    if score == 5:
        w.create_rectangle(50, 30, 350, 70, fill="#27cf54", outline="white")
        strong_label["text"] = "✅ Excellent password!"
        strong_label.config(fg="green")
    elif 3 <= score < 5:
        w.create_rectangle(50, 30, 350, 70, fill="#f0f007", outline="white")
        strong_label["text"] = "🟡 Good, but could be stronger."
        strong_label.config(fg="orange")
        suggestion_label["text"] = suggest_improvements(pw)
    else:
        w.create_rectangle(50, 30, 350, 70, fill="#de3c3c", outline="white")
        strong_label["text"] = "❌ Weak password."
        strong_label.config(fg="red")
        suggestion_label["text"] = suggest_improvements(pw)

# Run GUI loop
window.mainloop()
