import json
import os
import sys
from datetime import datetime
import argparse

# Define the task file
TASK_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return {}
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The tasks file is corrupted. Creating a new tasks file.")
        return {}

# Save tasks to the JSON file
def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")
        print("Warning: Changes have not been saved. Please check the file system.")

# Generate a unique ID for a new task
def generate_id(tasks):
    return max(tasks.keys(), default=0) + 1

# Validate task status
def is_valid_status(status):
    return status in ["todo", "in-progress", "done"]

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    now = datetime.now().isoformat()
    tasks[task_id] = {
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    task_id = str(task_id)  # Ensure task_id is a string
    if task_id in tasks:
        tasks[task_id]["description"] = new_description
        tasks[task_id]["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} updated to: {new_description}")
    else:
        print("Task not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    task_id = str(task_id)  # Convert task_id to a string
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task deleted: {deleted_task['description']}")
    else:
        print("Task not found.")

# Change task status
def change_status(task_id, status):
    tasks = load_tasks()
    if status not in ["todo", "in-progress", "done"]:
        print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
        return
    task_id = str(task_id)  # Convert task_id to a string
    if task_id in tasks:
        tasks[task_id]["status"] = status
        tasks[task_id]["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} status updated to: {status}")
    else:
        print("Task not found.")

# List tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    print(f"Loaded tasks: {tasks}")  # Debugging print
    print(f"Filter status: {filter_status}")  # Debugging print

    if filter_status and filter_status != "all":
        filtered_tasks = {
            tid: task for tid, task in tasks.items() if task["status"] == filter_status
        }
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
    else:
        for tid, task in filtered_tasks.items():
            print(
                f"ID: {tid}, Description: {task['description']}, "
                f"Status: {task['status']}, Created At: {task['createdAt']}, "
                f"Updated At: {task['updatedAt']}"
            )


# CLI interface
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("description", type=str, help="New description for the task")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # Mark-in-progress command
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_mark_in_progress.add_argument("id", type=int, help="ID of the task to mark in progress")

    # Mark-done command
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="ID of the task to mark as done")

    # List command
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", type=str, nargs="?", choices=["all", "done", "todo", "in-progress"], default="all", help="Filter tasks by status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        change_status(args.id, "in-progress")
    elif args.command == "mark-done":
        change_status(args.id, "done")
    elif args.command == "list":
        if args.status == "all":
            list_tasks()
        else:
            list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
