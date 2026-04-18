import os
FILE_NAME = "list.txt"
def add():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return[line.strip() for line in file.readlines()]
    return []

def save(list):
    with open(FILE_NAME, "w") as file:
        for item in list:
            file.write(item + "\n")

def show(list):
    if not list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, item in enumerate(list, start=1):
            print(f"{index}. {item}")
        print()

task = add()

while True:
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new = input("Enter a new task: ")
        task.append(new)
        save(task)
        print("Task added successfully!\n")
    elif choice == "2":
        show(task)
    elif choice == "3":
        show(task)
        try:
            index = int(input("Enter the task number to update: ")) - 1
            if 0 <= index < len(task):
                new_task = input("Enter the new task: ")
                task[index] = new_task
                save(task)
                print("Task updated successfully!\n")
            else:
                print("Invalid task number.\n")
        except :
            print("Please enter a valid number.\n")
        
    elif choice == "4":
        show(task)
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(task):
                removed_task = task.pop(index)
                save(task)
                print(f"Task '{removed_task}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except :
            print("Please enter a valid number.\n")
        
        
    elif choice == "5":     
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")