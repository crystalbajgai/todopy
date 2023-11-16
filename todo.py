"""
Allow the user to add tasks to a to-do list.
Allow the user to view their current to-do list.
Allow the user to mark tasks as completed and remove them from the list.
"""

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


def main():
    print("Please select one of the following options: ")
    print("1. View to-do list")
    print("2. Add task to to-do list")
    print("3. Mark task as completed")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        printTasks()
    elif choice == "2":
        addTask()
    # elif choice == "3":
    # print("Mark task as completed")
    # elif choice == "4":
    # print("Exit")
    else:
        print("Invalid input. Please try again.")


def printTasks():
    with open("./tasks.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


main()
