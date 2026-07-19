def toDo():
    tasks=[]
    print("Welcome to task managment app 😊")
    while True:
        try :
            total_task= int(input("Enter number of task = "))
        except ValueError:
            print("Enter a number !!")
            continue
        for i in range(1,total_task+1):
            task =input(f"Enter task {i}. ")
            tasks.append(task)
        print(f"Today's tasks are \n {tasks}")
        while True:
             operation = int(input("\nEnter 1 for Adding task \n Enter 2 for Update task \n Enter 3 for Delete task \n Enter 4 for View tasks \n Enter 5 to Exit \n = "))
             if operation==1:
                task_add = input("Enter new task = ")
                if task_add in tasks:
                    print(f"Task {task_add} already exist in To-DO List 😅")
                else:
                    tasks.append(task_add)
                    print(f"added {task_add} to the To-Do List 😁")
             elif operation==2:
                task_update =input("Enter task you want to update = ")
                if task_update in tasks:
                    new_task = input("Enter task you want to add = ")
                    ind = tasks.index(task_update)
                    tasks[ind]=new_task
                    print(f"{new_task} is updated in  To-DO List 😁 ")
                else:
                     print(f"{task_update} does not exist in To-DO List 😅")
             elif operation==3:
                task_delete = input("Enter the task you want to delete = ")
                if task_delete in tasks:
                     ind =tasks.index(task_delete)
                     tasks.pop(ind)
                     print(f"{task_delete} is removed from To-DO List 😁")
                     print(tasks)
                else:
                     print("Task does not exists in To-DO List 😅")
             elif operation==4 :
                print("To-DO List : ")
                print(tasks)
             elif operation ==5:
                print("Thank you for using To-DO List 😊 ")
                break
             else:
                print("Invalid Input 😒 !!")
        break


toDo()