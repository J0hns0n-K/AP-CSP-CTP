# This code was co-created with the assistance of Claude (Anthropic).

subjects = [
    {"name": "Math", "goal": 60, "studied": 0},
    {"name": "Science", "goal": 45, "studied": 0}
]

def log_study_time(subject_name, minutes):
    for subject in subjects:
        if subject["name"] == subject_name:
            subject["studied"] = subject["studied"] + minutes
            if subject["studied"] >= subject["goal"]:
                msg = subject_name + ": Goal achieved! You studied "
                msg = msg + str(subject["studied"]) + " minutes."
                print(msg)
            else:
                remaining = subject["goal"] - subject["studied"]
                msg = subject_name + ": Keep going! "
                msg = msg + str(remaining) + " minutes left."
                print(msg)
            return

    print("Error: " + subject_name + " is not found. Please add the subject first.")

def add_subject(subject_name, goal):
    subjects.append({
        "name": subject_name,
        "goal": goal,
        "studied": 0
    })
    msg = subject_name + " has been added with a goal of "
    print(msg + str(goal) + " minutes.")

print("Study Time Management App")

while True:
    print("\n1. Add subject and target time")
    print("2. Log study time")
    print("3. Quit")
    choice = input(": ")

    if choice == "1":
        name = input("Enter subject name: ")
        goal = int(input("Enter goal time (minutes): "))
        add_subject(name, goal)

    elif choice == "2":
        name = input("Enter subject name: ")
        minutes = int(input("Enter study time (minutes): "))
        log_study_time(name, minutes)

    elif choice == "3":
        print("Goodbye!")
        break
