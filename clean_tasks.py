tasks = ["  study", "exercise  ", " ", "read book", "  "]

def clean_count_tasks():
    global tasks
    clean_task = [task.strip().capitalize() for task in tasks if task.strip()!=""]
    clean_task.sort()
    return clean_task

final_tasks = clean_count_tasks() 
print(final_tasks)