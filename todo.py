"""
Allow the user to add tasks to a to-do list.
Allow the user to view their current to-do list.
Allow the user to mark tasks as completed and remove them from the list.
"""

task = []

print("Welcome to the To-Do List App!\n")


def printTasks():
    with open("./tasks.txt", "r") as f:
        print(f.read())


def addTask():
    while True:
        userin = input("Add a task: ")
        task.append(userin)

        while True:
            prompt = input("Do you want to add more task (y/n): ")
            if prompt.upper() == "N":
                return
            elif prompt.upper() == "Y":
                break
            else:
                print("The input must be either (y/n).")


def listToString(task):
    return "\n".join(task) + "\n"


with open("./tasks.txt", "a") as f:
    f.write(listToString(task))

print("Tasks saved.")
