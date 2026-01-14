from datetime import datetime
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()
db_conn = os.getenv("DB_CONNECTION")
app_name = os.getenv("APP_NAME", "Task Manager")
app_owner = os.getenv("APP_OWNER", "AK")

app = FastAPI(title=app_name, version=app_owner)

# in memory database
tasks = []

@app.get("/")
def root():
    return{
        "message": f"Welcome to {app_name}",
        "owner": app_owner,
        "total_tasks": len(tasks)
    }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: dict):
    task["id"] = len(tasks) + 1
    task["name"] = task["name"]
    task["is_completed"] = task["is_completed"]
    task["created_at"] = datetime.now()    
    tasks.append(task)
    return {
        "message": "Task added successfully",
        "task": task
        }

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {
        "message": "Task deleted successfully",
        "task": tasks
        }

@app.put("/tasks/{tasks_id}")
def update_task(tasks_id: int, update_data: dict):
    for task in tasks:
        if task["id"] == tasks_id:
            if "name" in update_data:
                task["name"] = update_data["name"]
            if "is_completed" in update_data:
                task["is_completed"] = update_data["is_completed"]
            return {
                "message": "Task updated successfully",
                "task": task
                }
    raise HTTPException(status_code=404, detail="Task not found")
            
    
# testing dotenv
# print(db_conn)