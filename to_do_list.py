print("1. View task")
print("2. Add task")
print("3. Remove task")
print("4. Exit")
task = None
task = []
while task != 4:
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        if not task:
            print("No task available")
        else:
            print(task)
    elif choice == 2:
        add_task = input("Enter task: ")
        task.append(add_task)
        print("{} has been added to the list" .format(task))
    elif choice == 3:
        remove_task = input("Enter the task you want to remove: ")
        task.remove(remove_task)
        print("{} has been removed the list" .format(task))
    elif choice == 4:
        break
    else:
        print("Invalid option")
    
