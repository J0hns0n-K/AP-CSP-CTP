import tkinter as tk

subjects = [
    {"name": "Math", "goal": 60, "studied": 0},
    {"name": "Science", "goal": 45, "studied": 0}
]

def find_subject(subject_name):
    for subject in subjects:
        if subject["name"].lower() == subject_name.lower():
            return subject
    return None

def calculate_overall_progress():
    total_goal = 0
    total_studied = 0

    for subject in subjects:
        total_goal += subject["goal"]
        total_studied += subject["studied"]

    if total_goal == 0:
        return 0

    return int((total_studied / total_goal) * 100)

def get_progress_status(subject):
    pct = (subject["studied"] / subject["goal"]) * 100

    if pct >= 100:
        return "Done"
    elif pct >= 50:
        return "Halfway"
    else:
        return "Keep going"

def add_subject(name, goal):
    if goal <= 0:
        return "Goal must be > 0"

    if find_subject(name):
        return "Already exists"

    subjects.append({"name": name, "goal": goal, "studied": 0})
    return "Added"

def log_study_time(name, minutes):
    if minutes < 0:
        return "No negative time"

    subject = find_subject(name)

    if subject:
        subject["studied"] += minutes

        if subject["studied"] >= subject["goal"]:
            subject["studied"] = subject["goal"]
            return "Done"

        return f"{subject['goal'] - subject['studied']} min left"

    return "Not found"

# ---------- UI ----------
def render_subjects():
    for w in subject_frame.winfo_children():
        w.destroy()

    for subject in subjects:
        pct = int((subject["studied"] / subject["goal"]) * 100)
        status = get_progress_status(subject)

        card = tk.Frame(subject_frame, bg="white", highlightbackground="#ddd", highlightthickness=1)
        card.pack(fill="x", pady=6)

        inner = tk.Frame(card, bg="white", padx=12, pady=10)
        inner.pack(fill="x")

        top = tk.Frame(inner, bg="white")
        top.pack(fill="x")

        tk.Label(top, text=subject["name"], font=("Arial", 13, "bold"), bg="white").pack(side="left")

        tk.Label(top, text=status, bg="white", fg="#1D9E75").pack(side="right")

        tk.Label(inner, text=f"{subject['studied']}/{subject['goal']} min",
                 bg="white", fg="#666").pack(anchor="w")

        bar_bg = tk.Frame(inner, bg="#e0e0e0", height=6)
        bar_bg.pack(fill="x", pady=6)
        bar_bg.pack_propagate(False)

        fill = tk.Frame(bar_bg, bg="#1D9E75")
        fill.place(relwidth=(pct/100 if pct > 0 else 0), relheight=1)

    overall_label.config(text=f"Overall Progress: {calculate_overall_progress()}%")

def add_placeholder(entry, text):
    def on_focus_in(e):
        if entry.get() == text:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(e):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="gray")

    entry.insert(0, text)
    entry.config(fg="gray")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def handle_add():
    name = add_name.get().strip()

    try:
        goal = int(add_goal.get())
    except:
        add_msg.config(text="Enter number")
        return

    result = add_subject(name, goal)
    add_msg.config(text=result)
    render_subjects()

    add_name.delete(0, tk.END)
    add_goal.delete(0, tk.END)
    add_name.focus()

def handle_log():
    name = log_name.get().strip()

    try:
        minutes = int(log_min.get())
    except:
        log_msg.config(text="Enter number")
        return

    result = log_study_time(name, minutes)
    log_msg.config(text=result)
    render_subjects()

    log_name.delete(0, tk.END)
    log_min.delete(0, tk.END)
    log_name.focus()

root = tk.Tk()
root.title("Study Tracker")
root.geometry("460x650")
root.configure(bg="#f5f5f0")

main = tk.Frame(root, bg="#f5f5f0", padx=20, pady=20)
main.pack(fill="both", expand=True)

tk.Label(main, text="Study Tracker",
         font=("Arial", 18, "bold"),
         bg="#f5f5f0").pack(anchor="w")

overall_label = tk.Label(main, text="Overall Progress: 0%",
                         font=("Arial", 11),
                         bg="#f5f5f0", fg="#666")
overall_label.pack(anchor="w", pady=(0, 10))

subject_frame = tk.Frame(main, bg="#f5f5f0")
subject_frame.pack(fill="both", expand=True)

# ---------- Add ----------
add_card = tk.Frame(main, bg="white", highlightbackground="#ddd", highlightthickness=1)
add_card.pack(fill="x", pady=10)

add_inner = tk.Frame(add_card, bg="white", padx=12, pady=10)
add_inner.pack(fill="x")

tk.Label(add_inner, text="Add Subject", bg="white", fg="#888").pack(anchor="w")

add_name = tk.Entry(add_inner)
add_name.pack(fill="x", pady=4)

add_goal = tk.Entry(add_inner)
add_goal.pack(fill="x", pady=4)

add_placeholder(add_name, "Subject name")
add_placeholder(add_goal, "Goal (minutes)")

tk.Button(add_inner, text="Add",
          bg="#1D9E75", fg="white",
          relief="flat",
          command=handle_add).pack(pady=5)

add_msg = tk.Label(add_inner, bg="white", fg="#666")
add_msg.pack(anchor="w")

log_card = tk.Frame(main, bg="white", highlightbackground="#ddd", highlightthickness=1)
log_card.pack(fill="x")

log_inner = tk.Frame(log_card, bg="white", padx=12, pady=10)
log_inner.pack(fill="x")

tk.Label(log_inner, text="Log Study Time", bg="white", fg="#888").pack(anchor="w")

log_name = tk.Entry(log_inner)
log_name.pack(fill="x", pady=4)

log_min = tk.Entry(log_inner)
log_min.pack(fill="x", pady=4)

add_placeholder(log_name, "Subject name")
add_placeholder(log_min, "Minutes studied")

tk.Button(log_inner, text="Log",
          bg="#1D9E75", fg="white",
          relief="flat",
          command=handle_log).pack(pady=5)

log_msg = tk.Label(log_inner, bg="white", fg="#666")
log_msg.pack(anchor="w")

add_name.bind("<Return>", lambda e: add_goal.focus())
add_goal.bind("<Return>", lambda e: handle_add())

log_name.bind("<Return>", lambda e: log_min.focus())
log_min.bind("<Return>", lambda e: handle_log())

render_subjects()
root.mainloop()