def main():
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level entered.")
            return

    # Modify the message if the task is time-bound
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Provide the reminder
    print("Reminder:", message)

# Execute the main function
if __name__ == "__main__":
    main()
