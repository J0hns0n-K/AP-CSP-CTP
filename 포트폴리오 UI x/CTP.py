subjects = [
    {"name": "Math", "goal": 60, "studied": 0},
    {"name": "Science", "goal": 45, "studied": 0}
]

def log_study_time(subject_name, minutes):
    if minutes < 0:
        print("Study time cannot be negative.")
        return

    for subject in subjects:
        if subject["name"].lower() == subject_name.lower():
            subject["studied"] += minutes

            if subject["studied"] >= subject["goal"]:
                subject["studied"] = subject["goal"]
                print(subject["name"] + ": Goal achieved! You studied " + str(subject["studied"]) + " minutes.")
            else:
                remaining = subject["goal"] - subject["studied"]
                print(subject["name"] + ": Keep going! " + str(remaining) + " minutes left.")

            return

    print("Error: " + subject_name + " is not found. Please add the subject first.")


def add_subject(subject_name, goal):
    if goal <= 0:
        print("Goal must be greater than 0.")
        return

    for subject in subjects:
        if subject["name"].lower() == subject_name.lower():
            print("Subject already exists.")
            return

    subjects.append({
        "name": subject_name,
        "goal": goal,
        "studied": 0
    })

    print(subject_name + " has been added with a goal of " + str(goal) + " minutes.")


def show_subjects():
    if not subjects:
        print("No subjects added yet.")
        return

    print("\n📚 Current Subjects:")
    for subject in subjects:
        print(f"- {subject['name']}: {subject['studied']}/{subject['goal']} minutes")


print("Study Time Management App")

while True:
    print("\n1. Add subject and target time")
    print("2. Log study time")
    print("3. Show subjects")
    print("4. Quit")

    choice = input(": ")

    if choice == "1":
        name = input("Enter subject name: ")

        try:
            goal = int(input("Enter goal time (minutes): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        add_subject(name, goal)

    elif choice == "2":
        name = input("Enter subject name: ")

        try:
            minutes = int(input("Enter study time (minutes): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        log_study_time(name, minutes)

    elif choice == "3":
        show_subjects()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")