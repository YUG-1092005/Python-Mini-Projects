print("----------TODO APP----------")

List = []
completed = []

while True:
    menu = ''.join(f'\n1.Add{"\n"}2.Remove{"\n"}3.View{"\n"}4.Mark as done{"\n"}5.Completed Tasks{"\n"}6.Exit'"\n")
    print(menu)
    choice = input("Enter your choice no. from menu: ")
    if choice == "Add" or choice=="1":
        #adding task
        task = input("Enter your task to add: ")
        List.append(task)
        newTask = ' '"\n".join(List)
        print("Task added.")

    elif choice == "Remove"or choice=="2":
        #remove task
        task = input("Enter your task name to remove: ")
        List.remove(task)
        print(f"{task} removed.")

    elif choice == "View" or choice=="3":
        #view tasks
        print("Your current pending tasks.")
        print(' '"\n".join(List))
    
    elif choice == "Mark as done" or choice=="4":
        #marking done tasks
        done = input("Enter your completed task name: ")
        List.remove(done)
        completed.append(done)
        print("Success.")
    
    elif choice == "Completed Tasks" or choice=="5":
        #showing completed tasks
        if len(completed) == 0:
            print("No tasks completed yet..")
        else:
            print(''"\n".join(completed))


    elif choice == "Exit" or choice=="6":
        print(' '"\n".join(List))
        break
print("Have a nice day!")











