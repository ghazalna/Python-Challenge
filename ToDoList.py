task_name = []
status = []
duration = []

for i in range(200):
    answer = input (" Add Task, Display, Remove, Edit, Search, Mark Task as Done, Details,Help, Exit : ").lower()
    
    
    #Add
    if answer == "add task":
        task = input("Write a new Task: ").lower()
        if task not in task_name:
            task_name.append(task)
            status.append(False)
            duration.append(None)
            print("Added!")
            
        else:
            print("Already Exit! ")
            

    #Display
    elif answer == "display":
        for i , task in enumerate(task_name):
            print(f"{i + 1}. {task} - Status: {'Done' if status[i] else 'Incomplete'}, Duration: {duration[i]} minutes")
    
    
    #Remove
    elif answer == "remove":
        task = input ( "write a task for removing: ").lower()
        if task in task_name:
            i = task_name.index(task)
            task_name.pop(i)
            status.pop(i)
            duration.pop(i)
            print("Removed!")
        else:
            print("Task doesn't Exit! ")
    
    #Edit
    elif answer == "edit":
        task = input ( "Write a task for editing: ").lower()
        if task in task_name:
            new_name = input("Write a new name for task : ").lower()
            if new_name not in task_name:
                i = task_name.index(task)
                task_name[i] = new_name
                print("Edited! ")
            else:
                print("Already Exist! ")
        else:
            print("Task Not Exist! ")
    
    #Search
    elif answer == "search" :
        name = input("Name for Search :").lower()
        if name in task_name:
            i = task_name.index(name)
            status = status[i]
            duration = duration[i]
            print(f"Status: {status}, Duration: {duration}")
        else:
            print("Not Found!")
    
    #Mark Task as Done
    elif answer == "mark task as done":
        name = input("Name of Task :").lower()
        if name in task_name:
            add_duration = float(input(f"Duration of {name} (in hours): "))
            add_duration_minutes = add_duration * 60
            i = task_name.index(name)
            status[i] = True
            duration[i] = add_duration_minutes
            print("Done!")
            
        else:
            print("Not Found!")
    
    #Details
    elif answer == "details":
        numbers = len(task_name)
        not_completed = status.count(False)
        #purchased = product_is_bought.count(True)
        completed = sum(status)
        
        print (f" Number of Task : {numbers}")
        print (f" Number of Completed : {completed}")
        print (f" number of not Completed : {not_completed}")
        
        add_duration_minutes = []
        for d in duration:
            if d:
                add_duration_minutes.append(d)
        sum_duration = sum(add_duration_minutes)
        print (f" Total Duration : {sum_duration}")
        
    
    
    #Help
    elif answer == "help":
        print("""
        Available Commands:
        - add task: Add a new task to the list.
        - display: Show all tasks with their statuses and durations.
        - remove: Remove a task from the list.
        - edit: Edit the name of an existing task.
        - search: Search for a task and display its status and duration.
        - mark task as done: Mark a task as completed and set its duration.
        - details: Show the total number of tasks, the number of completed and incomplete tasks, and the total duration.
        - exit: Exit the program.
        """)
    
    #Exit
    elif answer == "exit":
        break

    else:
        print ("Not Found! ")