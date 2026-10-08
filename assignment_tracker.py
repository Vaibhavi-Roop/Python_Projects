total_assignments = 4
original_count = total_assignments
completed_count = 0
task_num = 1
while task_num<=total_assignments:
    if task_num == 1:
        next_task = " Math"
    elif task_num == 2:
        next_task = " English"
    elif task_num == 3:
        next_task = " Science"
    else:
        next_task = " Coding"
    completion = input(f"Have you finished{next_task}? (yes/no):")
    if completion == 'yes':
        completed_count += 1
        task_num += 1
    else:
        print("Task not completed yet")
    print("You have", total_assignments - completed_count, "assignments left.")
    incomplete_count = total_assignments - completed_count
    if incomplete_count == 0:
        print("You have finished all of your assignments")