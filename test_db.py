import sqlite3
from db_connection import add_task, delete_task, update_task, get_all_tasks, get_tasks_for_date, get_tasks_between_dates, get_task_by_id

db = sqlite3.connect("task_management.db")

print("### printing all tasks###")
all_tasks = get_all_tasks(db)
for task in all_tasks:
    print(task)

print("### printing one day tasks###")   
one_day_task = get_tasks_for_date(db, "2017-09-09")
for task in one_day_task:
    print(task)

print("### printing tasks between dates###")  
tasks_between = get_tasks_between_dates(db, "2017-01-01", "2019-01-01")
for task in tasks_between:
    print(task)
    
id = get_task_by_id(db, 1)
print(id)