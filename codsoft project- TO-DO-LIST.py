tasks = [] 

def show_menu():
    print("\n------ TO-DO LIST MENU ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------------")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        t = input("Write your task: ")
        tasks.append(t)
        print("Task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet...")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to update...")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
            pos = int(input("Which task number to update? ")) - 1
            if pos >= 0 and pos < len(tasks):
                new_task = input("Enter new task: ")
                tasks[pos] = new_task
                print("Task updated!")
            else:
                print("Invalid task number!")
    elif choice == "4":
        if len(tasks) == 0:
            print("Nothing to delete...")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
            pos = int(input("Which task number to delete? ")) - 1
            if pos >= 0 and pos < len(tasks):
                tasks.pop(pos)
                print("Task deleted!")
            else:
                print("Invalid task number!")
    elif choice == "5":
        print("Exiting program... Bye!")
        break
    else:
        print("Wrong input! Please choose between 1-5.")
