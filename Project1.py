#Project – To-Do List (Console App)

tasks = [] #list to store all tasks

while True:
    print("\n---- TO-DO LIST ----")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        #Add a Task
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        #View Task
        if len(tasks) == 0:
            print("No task in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        #Remove a Task
        if len(tasks) == 0:
            print("No task in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
            task_no = input("Enter task number to remove:")
            #Validation input is a number
            if task_no.isdigit():
                task_no = int(task_no)
                if 1 <= task_no <= len(tasks):
                    remove = tasks.pop(task_no - 1)
                    print("Remove task", remove)

                else:
                    print("Please enter a valid number!")

    elif choice == "4":
        #Exit
        print("Esiting the TO-DO List, Goodbye!")
        break
    else:
        print("Invalid choice, PLease enter a valid choice (1-4)!")
        