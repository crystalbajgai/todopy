task = []

print("Welcome to the To-Do List App!\n")


def addTask():
    with open("./tasks.txt", "a") as f:
        while True:
            userin = input("Add a task: ")
            task.append(userin)
            f.write(userin + "\n")
            print("Tasks saved.")

            while True:
                prompt = input("Do you want to add more task (y/n): ")
                if prompt.upper() == "N":
                    return
                elif prompt.upper() == "Y":
                    break
                else:
                    print("The input must be either (y/n).")


def printTasks():
    with open("./tasks.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")


def removeTask():
    printTasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    with open("./tasks.txt", "r") as f:
        tasks = f.readlines()

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        with open("./tasks.txt", "w") as f:
            for task in tasks:
                f.write(task)
        print("Task removed.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("Please select one of the following options: ")
        print("1. View to-do list")
        print("2. Add task to to-do list")
        print("3. Remove task from to-do list")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print()
            print("Tasks: ")
            printTasks()
            print()
        elif choice == "2":
            print()
            addTask()
            print()
        elif choice == "3":
            removeTask()
            print()
        elif choice == "4":
            exit()
        else:
            print("Invalid input. Please try again.")


main()
