checkList = []
completed_tasks = []
incomplete_tasks= []

num = int(input("How many tasks you want to add :" ))
for i in range(num):
    task = input(f"Enter Task {i+1} :")
    checkList.append(task)

for i in checkList:
    check = input(f"did you complete {i} ? (yes/no):")
    if(check == 'yes'):
        completed_tasks.append(i)
    else:
        incomplete_tasks.append(i)
        
for task in completed_tasks:
    print('completed tasks', task)
    
for task in incomplete_tasks:
    print('in_completed Tasks', task)